/*
Dialog custom
*/

import QtQuick 2.4
import QtQuick.Controls 1.3
//import QtQuick.Dialogs 1.2

import "../dialogs" as MyDialogs

import QmlDelegate 1.0


Item {

	DialogDelegate {
		id: dialogDelegate
		objectName: "dialogDelegate"
	}
	
	/*
	 * Not a QML Dialog but a QML Window configured as a dialog.
	 */
	MyDialogs.WindowAsDialog{
		id: dialog
	}

	 
	 Connections {
    	// target is id of thing emitting signal
    	// control must exist (preceding this in the source file.)
	    target: dialogDelegate
	    onActivated: {
	    	console.log("Dialog activated")
	    	// the id of an object is not accessible except to dereference by its value
	    	console.log("delegate id:", dialogDelegate.id)
	    	console.log("delegate objectName:", dialogDelegate.objectName)
	    	//dialog.open()
	    	dialog.show()
	    }	
	 }
}
