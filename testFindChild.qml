import QtQuick 2.2
import QtQuick.Controls 1.2

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