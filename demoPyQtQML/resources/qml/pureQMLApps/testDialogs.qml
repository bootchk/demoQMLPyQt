// Test Quick Dialogs
// See QTBUG 41844
// Also test a custom dialog implementation

import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Dialogs 1.2

import "../dialogs" as MyDialogs

ApplicationWindow {
    visible: true
    title: "Test "

    width: 640
    height: 420
    minimumHeight: 400
    minimumWidth: 600

    FileDialog {
        id: fileDialog
        nameFilters: [ "Image files (*.png *.jpg)" ]
        onAccepted: imageViewer.open(fileUrl)
    }
    
    ColorDialog {
        id: colorDialog
    }
    
    FontDialog {
        id: fontDialog
    }
    
    MessageDialog {
        id: messageDialog
        text: "Message"
    }
    
    Dialog {
		id: plainDialog
		title: "Plain dialog"
	}
    
    // Not a QML Dialog but a QML Window configured as a dialog.
    MyDialogs.WindowAsDialog{
    	id: customDialog
    }
    

    // Actions displaying dialogs
    Action {
        id: fileAction
        text: "&File"
        shortcut: StandardKey.Open
        onTriggered: fileDialog.open()
        tooltip: "Choose file"
    }
    
    Action {
        id: colorAction
        text: "&Color"
        onTriggered: colorDialog.open()
        tooltip: "Choose color"
    }
    
    Action {
        id: fontAction
        text: "&Font"
        onTriggered: fontDialog.open()
        tooltip: "Choose font"
    }
    
    Action {
        id: messageAction
        text: "&Message"
        onTriggered: messageDialog.open()
        tooltip: "Message"
    }
    
    Action {
            id: plainAction
            text: "&Plain Dialog"
            onTriggered: plainDialog.open()
            tooltip: "Plain"
        }
    
    Action {
                id: customAction
                text: "&Custom Dialog"
                onTriggered: customDialog.open()
                tooltip: "Custom"
            }

    // !!! Must assign to the property 'menubar'
    menuBar: MenuBar {
        Menu {
            title: "&Test dialog"
            MenuItem { action: fileAction }
            MenuItem { action: colorAction }
            MenuItem { action: fontAction }
            MenuItem { action: messageAction }
            MenuItem { action: plainAction }
            MenuItem { action: customAction }
        }
    }
    
    Label {
    	text: "Expect menubar having 'Test dialog' item"
    }
}