import QtQuick 2.2
import QtQuick.Controls 1.2

// Actions

    Action {
        id: fileAction
        text: "&File"
    }
    


    MenuBar {
        Menu {
            title: "&Choosers"
            MenuItem { action: fileAction }
        }
    }