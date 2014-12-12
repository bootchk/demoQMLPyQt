#! /usr/local/bin/python3

'''
Drawn from examples:
- PyQt 5.3.2 Reference Quide "Integrating Python and QML"
- PySide wiki
- Qt gallery example
- Qt QML reference guide
-- "Interacting with QML Objects from C++"
'''

from qmlApp.qmlApp import QmlApp
from widgetApp.widgetApp import WidgetApp


'''
Pure QML apps (invokes QmlApp)

Create and init app enters event loop, doesn't return
'''
'''
Cruft
# "person.qml"
# "qrc:/resources/helloWorld.qml"
# qrc:/weatherapp/qml/main.qml"))

# Qt's gallery exampe
# Half working, imports a contents dir of qml? Much commented out
# app = QmlApp(qml="qml/gallery/gallery.qml")
'''

'''
These seem to work.
Uncomment one to test.
'''
#app = QmlApp(qml="qml/pureQMLApps/helloWorld.qml")
#app = QmlApp(qml="qml/pureQMLApps/testDialogs.qml")
#app = QmlApp(qml="qml/pureQMLApps/testViews.qml")
#app = QmlApp(qml="qml/pureQMLApps/testBars.qml")
app = QmlApp(qml="qml/pureQMLApps/testMenu.qml")
#app = QmlApp(qml="qml/pureQMLApps/testComboBox.qml")


" Test signals from QML to Python slot"
#app = QmlApp(qml="qml/pureQMLApps/testSignals.qml")
" Test signal from Python to QML"
#app = QmlApp(qml="qml/pureQMLApps/testSignalsUp.qml")
" Test model with nested properties accessible in QML"
#app = QmlApp(qml="qml/pureQMLApps/testNestedProperties.qml")
" Test model returning a type via a method"
#app = QmlApp(qml="qml/pureQMLApps/testModelSlot.qml")


'''
QWidget app embedding QML
'''

# menuBar does NOT seem to work
#app = WidgetApp(embeddedQml="qml/bars/menuBar.qml")

# This doesn't work: 'QQuickView only supports loading of root objects that derive from QQuickItem.'
#app = WidgetApp(embeddedQml="qml/helloWorld.qml")

"These work"

# Popup menu
#app = WidgetApp(embeddedQml="qml/menu.qml")

# dialog not working?
#app = WidgetApp(embeddedQml="qml/dialogs/fontDialog.qml")

# Toolbar works.  toolbar are NOT exclusive to ApplicationWindow?
#app = WidgetApp(embeddedQml="qml/bars/toolBar.qml")

# Toolbar, context menu, and dialog
#app = WidgetApp(embeddedQml="qml/bars/toolBar.qml", secondEmbeddedQml="qml/embeddedQML/MenuAndDialog.qml")
#"qml/embeddedQML/PickMenu.qml"
#"qml/dialogs/dialog.qml"

# Dialog with controls.  Slider owning model
#app = WidgetApp(embeddedQml="qml/bars/toolBar.qml", secondEmbeddedQml="qml/embeddedQML/DialogWControls.qml")

# Dialog with calendar
#app = WidgetApp(embeddedQml="qml/bars/toolBar.qml", secondEmbeddedQml="qml/embeddedQML/DialogWCalendar.qml")

# Dialog implemented using Window with Qt.Dialog flag
#app = WidgetApp(embeddedQml="qml/bars/toolBar.qml", secondEmbeddedQml="qml/embeddedQML/WindowAsDialog.qml")


# Test toolbar and popupmenu 
#app = WidgetApp(embeddedQml="qml/bars/toolBar.qml")


# Not work? QmlApp requires a QWindow, which this does not have
#app = QmlApp(qml="qml/pureQMLApps/helloWorldRedRect.qml")


  
