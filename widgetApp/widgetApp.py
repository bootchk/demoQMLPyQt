'''
App whose outer is QWidget, having embedded QML
'''
import sys

from PyQt5.QtCore import QUrl # QObject, 
#from PyQt5.QtCore import qWarning
from PyQt5.QtWidgets import QApplication, QVBoxLayout

#from PyQt5.QtGui import QGuiApplication

from PyQt5.QtWidgets import QWidget
from PyQt5.QtQuick import QQuickView


from widgetApp.graphicsView import MyGraphicsView

from qmlApp.qmlModel import QmlModel


class WidgetApp(object):
  def __init__(self, qml):
    app = QApplication(sys.argv)
    
    '''
    Register our Python model (classes/types to be registered with QML.)
    '''
    model = QmlModel()
    model.register()
    
    contextMenuView = QQuickView(self.qmlFilenameToQUrl("qml/PickMenu.qml"))
    
    " simple widget, not QMainWindow"
    mainWindow = QWidget()
    mainWindow.setGeometry(100, 100, 500, 400)
    mainWindow.show()
    
    " mainWindow has layout has widget has quickview"
    layout = QVBoxLayout()
    
    " Add QML toolbar to main window."
    quickThing = QQuickView(self.qmlFilenameToQUrl(qml))
    quickThingContainer = QWidget.createWindowContainer(quickThing)
    layout.addWidget(quickThingContainer)
    
    " Add QGV to main window"
    gv = MyGraphicsView(pickerView=contextMenuView)
    layout.addWidget(gv)
    
    mainWindow.setLayout(layout)

    
    
    " Connections are defined inside the QML"

    # Qt Main loop
    sys.exit(app.exec_())


  def qmlFilenameToQUrl(self,qml):
      qmlUrl=QUrl(qml)
      assert qmlUrl.isValid()
      print(qmlUrl.path())
      #assert qmlUrl.isLocalFile()
      return qmlUrl
  
  