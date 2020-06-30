
import w20200630
import wx
import codecs


class homework ( w20200630.MyFrame1 ):


	def build_file( self, event ):
		wx.Image(檔案串流, 圖片類型)

	def open_file( self, event ):
		p=wx.FileSelector(
		"請選擇要開啟的檔案",
		wildcard= "Txt文字 (*.txt)|*.txt",
		flags=wx.FD_OPEN
		)

		with codecs.open(p,"r") as file:
			file.read()

		

	def save_file( self, event ):
		r=wx.FileSelector(
		"請選擇要開啟的檔案",
		wildcard= "Txt文字 (*.txt)|*.txt",
		flags=wx.FD_SAVE
		)
		
	def close_file( self, event ):
		wx.Exit()

	def about_me( self, event ):
		event.Skip()






app = wx.App()
win = homework(None)
win.Show()
app.MainLoop()