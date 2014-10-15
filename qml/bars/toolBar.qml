import QtQuick 2.2
import QtQuick.Controls 1.2

// Actions

    Action {
        id: fileAction
        text: "&File"
    }
    


// This doesn't work, syntax error: a menubar can only be used in an ApplicationWindow


ToolBar {
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