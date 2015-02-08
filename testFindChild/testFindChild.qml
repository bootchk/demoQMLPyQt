import QtQuick 2.4
import QtQuick.Controls 1.3

import People 1.0

Item {
	Person {
		id: person
		objectName: "person"
	}
	Menu {
		id: menu
		MenuItem {
			text: "foo"
		}
	}
}