import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2

/*
Must be nested in Item if it is to be embedded in QWidget.
FontDialog does not derive from QQuickItem, and only QQuickItem's can be rooted in a QWidget.
*/
Item {

	FontDialog {
	     id: fontDialog
	     
	     // Usually hidden unless call open()
	     visible: true
	}
}