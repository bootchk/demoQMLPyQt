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

# ??? button.activated.connect(person.onActivated)

" Test signals from QML to Python slot"
#app = QmlApp(qml="qml/testSignals.qml")
" Test signal from Python to QML"
#app = QmlApp(qml="qml/testSignalsUp.qml")

# popup context menu from QML app
#app = QmlApp(qml="qml/testMenu.qml")



'''
QWidget app embedding QML
'''
# Toolbar works.  toolbar are NOT exclusive to ApplicationWindow?
#app = WidgetApp(qml="qml/bars/toolBar.qml")

# menuBar does NOT seem to work
app = WidgetApp(qml="qml/bars/menuBar.qml")

# This doesn't work: 'QQuickView only supports loading of root objects that derive from QQuickItem.'
#app = WidgetApp(qml="qml/helloWorld.qml")

"These work"

# Popup menu from a QWidget app
#app = WidgetApp(qml="qml/menu.qml")
#app = WidgetApp(qml="qml/dialogs/fontDialog.qml")



# Not work? No window or window not show()?
# app = QmlApp(qml="qml/helloWorldRedRect.qml")


  
