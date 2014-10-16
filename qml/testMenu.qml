/*
Test menu, pure QML, inside 

- popup
- set position??
- how closes
- whether a QWidget picker can open it properly

*/

import QtQuick 2.2
import QtQuick.Controls 1.2

ApplicationWindow {
    visible: true
    title: "Test "

    width: 640
    height: 420
    minimumHeight: 400
    minimumWidth: 600

		
	// ContextMenu is Qt Quick 1.0, or only DesktopComponents?
	
    // A context menu to be popped up with RMB in app window
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
	
    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.RightButton
        onPressed: menu.popup()
    }
	
	// contextMenu.showPopup(mouseX,mouseY)
}
