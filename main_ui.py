import wx
import line_diff_ui
import line_split_ui

class MainUI(wx.Frame):

    def __init__(self, parent, title):
        super(MainUI, self).__init__(parent, title=title) 
        self.InitUI()
        self.FillPages()

        self.SetMinSize(self.GetSize())


    def InitUI(self):
        panel = wx.Panel(self)
        self.notepad = wx.Notebook(panel)

        vert_sizer = wx.BoxSizer(wx.VERTICAL)
        vert_sizer.Add(self.notepad, flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 10)
        panel.SetSizer(vert_sizer)

        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText("Idle")


    def FillPages(self):
        page = line_diff_ui.LineDiffUI(self.notepad)
        self.notepad.AddPage(page, "Line Diff")

        page = line_split_ui.LineSplitUI(self.notepad)
        self.notepad.AddPage(page, "Line Split")

        self.notepad.SetSize(self.notepad.GetMinClientSize())

def main():
    app = wx.App()
    ex = MainUI(None, title='Line Helpers')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()