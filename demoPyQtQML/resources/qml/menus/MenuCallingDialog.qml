/*
A context menu that opens another dialog using a delegate.
*/

import QtQuick 2.4
import QtQuick.Controls 1.3


	
Menu {
	id: menu
    title: "Context Menu"
    
    MenuItem { 
    	text: "Show dialog"
    	onTriggered: {
    		print("menu item triggered")
    		
		    /*
    		// call slot to show another dialog via signal
    		print("activating dialog by calling method of delegate")
    		dialogDelegate.activate()
    		*/
    				
    		// Alternatively, open the dialog directly
    		print("direct call to dialog.open()")
    		dialog.open()
    	}
    }
    MenuItem { text: "foo" }
}
	
