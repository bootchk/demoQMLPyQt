
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene



from demoPyQtQML.qmlMaster.qmlMaster import QmlMaster
#from model.person import Person
import demoPyQtQML.model as model


class MyGraphicsView(QGraphicsView):
  '''
  GV with GS having an item.
  When mouse pressed, emit signal to open QML context menu (mocking a pick of an item.)
  '''
  
  def __init__(self, pickerView):
    scene = QGraphicsScene()
    scene.addText("QGraphicsItem in QGraphicsView.  Press mouse to mock pick, key to open dialog.")
    QGraphicsView.__init__(self, scene)
    
    # Accept touch on both this widget and viewport (abstract scroll area)
    # Touch engenders LMB mouse press event since app attribute for that is set.
    self.setAttribute(Qt.WA_AcceptTouchEvents)
    self.viewport().setAttribute(Qt.WA_AcceptTouchEvents)
    
    self.qmlMaster = QmlMaster()
    
    '''
    See the QML, created there?
    
    " A Person model which is mock-picked"
    self.model = Person()
    '''
    if pickerView is not None:
      self.pickerView = pickerView
      
      self.pickDelegate = self.qmlMaster.findComponent(self.pickerView, 
                                                       className=model.person.Person, 
                                                       objectName="person")
      
      self.dialogDelegate = self.qmlMaster.findComponent(self.pickerView, 
                                                         className=model.qmlDelegate.QmlDelegate, 
                                                         objectName="dialogDelegate")
    else:
      self.pickDelegate = None
      self.dialogDelegate = None
    #self.findQMLControl()

    
  def touchEvent(self, event):
    print("Touch event")
    
    
  def mousePressEvent(self, event):
    '''
    Treat any mousePressEvent as a mock pick of the QGraphicsItem.
    '''
    if self.pickDelegate is not None:
      self.pickDelegate.activate()  # cause signal to be emitted to QML
    print("Mouse pressed")
    
    
  def keyPressEvent(self, event):
    '''
    Any key opens dialog.
    '''
    print("Key pressed")
    if self.dialogDelegate is not None:
      self.dialogDelegate.activate()
    
    
  
    
  
  
        
        
  
    