import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1


// Syntax error if Actions defined ahead of this?

// A simple toolbar with one checkbox

ToolBar {
        id: toolbar
        objectName: "toolbar"
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
