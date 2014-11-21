'''
App whose outer is QWidget, having embedded QML
'''
import sys


from PyQt5.QtWidgets import QApplication, QVBoxLayout
#from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QWidget

from widgetApp.graphicsView import MyGraphicsView

from qmlApp.qmlModel import QmlModel
from qmlMaster.qmlMaster import QmlMaster


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
    
    " mainWindow has layout has widget has quickview"
    layout = QVBoxLayout()
    
    '''
    Embed QML to main window.
    Typically a toolbar or dialog
    '''
    layout.addWidget(qmlMaster.widgetForQML(qmlFilename=embeddedQml))
    
    '''
    ??? No need for this.  Has strange effects.
    '''
    #quickThingContainer.show()
    #quickThing.show()
    
    if secondEmbeddedQml is not None:
      '''
      Create QQuickView to pass to GV.
      Typically contains menu or dialog that GV will present on certain events
      (keypress for dialog, mouseclick for menu.)
      '''
      myView = qmlMaster.quickViewForQML(qmlFilename=secondEmbeddedQml)
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


  
  
  