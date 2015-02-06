
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout
#from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QWidget

from demoPyQtQML.widgetApp.graphicsView import MyGraphicsView

from demoPyQtQML.qmlApp.qmlModel import QmlModel
from demoPyQtQML.qmlMaster.qmlMaster import QmlMaster

from demoPyQtQML.model.person import Person
from demoPyQtQML.model.qmlDelegate import QmlDelegate


class WidgetApp(QApplication):
  '''
  App whose outer is QWidget i.e. QApplication, having embedded QML
  '''
  
  def __init__(self, embeddedQml, secondEmbeddedQml=None):
    super().__init__(sys.argv)
    
    print("On mobile platform, synthesizing LMB mouse events from touch.")
    self.setAttribute(Qt.AA_SynthesizeMouseForUnhandledTouchEvents, on=True)
      
    '''
    Register our Python model (classes/types to be registered with QML.)
    '''
    model = QmlModel()
    model.register()
    
    qmlMaster = QmlMaster()
    
    " simple widget, not QMainWindow"
    mainWindow = QWidget()
    self.mainWindow = mainWindow  # keep referenceid: toolbarLayout
    mainWindow.setGeometry(100, 100, 500, 400)
    mainWindow.show()
    
    mainQWindow = qmlMaster.appQWindow()
    
    " mainWindow has layout has widget has quickview"
    layout = QVBoxLayout()
    
    '''
    Embed QML to main window.
    Typically a toolbar or dialog
    '''
    ##widget = qmlMaster.widgetForQML(qmlFilename=embeddedQml, parentWindow=mainWindow)
    ##widget, quickthing = qmlMaster.widgetAndQuickViewForQML(qmlFilename=embeddedQml, parentWindow=mainWindow)
    widget, quickthing = qmlMaster.widgetForQMLUsingQQuickWidget(qmlFilename=embeddedQml, parentWindow=mainWindow)
    
    "No need to show() the quickview or the container QWidget?  Has strange effects."
    widget.show()
    print("Height of widget embedding QML:", widget.height())
    print("Widget embedding QML isVisible:", widget.isVisible())
    
    layout.addWidget(widget)
    
    " first embeddedQml might have a delegate"
    firstDelegate = qmlMaster.findComponent( quickthing,
                                             className=QmlDelegate, 
                                             objectName="dialogDelegate")
    print("Delegate in first qml:", firstDelegate)
    
    if secondEmbeddedQml is not None:
      myView = self._createSecondQuickView(qmlMaster, qmlFilename=secondEmbeddedQml, transientParent=mainQWindow)
    else:
      myView = None
    
    " Create QGV that on mouse down (a pick) opens another top level window embedding QML (pickerView) "
    gv = MyGraphicsView(pickerView=myView)
    layout.addWidget(gv)
    mainWindow.setLayout(layout)

    " Some connections are defined inside the QML"
    
    '''
    Connect optional delegate of first qml to delegate of second.
    
    Example: ToolButton in first qml onTriggered calls firstDelegate.activate() which emits signal
    which we here connect to secondDelegate.activate() which is connected in second qml to dialog.open().
    Thus, user push ToolButton opens a dialog.
    '''
    if firstDelegate is not None and gv.dialogDelegate is not None:
      firstDelegate.activated.connect(gv.dialogDelegate.activate)

    
    

  def _createSecondQuickView(self, qmlMaster, qmlFilename, transientParent ):
    '''
    Create QQuickView to pass to GV.
    Typically contains menu or dialog that GV will present on certain events
    (keypress for dialog, mouseclick for menu.)
    
    Note here quickview is NOT contained.  Experimental.
    '''
    myView = qmlMaster.quickViewForQML(qmlFilename=qmlFilename, transientParent=transientParent)
    # container = QWidget.createWindowContainer(myView)
    '''
    Expose our model to QML.
    This instance of Person is owned here, but visible in QML.
    '''
    data = Person()
    myView.rootContext().setContextProperty("applicationData", data)
    return myView
    
  
  
  