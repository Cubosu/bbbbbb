///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxGridSizer* gSizer1;
	gSizer1 = new wxGridSizer( 0, 2, 0, 0 );


	this->SetSizer( gSizer1 );
	this->Layout();
	m_menubar1 = new wxMenuBar( 0 );
	first = new wxMenu();
	wxMenuItem* m_menuItem1;
	m_menuItem1 = new wxMenuItem( first, wxID_ANY, wxString( wxT("建立檔案") ) , wxEmptyString, wxITEM_NORMAL );
	first->Append( m_menuItem1 );

	wxMenuItem* m_menuItem2;
	m_menuItem2 = new wxMenuItem( first, wxID_ANY, wxString( wxT("開啟檔案") ) , wxEmptyString, wxITEM_NORMAL );
	first->Append( m_menuItem2 );

	wxMenuItem* m_menuItem3;
	m_menuItem3 = new wxMenuItem( first, wxID_ANY, wxString( wxT("儲存檔案") ) , wxEmptyString, wxITEM_NORMAL );
	first->Append( m_menuItem3 );

	wxMenuItem* m_menuItem4;
	m_menuItem4 = new wxMenuItem( first, wxID_ANY, wxString( wxT("關閉程式") ) , wxEmptyString, wxITEM_NORMAL );
	first->Append( m_menuItem4 );

	m_menubar1->Append( first, wxT("檔案") );

	m_menu6 = new wxMenu();
	wxMenuItem* m_menuItem5;
	m_menuItem5 = new wxMenuItem( m_menu6, wxID_ANY, wxString( wxT("作者介紹") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu6->Append( m_menuItem5 );

	m_menubar1->Append( m_menu6, wxT("關於") );

	this->SetMenuBar( m_menubar1 );


	this->Centre( wxBOTH );
}

MyFrame1::~MyFrame1()
{
}
