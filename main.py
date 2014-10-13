'''
Drawn from examples:
- PyQt 5.3.2 Reference Quide "Integrating Python and QML"
- PySide wiki
- Qt gallery example
- Qt QML reference guide
'''

from qmlApp.qmlApp import QmlApp

# "person.qml"
# "qrc:/resources/helloWorld.qml"
# qrc:/weatherapp/qml/main.qml"))

# Qt's gallery exampe
# Half working, imports a contents dir of qml? Much commented out
# app = QmlApp(qml="qml/gallery/gallery.qml") 

'''
These seem to work.
'''
# app = QmlApp(qml="qml/helloWorld.qml")
#app = QmlApp(qml="qml/testDialogs.qml")
app = QmlApp(qml="qml/testViews.qml")
#app = QmlApp(qml="qml/testBars.qml")

# Not work? No window or window not show()?
# app = QmlApp(qml="qml/helloWorldRedRect.qml")

# init app enters event loop, doesn't return
  
