import QtQuick 2.4
// import built-in non-basic types, i.e. ApplicationWindow
import QtQuick.Controls 1.3


// Built-in Qt Quick control
ApplicationWindow {
  id: root
  visible: true
  height: 700
  width: 1200
  title: "Hello World"
  
  Label {
	  text: "Assert title is 'Hello World' and no controls except window controls."
  }
}