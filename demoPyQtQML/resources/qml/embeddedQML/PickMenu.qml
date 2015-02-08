/*
A context menu for person.

Opens on receiving signal personChanged.
*/

import QtQuick 2.4
import QtQuick.Controls 1.3

import "menus" as MyMenu

import People 1.0


Item {
	
	
	// Mock a picker object: known to QGraphicsView (using findChild())
	// with a method that emits personChanged.
	Person {
		id: person
		objectName: "person"
	    name: "Bob Jones"
	    shoeSize: 12
	}
	
	
	MyMenu.Menu {
		id: menu
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
}
