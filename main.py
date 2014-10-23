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
#app = QmlApp(qml="qml/helloWorld.qml")
#app = QmlApp(qml="qml/testDialogs.qml")
#app = QmlApp(qml="qml/testViews.qml")
#app = QmlApp(qml="qml/testBars.qml")
#app = QmlApp(qml="qml/testMenu.qml")


" Test signals from QML to Python slot"
#app = QmlApp(qml="qml/testSignals.qml")
" Test signal from Python to QML"
#app = QmlApp(qml="qml/testSignalsUp.qml")





'''
QWidget app embedding QML
'''


# menuBar does NOT seem to work
#app = WidgetApp(qml="qml/bars/menuBar.qml")

# This doesn't work: 'QQuickView only supports loading of root objects that derive from QQuickItem.'
#app = WidgetApp(qml="qml/helloWorld.qml")

"These work"

# Popup menu
#app = WidgetApp(qml="qml/menu.qml")

#app = WidgetApp(qml="qml/dialogs/fontDialog.qml")

# Toolbar works.  toolbar are NOT exclusive to ApplicationWindow?
#app = WidgetApp(qml="qml/bars/toolBar.qml")


# Test toolbar and popupmenu 
app = WidgetApp(qml="qml/bars/toolBar.qml")


# Not work? No window or window not show()?
# app = QmlApp(qml="qml/helloWorldRedRect.qml")


  
