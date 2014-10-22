import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1


// Syntax error if Actions defined ahead of this?


ToolBar {
        id: toolbar
        RowLayout {
            id: toolbarLayout
            spacing: 0
            width: parent.width
            // ToolButton { action: fileAction }
            Item { Layout.fillWidth: true }
            CheckBox {
                id: enabledCheck
                text: "Enabled"
                checked: true
            }
        }
    }
