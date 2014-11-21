import QtQuick 2.3
import QtQuick.Controls 1.2


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