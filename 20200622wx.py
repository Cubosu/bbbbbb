# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.combo
import wx.adv
import wx.grid
import wx.dataview

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 980,746 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_auinotebook4 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_panel75 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self.m_panel75, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self.m_panel75, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self.m_panel75, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self.m_panel75, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button7, 0, wx.ALL, 5 )

		m_comboBox3Choices = [ u"1", u"2", u"3", u"4", u"5", wx.EmptyString, wx.EmptyString ]
		self.m_comboBox3 = wx.ComboBox( self.m_panel75, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		self.m_comboBox3.SetSelection( 3 )
		bSizer3.Add( self.m_comboBox3, 0, wx.ALL, 5 )

		self.m_bcomboBox1 = wx.combo.BitmapComboBox( self.m_panel75, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0 )
		bSizer3.Add( self.m_bcomboBox1, 0, wx.ALL, 5 )

		self.m_bcomboBox2 = wx.combo.BitmapComboBox( self.m_panel75, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 )
		bSizer3.Add( self.m_bcomboBox2, 0, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self.m_panel75, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self.m_panel75, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer3.Add( self.m_choice1, 0, wx.ALL, 5 )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.m_panel75, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer3.Add( self.m_listBox1, 0, wx.ALL, 5 )


		self.m_panel75.SetSizer( bSizer3 )
		self.m_panel75.Layout()
		bSizer3.Fit( self.m_panel75 )
		self.m_auinotebook4.AddPage( self.m_panel75, u"a page", False, wx.NullBitmap )
		self.m_panel76 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox2 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox4, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox5, 0, wx.ALL, 5 )

		self.m_checkBox6 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox6, 0, wx.ALL, 5 )

		self.m_checkBox7 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox7, 0, wx.ALL, 5 )

		self.m_checkBox8 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox8, 0, wx.ALL, 5 )

		self.m_checkBox9 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox9, 0, wx.ALL, 5 )

		self.m_checkBox10 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox10, 0, wx.ALL, 5 )

		self.m_checkBox11 = wx.CheckBox( self.m_panel76, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox11, 0, wx.ALL, 5 )


		self.m_panel76.SetSizer( fgSizer1 )
		self.m_panel76.Layout()
		fgSizer1.Fit( self.m_panel76 )
		self.m_auinotebook4.AddPage( self.m_panel76, u"a page", False, wx.NullBitmap )
		self.m_panel77 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_toggleBtn1 = wx.ToggleButton( self.m_panel77, wx.ID_ANY, u"Toggle me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.m_searchCtrl1 = wx.SearchCtrl( self.m_panel77, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		gSizer4.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )

		self.m_colourPicker1 = wx.ColourPickerCtrl( self.m_panel77, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gSizer4.Add( self.m_colourPicker1, 0, wx.ALL, 5 )

		self.m_fontPicker1 = wx.FontPickerCtrl( self.m_panel77, wx.ID_ANY, wx.NullFont, wx.DefaultPosition, wx.DefaultSize, wx.FNTP_DEFAULT_STYLE )
		self.m_fontPicker1.SetMaxPointSize( 100 )
		gSizer4.Add( self.m_fontPicker1, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel77, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer4.Add( self.m_filePicker1, 0, wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self.m_panel77, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gSizer4.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self.m_panel77, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer4.Add( self.m_datePicker1, 0, wx.ALL, 5 )

		self.m_timePicker1 = wx.TimePickerCtrl( self.m_panel77, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.TP_DEFAULT )
		gSizer4.Add( self.m_timePicker1, 0, wx.ALL, 5 )

		self.m_calendar1 = wx.adv.CalendarCtrl( self.m_panel77, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		gSizer4.Add( self.m_calendar1, 0, wx.ALL, 5 )

		self.m_scrollBar1 = wx.ScrollBar( self.m_panel77, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_HORIZONTAL )
		gSizer4.Add( self.m_scrollBar1, 0, wx.ALL, 5 )


		self.m_panel77.SetSizer( gSizer4 )
		self.m_panel77.Layout()
		gSizer4.Fit( self.m_panel77 )
		self.m_auinotebook4.AddPage( self.m_panel77, u"a page", False, wx.NullBitmap )
		self.m_panel79 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox13 = wx.CheckBox( self.m_panel79, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_checkBox13, 0, wx.ALL, 5 )

		m_radioBox3Choices = [ u"Radio Button" ]
		self.m_radioBox3 = wx.RadioBox( self.m_panel79, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox3.SetSelection( 0 )
		fgSizer2.Add( self.m_radioBox3, 0, wx.ALL, 5 )

		self.m_radioBtn1 = wx.RadioButton( self.m_panel79, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_slider1 = wx.Slider( self.m_panel79, wx.ID_ANY, 5, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer2.Add( self.m_slider1, 0, wx.ALL, 5 )

		self.m_gauge1 = wx.Gauge( self.m_panel79, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 60 )
		fgSizer2.Add( self.m_gauge1, 0, wx.ALL, 5 )


		self.m_panel79.SetSizer( fgSizer2 )
		self.m_panel79.Layout()
		fgSizer2.Fit( self.m_panel79 )
		self.m_auinotebook4.AddPage( self.m_panel79, u"a page", False, wx.NullBitmap )
		self.m_panel78 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook4.AddPage( self.m_panel78, u"a page", False, wx.NullBitmap )
		self.m_panel80 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook4.AddPage( self.m_panel80, u"a page", True, wx.NullBitmap )
		self.m_panel81 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook4.AddPage( self.m_panel81, u"a page", False, wx.NullBitmap )
		self.m_panel82 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook4.AddPage( self.m_panel82, u"a page", False, wx.NullBitmap )
		self.m_panel83 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook4.AddPage( self.m_panel83, u"a page", False, wx.NullBitmap )
		self.m_panel84 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook4.AddPage( self.m_panel84, u"a page", False, wx.NullBitmap )

		gSizer2.Add( self.m_auinotebook4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_auinotebook9 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_panel86 = wx.Panel( self.m_auinotebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_scrollBar2 = wx.ScrollBar( self.m_panel86, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_HORIZONTAL )
		gSizer5.Add( self.m_scrollBar2, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self.m_panel86, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer5.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_spinBtn1 = wx.SpinButton( self.m_panel86, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_spinBtn1, 0, wx.ALL, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self.m_panel86, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer5.Add( self.m_hyperlink1, 0, wx.ALL, 5 )

		self.m_hyperlink2 = wx.adv.HyperlinkCtrl( self.m_panel86, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer5.Add( self.m_hyperlink2, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self.m_panel86, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer5.Add( self.m_grid1, 0, wx.ALL, 5 )


		gSizer5.Add( self.m_customControl1, 0, wx.ALL, 5 )

		self.m_genericDirCtrl1 = wx.GenericDirCtrl( self.m_panel86, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl1.ShowHidden( False )
		gSizer5.Add( self.m_genericDirCtrl1, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer5.Add( self.m_customControl2, 0, wx.ALL, 5 )


		self.m_panel86.SetSizer( gSizer5 )
		self.m_panel86.Layout()
		gSizer5.Fit( self.m_panel86 )
		self.m_auinotebook9.AddPage( self.m_panel86, u"a page", False, wx.NullBitmap )
		self.m_panel87 = wx.Panel( self.m_auinotebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook9.AddPage( self.m_panel87, u"a page", True, wx.NullBitmap )
		self.m_panel88 = wx.Panel( self.m_auinotebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid2 = wx.grid.Grid( self.m_panel88, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 5, 5 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer4.Add( self.m_grid2, 0, wx.ALL, 5 )

		m_checkList2Choices = []
		self.m_checkList2 = wx.CheckListBox( self.m_panel88, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList2Choices, 0 )
		bSizer4.Add( self.m_checkList2, 0, wx.ALL, 5 )

		self.m_treeListCtrl1 = wx.dataview.TreeListCtrl( self.m_panel88, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.m_treeListCtrl1.AppendColumn( u"Column1", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

		bSizer4.Add( self.m_treeListCtrl1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel88, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_dataViewListCtrl1, 0, wx.ALL, 5 )


		self.m_panel88.SetSizer( bSizer4 )
		self.m_panel88.Layout()
		bSizer4.Fit( self.m_panel88 )
		self.m_auinotebook9.AddPage( self.m_panel88, u"a page", False, wx.NullBitmap )

		gSizer2.Add( self.m_auinotebook9, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_menu11 = wx.Menu()
		self.Bind( wx.EVT_RIGHT_DOWN, self.MyFrame1OnContextMenu )

		self.m_statusBar2 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu9 = wx.Menu()
		self.m_menu4 = wx.Menu()
		self.m_menu9.AppendSubMenu( self.m_menu4, u"開啟" )

		self.m_menu6 = wx.Menu()
		self.m_menu9.AppendSubMenu( self.m_menu6, u"結束" )

		self.m_menu91 = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.m_menu91, wx.ID_ANY, u"不給你按", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu91.Append( self.m_menuItem12 )
		self.m_menuItem12.Enable( False )

		self.m_menu9.AppendSubMenu( self.m_menu91, u"存檔" )

		self.m_menubar2.Append( self.m_menu9, u"檔案" )

		self.m_menu10 = wx.Menu()
		self.m_menubar2.Append( self.m_menu10, u"編輯" )

		self.SetMenuBar( self.m_menubar2 )

		self.m_toolBar3 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_tool1 = self.m_toolBar3.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar3.Realize()


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

	def MyFrame1OnContextMenu( self, event ):
		self.PopupMenu( self.m_menu11, event.GetPosition() )


a = wx.App()
w = MyFrame1(None)
w.Show()
a.MainLoop()