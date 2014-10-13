// QML dialogs

import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2


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


    menuBar: MenuBar {
        Menu {
            title: "&Choosers"
            MenuItem { action: fileAction }
            MenuItem { action: colorAction }
            MenuItem { action: fontAction }
            MenuItem { action: messageAction }
        }
    }
}