
" Example apps use one of these alternatives "
from demoPyQtQML.qmlApp.qmlApp import QmlApp  # outer app is QML
from demoPyQtQML.widgetApp.widgetApp import WidgetApp # outer app is Qwidget with embedded QML



def createApp():
  '''
  Create a demo app.
  Uncomment one.
  '''
  #result = createPureQMLApp()
  result = createEmbeddedQMLApp()
  return result
  
  
def createPureQMLApp():
  '''
  Pure QML apps (invokes QmlApp)
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
  '''
  Not working OSX in Python in terminal because app menubar hidden?
  '''
  #app = QmlApp(qml="pureQMLApps/testDialogs.qml")
  #app = QmlApp(qml="pureQMLApps/testViews.qml")
  app = QmlApp(qml="pureQMLApps/testBars.qml")
  #app = QmlApp(qml="pureQMLApps/testMenu.qml")
  #app = QmlApp(qml="pureQMLApps/testComboBox.qml")
  
  
  " Test signals from QML to Python slot"
  #app = QmlApp(qml="pureQMLApps/testSignals.qml")
  " Test signal from Python to QML"
  #app = QmlApp(qml="pureQMLApps/testSignalsUp.qml")
  " Test model with nested properties accessible in QML"
  #app = QmlApp(qml="pureQMLApps/testNestedProperties.qml")
  " Test model returning a type via a method"
  #app = QmlApp(qml="pureQMLApps/testModelSlot.qml")
  return app
  
  
def createEmbeddedQMLApp():
  '''
  QWidget app embedding QML
  '''
  
  '''
  menuBar does NOT seem to work?
  QWidget layout is not handling it properly so it is obscured by it's sibling QGV?
  '''
  #app = WidgetApp(embeddedQml="bars/menuBar.qml")
  
  # This doesn't work: 'QQuickView only supports loading of root objects that derive from QQuickItem.'
  #app = WidgetApp(embeddedQml="helloWorld.qml")
  
  "These work"
  
  # Popup menu
  #app = WidgetApp(embeddedQml="menu.qml")
  
  # dialog not working?
  #app = WidgetApp(embeddedQml="dialogs/fontDialog.qml")
  
  # Toolbar works.  toolbar are NOT exclusive to ApplicationWindow?
  #app = WidgetApp(embeddedQml="bars/toolBar.qml")
  
  # Toolbar having button opening a dialog
  app = WidgetApp(embeddedQml="bars/toolBarWButton.qml", secondEmbeddedQml="embeddedQML/MenuAndDialog.qml")
  
  '''
  Test round trip to modal context menu:
  mouse press in QGV invokes QML context menu which invokes QML dialog
  '''
  # Toolbar, context menu, and dialog
  #app = WidgetApp(embeddedQml="bars/toolBar.qml", secondEmbeddedQml="embeddedQML/MenuAndDialog.qml")
  #"embeddedQML/PickMenu.qml"
  #"dialogs/dialog.qml"
  
  # Menu with delegate.  Doesn't work unless Menu embedded in Item
  #app = WidgetApp(embeddedQml="bars/toolBar.qml", secondEmbeddedQml="embeddedQML/MenuWDelegate.qml")
  
  # Dialog with controls.  Slider owning model
  # Works Linux, OSX
  #app = WidgetApp(embeddedQml="bars/toolBar.qml", secondEmbeddedQml="embeddedQML/DialogWControls.qml")
  
  # Dialog with calendar
  #app = WidgetApp(embeddedQml="bars/toolBar.qml", secondEmbeddedQml="embeddedQML/DialogWCalendar.qml")
  
  # Dialog implemented using Window with Qt.Dialog flag
  #app = WidgetApp(embeddedQml="bars/toolBar.qml", secondEmbeddedQml="embeddedQML/WindowAsDialog.qml")
  
  
  # Test toolbar
  #app = WidgetApp(embeddedQml="bars/toolBar.qml")
  
  # Menubar invoking dialogs
  #app = WidgetApp(embeddedQml="bars/menuBar.qml", secondEmbeddedQml="embeddedQML/DialogWControls.qml")
  
  # Not work? QmlApp requires a QWindow, which this does not have
  #app = QmlApp(qml="pureQMLApps/helloWorldRedRect.qml")
  return app

