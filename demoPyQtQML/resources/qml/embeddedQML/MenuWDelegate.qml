/*
A context menu for person.

Opens by calling popup() from business side.

Menu item of context menu in turn calls dialogDelegate to do business.
*/

import QtQuick 2.4
import QtQuick.Controls 1.3

import QmlDelegate 1.0

Item {
Menu {
	
	Instantiator {
		DialogDelegate {
		
			id: dialogDelegate
			objectName: "dialogDelegate"
		}
	}
	
	MenuItem {
		text: "foo"
	}
}
}
