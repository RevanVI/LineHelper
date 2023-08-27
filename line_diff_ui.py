import wx
import line_helper

class LineDiffUI(wx.Panel):

    def __init__(self, parent):
        super(LineDiffUI, self).__init__(parent) 
        self.InitUI()


    def InitUI(self):
        sizer = wx.GridBagSizer(6, 2)

        #ignore duplicates check box
        self.ignore_duplicates_chb = wx.CheckBox(self, label = "Ignore duplicates")
        #sizer.Add(self.ignore_duplicates_chb, pos = (0, 0), flag = wx.TOP | wx.LEFT, border = 10)

        self.ignore_whitespaces_chb = wx.CheckBox(self, label = "Ignore empty lines")
        #sizer.Add(self.ignore_duplicates_chb, pos = (0, 0), flag = wx.TOP | wx.LEFT, border = 10)

        vert_sizer = wx.BoxSizer(wx.VERTICAL)
        vert_sizer.Add(self.ignore_duplicates_chb, flag = wx.TOP | wx.LEFT, border = 10)
        vert_sizer.Add(self.ignore_whitespaces_chb, flag = wx.TOP | wx.LEFT, border = 10)

        sizer.Add(vert_sizer, pos = (0, 0))
        #labels for line input
        input1_text = wx.StaticText(self, label = "List 1:")
        sizer.Add(input1_text, pos= (1, 0), flag = wx.TOP | wx.LEFT, border = 10)

        intput2_text = wx.StaticText(self, label = "List 2:")
        sizer.Add(intput2_text, pos= (1, 1), flag = wx.TOP, border = 10)

        #input and output text controls
        self.input1_tc = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.HSCROLL)
        sizer.Add(self.input1_tc, pos = (2, 0), flag = wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT, border = 10)
        
        self.input2_tc = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.HSCROLL)
        sizer.Add(self.input2_tc, pos = (2, 1), flag = wx.EXPAND | wx.RIGHT | wx.TOP, border = 10)

        #labes for diff
        diff_text = wx.StaticText(self, label = "Diff:")
        sizer.Add(diff_text, pos = (3, 0), flag = wx.LEFT | wx.TOP, border = 10)

        #diff text ctrl
        self.diff_tc = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.HSCROLL | wx.TE_READONLY)
        sizer.Add(self.diff_tc, pos = (4, 0), span = (1, 2), flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border = 10)

        #diff button
        self.buttonDiff = wx.Button(self, label="Diff")
        self.buttonDiff.Bind(wx.EVT_BUTTON, self.OnDiffButtonClicked, self.buttonDiff)
        sizer.Add(self.buttonDiff, pos=(5, 1), flag= wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border = 10)

        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(4)
        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)


    def OnDiffButtonClicked(self, e):
        lines_left = []
        for i in range (0, self.input1_tc.GetNumberOfLines()):
            lines_left.append(self.input1_tc.GetLineText(i))

        lines_right = []
        for i in range (0, self.input2_tc.GetNumberOfLines()):
            lines_right.append(self.input2_tc.GetLineText(i))

        if self.ignore_whitespaces_chb.IsChecked():
            line_helper.RemovEmptyStrings(lines_left)
            line_helper.RemovEmptyStrings(lines_right)

        ignore_duplicates = self.ignore_duplicates_chb.IsChecked()
        only_left, only_right, both = line_helper.CompareLines(lines_left, lines_right, ignore_duplicates)        
        
        self.diff_tc.Clear()
        self.diff_tc.AppendText("Only in left:\n")
        for line, count in only_left.items():
            self.diff_tc.AppendText(line)
            if not ignore_duplicates:
                self.diff_tc.AppendText(f" {count}")
            self.diff_tc.AppendText("\n")

        self.diff_tc.AppendText("\n\n")

        self.diff_tc.AppendText("Only in right:\n")
        for line, count in only_right.items():
            self.diff_tc.AppendText(line)
            if not ignore_duplicates:
                self.diff_tc.AppendText(f" {count}")
            self.diff_tc.AppendText("\n")

        self.diff_tc.AppendText("\n\n")

        self.diff_tc.AppendText("In both:\n")
        for line, count in both.items():
            self.diff_tc.AppendText(line)
            if not ignore_duplicates:
                self.diff_tc.AppendText(f" {count}")
            self.diff_tc.AppendText("\n")
        

def main():
    app = wx.App()
    frame = wx.Frame(None, title='Line Diff')
    ex = LineDiffUI(frame)
    frame.SetMinSize(frame.GetSize())
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()