import QtQuick 2.4
import QtQuick.Controls 1.3

import People 1.0

Row {
	Label {
		id: label
		text: "foofoofoofoofoo"
	}
	// Demonstrate model owned by control.
	// Simpler than putting model outside control (which requires using Connection.)
	SpinBox {
		id: spinbox
		
		// Model is a property
		property QtObject model: Person{}
		
		// Usual signal on SpinBox.value property changed.
		onValueChanged: {
			print("SpinBox.value changed")
			/*
			Futz with object owned by business logic and exposed to this QML via contextObject
			Its another instance of Person, name is applicationData.
			This is reverse of above instance of Person which is owned by the QML and exposed to the business logic.
			*/
			applicationData.activate()
			}
		
		// special signal on SpinBox lose focus
		onEditingFinished: {
			print("SpinBox.editingFinished")
			model.activate()	// Relay to business logic
		}
		
		// This executed if business logic changes model value.
		// The view should change to reflect new value
		onModelChanged: print("Model changed by business logic")
	}
	Button {
		id: button
		text: "Reset"
		onClicked: print("button clicked")
	}
}