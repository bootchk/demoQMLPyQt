import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2

import QmlDelegate 1.0

/*
Ordinary dialog with content.
*/
Item {

	DialogDelegate {
		id: dialogDelegate
		objectName: "dialogDelegate"
	}
	
	Dialog {
		     id: dialog
		     
		     // Usually hidden unless call open()
		     // visible: true
		     
		     contentItem: Rectangle {
		        color: "lightskyblue"
		        implicitWidth: 400
		        implicitHeight: 100
		        Text {
		            text: "Hello blue sky!"
		            color: "navy"
		            anchors.centerIn: parent
		        }
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