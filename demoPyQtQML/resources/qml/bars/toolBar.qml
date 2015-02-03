import QtQuick 2.2
import QtQuick.Controls 1.2
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
