// QML bars

import QtQuick 2.2
import QtQuick.Controls 1.2

// Need layouts for toolbar
import QtQuick.Layouts 1.0


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