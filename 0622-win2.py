
import mywindows
import wx

class MyFrame2 ( mywindows.MyFrame2 ):

	def hey( self, event ):
		self.m_grid3.AppendCols(3)
		self.m_grid3.AppendRows(3)

	def bnm( self, event ):
		pass

	def idj( self, event ):
		event.Skip()

	def keu( self, event ):
		event.Skip()





a = wx.App()
w = mywindows.MyFrame2(None)
w.Show()
a.MainLoop()