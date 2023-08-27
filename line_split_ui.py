import wx
import line_helper

class LineSplitUI(wx.Panel):

    def __init__(self, parent):
        super(LineSplitUI, self).__init__(parent) 
        self.InitUI()

    def InitUI(self):
        sizer = wx.GridBagSizer(4, 3)

        #separator input
        separator_text = wx.StaticText(self, label = "Separator:")
        self.separator_tc = wx.TextCtrl(self)
        
        hboxsizer = wx.BoxSizer(orient = wx.HORIZONTAL)
        hboxsizer.Add(separator_text, flag = wx.TOP | wx.LEFT | wx.RIGHT, border = 10)
        hboxsizer.Add(self.separator_tc, proportion = 1, flag = wx.TOP | wx.RIGHT | wx.EXPAND, border = 10)
        sizer.Add(hboxsizer, pos = (0, 0), span = (1, 3), flag = wx.EXPAND)

        #labels for line input
        input_text = wx.StaticText(self, label = "Input lines:")
        sizer.Add(input_text, pos= (1, 0), flag = wx.TOP | wx.LEFT, border = 10)

        output_text = wx.StaticText(self, label = "Output lines:")
        sizer.Add(output_text, pos= (1, 2), flag = wx.TOP, border = 10)

        #input and output text controls
        self.input_tc = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.HSCROLL)
        sizer.Add(self.input_tc, pos = (2, 0), flag = wx.EXPAND | wx.LEFT | wx.TOP, border = 10)
        
        self.output_tc = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.HSCROLL |wx.TE_READONLY)
        sizer.Add(self.output_tc, pos = (2, 2), flag = wx.EXPAND | wx.RIGHT | wx.TOP, border = 10)

        #split button
        self.buttonSplit = wx.Button(self, label="Split")
        self.buttonSplit.Bind(wx.EVT_BUTTON, self.OnSplitButtonClicked, self.buttonSplit)
        sizer.Add(self.buttonSplit, pos=(3, 2), flag= wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border = 10)

        sizer.AddGrowableRow(2)
        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(2)
        self.SetSizer(sizer)


    def OnSplitButtonClicked(self, e):
        separator = self.separator_tc.GetValue()
        lines = []
        for i in range (0, self.input_tc.GetNumberOfLines()):
            lines.append(self.input_tc.GetLineText(i))

        result = []
        for line in lines:
            result += line_helper.SplitLine(line, separator)
            print(result)
        
        self.output_tc.Clear()
        for line in result:
            self.output_tc.AppendText(line + "\n")
        

def main():
    app = wx.App()
    frame = wx.Frame(None, title='Line Split')
    LineSplitUI(frame)
    frame.SetMinSize(frame.GetSize())
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()