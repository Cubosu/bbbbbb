# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 953,652 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )


		self.SetSizer( gSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.first = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.first, wx.ID_ANY, u"建立檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.first.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.first, wx.ID_ANY, u"開啟檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.first.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.first, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.first.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.first, wx.ID_ANY, u"關閉程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.first.Append( self.m_menuItem4 )

		self.m_menubar1.Append( self.first, u"檔案" )

		self.m_menu6 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"作者介紹", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.m_menuItem5 )

		self.m_menubar1.Append( self.m_menu6, u"關於" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_file, id = self.m_menuItem1.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def open_file( self, event ):
		event.Skip()


