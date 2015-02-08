import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1

import QmlDelegate 1.0	// DialogDelegate

// Syntax error if Actions defined ahead of this?

// A toolbar with button and checkbox

ToolBar {
	id: toolbar
	objectName: "toolbar"
	
	// delegate that business side knows (by finding it.)
	DialogDelegate {
		id: dialogDelegate
		objectName: "dialogDelegate"
	}
	
	Action {
	        id: fileAction
	        text: "&File"
	        shortcut: StandardKey.Open
	        tooltip: "Choose file"
	        onTriggered: {
	        	console.log("triggered")
	        	// make delegate emit signal 'activated'.  Business side can connect to it.
	        	dialogDelegate.activate()
	        }
	    }
	
	RowLayout {
		spacing: 0
		width: parent.width
		
		ToolButton { action: fileAction }
		
		Item { Layout.fillWidth: true }
		
		CheckBox {
			id: enabledCheck
			text: "Enabled"
			checked: true
		}
	}
}
