// QML bars

import QtQuick 2.4
import QtQuick.Controls 1.3

// Need layouts for toolbar
import QtQuick.Layouts 1.1


ApplicationWindow {
    visible: true
    title: "Test "

    width: 640
    height: 420
    minimumHeight: 400
    minimumWidth: 600

    

    // Actions
    Action {
        id: fileAction
        text: "&File"
        shortcut: StandardKey.Open
        tooltip: "Choose file"
        onTriggered: console.log("triggered")
    }
    


    menuBar: MenuBar {
        Menu {
            title: "&Choosers"
            MenuItem { action: fileAction }
        }
    }
    
    toolBar: ToolBar {
        id: toolbar
        RowLayout {
            id: toolbarLayout
            spacing: 0
            width: parent.width
            ToolButton { action: fileAction }
            Item { Layout.fillWidth: true }
            CheckBox {
                id: enabledCheck
                text: "Enabled"
                checked: true
            }
        }
    }
    
    statusBar: StatusBar {
        RowLayout {
            Button { action: fileAction }
            ToolButton { action: fileAction }
            Label { text: "Read Only" }
        }
    }
    
    
}