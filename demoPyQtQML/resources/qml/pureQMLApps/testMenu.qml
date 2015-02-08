/*
Test menu, pure QML, inside 

- popup
- set position??
- how closes
- whether a QWidget picker can open it properly

*/

import QtQuick 2.4
import QtQuick.Controls 1.3

import "../menus" as MyMenu

ApplicationWindow {
    visible: true
    title: "Test "

    width: 640
    height: 420
    minimumHeight: 400
    minimumWidth: 600

		
	// ContextMenu is Qt Quick 1.0, or only DesktopComponents?
	// contextMenu.showPopup(mouseX,mouseY)
	
	MyMenu.Menu {
		id: menu
	}
	
    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.RightButton
        onPressed: menu.popup()
    }
	
	Text {
		text: "RMB to popup menu under cursor"
	}
}
