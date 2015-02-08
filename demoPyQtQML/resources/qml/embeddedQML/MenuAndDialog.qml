/*
A context menu for person.

Opens on receiving signal personChanged.

Menu item of context menu in turn calls dialogDelegate to show another dialog.
This sequence did not work on OSX??
*/

import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Dialogs 1.2

import "../menus" as MyMenu
import "../dialogs" as MyDialogs

import People 1.0
import QmlDelegate 1.0


Item {
	
	
	// Mock a picker object: known to QGraphicsView (using findChild())
	// with a method that emits personChanged.
	Person {
		id: person
		objectName: "person"
	    name: "Bob Jones"
	    shoeSize: 12
	}
	
	DialogDelegate {
		id: dialogDelegate
		objectName: "dialogDelegate"
	}
	
	
	MyMenu.MenuCallingDialog {
		id: menu
	}
	
	MyDialogs.Dialog3 {
		id: dialog
	}
	
	Connections {
    	// id of thing emitting signal
    	// control must exist (preceding this in the source file.)
	    target: person
	    onPersonChanged: {
	    	console.log("Person clicked")
	    	menu.popup()
	    }	
	 }
	 
	 Connections {
    	// target is id of thing emitting signal
    	// control must exist (preceding this in the source file.)
	    target: dialogDelegate
	    onActivated: {
	    	console.log("Dialog activated")
	    	dialog.open()
	    }	
	 }
}
