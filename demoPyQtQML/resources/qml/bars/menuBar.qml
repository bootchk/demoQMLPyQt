import QtQuick 2.4
import QtQuick.Controls 1.3

/*
This causes syntax error later?
    Action {
        id: fileAction
        text: "&File"
    }
*/
    
// QQuickView only supports loading of root objects derived from QQuickItem, thus enclose in Item
Item {
	MenuBar {
		Menu {
			title: "&Choosers"
			// MenuItem { action: fileAction }
			MenuItem { text: "foo" }
		}
		Menu {
			title: "B"
			MenuItem { text: "bar" }
		}
	}
}


// INCORRECT: Menubar IS a list, does not need a row layout?
/*
MenuBar {
	RowLayout {
		//spacing: 0
		width: parent.width
		// ToolButton { action: fileAction }
		Item { Layout.fillWidth: true }
		Menu {
			title: "&Choosers"
			// MenuItem { action: fileAction }
			MenuItem { text: "foo" }
		}
	}
}
*/