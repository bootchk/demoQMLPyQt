import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2


Dialog {
     id: dialog
     
     // Usually hidden unless call open()
     // visible: true
     // Not a property: anchors.centerIn: parent
     // Not a property: flags: Qt.Dialog
     title: "My dialog"
	 standardButtons: StandardButton.Ok | StandardButton.Cancel
	 
	 //Calendar {
	 //	id: calendar
	//	onDoubleClicked: dateDialog.click(StandardButton.Save)
	//	}
	
	Column {
		anchors.fill: parent
		anchors.margins: 10

		Row {
			Label {
				id: label
				text: "foo"
			}
			SpinBox {
				id: spinbox
			}
			Button {
				id: button
				text: "Reset"
			}
			
		}
	}
	// a contentItem will not have buttons
}