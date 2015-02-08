import QtQuick 2.4
import QtQuick.Controls 1.3

ApplicationWindow {
  id: root
  visible: true
  height: 700
  width: 1200
  title: "test combobox currentIndex"
  
  ComboBox{
	  model: ["foo", "bar"]
	  onActivated: {
		 console.debug("CombBox.onActivated", index)		
		console.assert(currentIndex == index, "Assertion failed: property currentIndex not equal to actual parameter index")
		// Note index is actual parameter of signal, not same as currentIndex
	  }
  }
}