/*
Test menu

- popup
- set position??
- how closes
- whether a QWidget picker can open it properly

*/

import QtQuick 2.2
import QtQuick.Controls 1.2



Item {
	
	// ContextMenu is Qt Quick 1.0, or only DesktopComponents?
	
	Menu {
		id: menu
	    title: "&Choosers"
	    /*
	    Read QML Menu doc
	    'visible' is not a property unless a submenu.
	    This is currently a top-level menu.
	    */ 
	    // Some posts suggest a hidden property? _xOffset: 10
	    
	    MenuItem { text: "bar"  }
	    MenuItem { text: "foo" }
	}
	
	Button {
		text: "Show menu"
		
		/*
		Pos is not a parameter (mouseX, mouseY) or (300, 50)
		It always opens at pointer (cursor)
		No way to offset it so that certain item is under cursor?
		Does it center on phones?
		*/
		onClicked: menu.popup()
	}
	
	// contextMenu.showPopup(mouseX,mouseY)
}
