import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Dialogs 1.2

import "../views" as MyViews


Dialog {
     id: dialog
     
     // Usually hidden unless call open()
     // visible: true
     // Not a property: anchors.centerIn: parent
     // Not a property: flags: Qt.Dialog
     title: "My dialog"
	 standardButtons: StandardButton.Ok | StandardButton.Cancel
	 
	 //MyViews.StackView {
	 //	id: stackview
	 //}
	 
	 MyViews.TabView {
	 	id: tabview
	 }
}