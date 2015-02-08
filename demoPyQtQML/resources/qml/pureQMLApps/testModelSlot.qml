/*
Test a model having slot get(str) returning type Person.
*/

import QtQuick 2.4
import QtQuick.Controls 1.3

import People 1.0
import SlottedModel 1.0


ApplicationWindow {
	id: root
	objectName: "root"
    visible: true
    title: "Test "

    width: 640
    height: 420
    minimumHeight: 400
    minimumWidth: 600

    SlottedModel {
        id: slottedModel
    }

    Button {
        id: button
        objectName: "button"
        text: "Test"
        property Person submodel
        
 		onClicked: {
        	console.log("button clicked")
            submodel = slottedModel.get('foo')
 			console.log("slottedModel.get('foo'):", submodel)
			console.log("submodel.name:", submodel.name)
 			
 		}
    }
}