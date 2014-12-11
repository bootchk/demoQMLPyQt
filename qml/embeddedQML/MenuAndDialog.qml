/*
A context menu for person.

Opens on receiving signal personChanged.
*/

import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2

import "menus" as MyMenu
import "dialogs" as MyDialogs

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
	
	
	MyMenu.Menu {
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
