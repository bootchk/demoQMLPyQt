'''
App whose outer is QWidget, having embedded QML
'''
import sys


from PyQt5.QtWidgets import QApplication, QVBoxLayout
#from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QWidget

from demoPyQtQML.widgetApp.graphicsView import MyGraphicsView

from demoPyQtQML.qmlApp.qmlModel import QmlModel
from demoPyQtQML.qmlMaster.qmlMaster import QmlMaster

from demoPyQtQML.model.person import Person


class WidgetApp(object):
  def __init__(self, embeddedQml, secondEmbeddedQml=None):
    app = QApplication(sys.argv)
    
    '''
    Register our Python model (classes/types to be registered with QML.)
    '''
    model = QmlModel()
    model.register()
    
    qmlMaster = QmlMaster()
    
    " simple widget, not QMainWindow"
    mainWindow = QWidget()
    mainWindow.setGeometry(100, 100, 500, 400)
    mainWindow.show()
    
    mainQWindow = qmlMaster.appQWindow()
    
    " mainWindow has layout has widget has quickview"
    layout = QVBoxLayout()
    
    '''
    Embed QML to main window.
    Typically a toolbar or dialog
    '''
    widget = qmlMaster.widgetForQML(qmlFilename=embeddedQml, parentWindow=mainWindow)
    layout.addWidget(widget)
    
    '''
    No need to show() the quickview or the container QWidget.  Has strange effects.
    '''
    
    if secondEmbeddedQml is not None:
      '''
      Create QQuickView to pass to GV.
      Typically contains menu or dialog that GV will present on certain events
      (keypress for dialog, mouseclick for menu.)
      
      Note here quickview is NOT contained.  Experimental.
      '''
      myView = qmlMaster.quickViewForQML(qmlFilename=secondEmbeddedQml, transientParent=mainQWindow)
      # container = QWidget.createWindowContainer(myView)
      '''
      Expose our model to QML.
      This instance of Person is owned here, but visible in QML.
      '''
      data = Person()
      myView.rootContext().setContextProperty("applicationData", data)
    else:
      myView = None
      
    " Add QGV to main window"
    #gv = MyGraphicsView(pickerView=contextMenuView, dialogView=dialogView)
    gv = MyGraphicsView(pickerView=myView)
    layout.addWidget(gv)
    mainWindow.setLayout(layout)

    " Connections are defined inside the QML"

    # Qt Main loop
    sys.exit(app.exec_())


  
  
  