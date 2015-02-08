// QML signals
// See "QML Object Attributes" 5.3
// Also: http://stackoverflow.com/questions/19131084/pyqt5-qml-signal-to-python-slot

import QtQuick 2.4
import QtQuick.Controls 1.3


import People 1.0


// Note you can't create a Person outside app window?

ApplicationWindow {
	id: root
	objectName: "root"
    visible: true
    title: "Test "

    width: 640
    height: 420
    minimumHeight: 400
    minimumWidth: 600

	

    Button {
        id: button
        objectName: "button"
        text: "Test"
        
        // Declare signal.  !!! Note there is no colon
        // NOT WORKING, maybe the emit is wrong
        signal activated
        
        // Receive built-in clicked signal and propagate by emiting activated signal
 		onClicked: {
 			// emit parent signal, equivalently using object id: 'button.activated'
 			// ??? who does signal belong to?
 			parent.activated	
 			console.log("button clicked, emit activated")
 			}
    }
    
    // Create a person component (class/type defined in Python.)
	// A signal handler (slot) doActivated is defined in class in Python.
    Person {
    	id: person
    	objectName: "person"
    	name: "Bob Jones"
    	shoeSize: 12
    	
    	/*
    	This works as well as the Connections below.
    	Note we are connecting multiple times same slot to same signal.
    	*/
    	// Connect a QML component to Python model
    	// This Person instance is not dynamic, but we only connect when completed? why?
   	    Component.onCompleted: {
   	      console.log("Person.onCompleted")
          // JS to connect signal-from-button to slot-in-person
	 	  button.clicked.connect(person.doActivated)
        }
	}
	
	/*
	Qt docs: "A Connections object creates a connection to a QML signal"
	The connection is NOT to a handler in another object, but to the handler defined in the body of the Connection element.
	I.E. in this example, onClicked: is the handler for the signal clicked.
	If we want the handler to call some other object, we can do so,
	but the Connection is intermediary.
	
	In general, the Connections element can be a child of any QML component.
	In other words, a Connections element simply puts a onClicked handler for the signal clicked
	within any component that cares to receive it.
	*/
	/*
	This works
	*/
	// Connecting other component's signals to this component
    Connections {
    	// id of control emitting signal
    	// control must exist (preceding this in the source file.)
	    target: button
	    // This doesn't work
	    /// onActivated: console.log("Person activated")
	    onClicked: {
	    	console.log("Person clicked")
	    	person.doActivated()	// call model slot
	    }	
	 }

	 
	 /*
	 Connections {
    	// id of control emitting signal
    	// control must exist (preceding this in the source file.)
	    target: button
	    // This doesn't work
	    onActivated: console.log("Person activated")
	 }
	 */
}