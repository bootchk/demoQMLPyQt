import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Dialogs 1.2

/*
 * This tests whether Dialog truly resizes to fit contents.
 * Apparently not see QTBUG 40134
 */

Dialog {
	id: dialog
	
	// Usually hidden unless call open()
	// visible: true
	// Not a property: anchors.centerIn: parent
	// Not a property: flags: Qt.Dialog
	title: "Choose a date"
	standardButtons: StandardButton.Ok | StandardButton.Cancel
	// Must set width, it is NOT automatically large enough to contain contents
	// Works
	//width: 400
	// Docs say NOT to do this, to bind width to size of content
	// Works, except off a little, omits margins
	//width: calendar.width
	
	Calendar {
		id: calendar
		onDoubleClicked: dateDialog.click(StandardButton.Save)
		// This doesn't help
		//implicitWidth: 400
	}
	
	// a custom contentItem will not have buttons
}