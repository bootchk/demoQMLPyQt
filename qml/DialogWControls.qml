/*
Dialog containing row of controls
*/

import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2

import "dialogs" as MyDialogs

import QmlDelegate 1.0


Item {

	
	DialogDelegate {
		id: dialogDelegate
		objectName: "dialogDelegate"
	}
	
	
	MyDialogs.Dialog2 {
		id: dialog
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
