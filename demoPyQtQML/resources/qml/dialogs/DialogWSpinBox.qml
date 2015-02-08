import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Dialogs 1.2

import "../controls" as MyControls


// Dialog having a spinbox

Dialog {
	id: dialog
	
	// Usually hidden unless call open()
	// visible: true
	// Not a property: anchors.centerIn: parent
	// Not a property: flags: Qt.Dialog
	title: "My dialog"
	standardButtons: StandardButton.Ok | StandardButton.Cancel
	
	Column {
		anchors.fill: parent
		anchors.margins: 10
	
		MyControls.LabeledSpinBoxWButton {
			id: rowControl
		}
		
		/*Calendar {
			id: calendar
			onDoubleClicked: dateDialog.click(StandardButton.Save)
		}
		*/
	}
	// a contentItem will not have buttons
}