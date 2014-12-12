/*
A context menu that opens another dialog using a delegate.
*/

import QtQuick 2.2
import QtQuick.Controls 1.2


	
Menu {
	id: menu
    title: "Context Menu"
    
    MenuItem { 
    	text: "Show dialog"
    	onTriggered: {
    		print("menu item triggered")
    		// call slot to show another dialog via signal
    		dialogDelegate.activate()
    	}
    }
    MenuItem { text: "foo" }
}
	
