/*
Test a model with nested properties can be accessed from QML via qualification (dot notation) syntax.
*/

import QtQuick 2.4
import QtQuick.Controls 1.3


import Clan 1.0


ApplicationWindow {
	id: root
	objectName: "root"
    visible: true
    title: "Test "

    width: 640
    height: 420
    minimumHeight: 400
    minimumWidth: 600

    Clan {
        id: clan
    }

    Button {
        id: button
        objectName: "button"
        text: "Test"
        
 		onClicked: {
        	console.log("button clicked")
 			console.log("clan.person:", clan.person)
			console.log("clan.person.name:",clan.person.name)
 			
 		}
    }
}