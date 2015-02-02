import QtQuick 2.3
import QtQuick.Controls 1.2


/*
This causes syntax error later?
    Action {
        id: fileAction
        text: "&File"
    }
*/
    

// Does it need to be enclosed in Item?
Item {
MenuBar {
	Menu {
		title: "&Choosers"
		// MenuItem { action: fileAction }
		MenuItem { text: "foo" }
	}
}
}
