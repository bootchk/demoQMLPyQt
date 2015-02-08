import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.0


/*
Component
A QML Window acting as a dialog.
I.E. an alternate implementation of QML Dialog, which is buggy.
*/
Window {
		id: dialog
		flags: Qt.Dialog
		modality: Qt.WindowModal
		
		title: "Custom dialog implementation"
		
		Button {
			text: "OK"
			onClicked: {
				dialog.close()
			}
		}
		
		function open() {
			show()
		}
	}