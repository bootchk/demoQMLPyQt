import QtQuick 2.4
import QtQuick.Controls 1.3


StackView {
    	id: stack
    	initialItem: view

    	Component {
	        id: view
	
	        MouseArea {
	            Text {
	                text: stack.depth
	                anchors.centerIn: parent
	            }
	            onClicked: stack.push(view)
	        }
	    }
	    Component {
	        id: view2
	
	        MouseArea {
	            Text {
	                text: stack.depth
	                anchors.centerIn: parent
	            }
	            onClicked: stack.push(view)
	        }
	    }
	}