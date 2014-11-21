
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene



from qmlMaster.qmlMaster import QmlMaster
#from model.person import Person
import model


class MyGraphicsView(QGraphicsView):
  '''
  GV with GS having an item.
  When mouse pressed, emit signal to open QML context menu (mocking a pick of an item.)
  '''
  
  def __init__(self, pickerView):
    scene = QGraphicsScene()
    scene.addText("QGraphicsItem to be mock picked.")
    QGraphicsView.__init__(self, scene)
    self.qmlMaster = QmlMaster()
    
    '''
    See the QML, created there?
    
    " A Person model which is mock-picked"
    self.model = Person()
    '''
    if pickerView is not None:
      self.pickerView = pickerView
      #self.dialogView = dialogView
      
      #self.pickDelegate = self.findPickDelegate()
      self.pickDelegate = self.qmlMaster.findComponent(self.pickerView, className=model.person.Person, objectName="person")
      
      #self.dialogDelegate = self.qmlMaster.findComponent(self.dialogView, className=model.qmlDelegate.QmlDelegate, objectName="dialogDelegate")
      self.dialogDelegate = self.qmlMaster.findComponent(self.pickerView, className=model.qmlDelegate.QmlDelegate, objectName="dialogDelegate")
    else:
      self.pickDelegate = None
      self.dialogDelegate = None
    #self.findQMLControl()

    
    
  def mousePressEvent(self, event):
    '''
    Treat any mousePressEvent as a mock pick of the QGraphicsItem.
    '''
    if self.pickDelegate is not None:
      self.pickDelegate.doActivated()  # cause signal to be emitted to QML
    print("pressed")
    
    
  def keyPressEvent(self, event):
    '''
    Any key opens dialog.
    '''
    print("Key pressed")
    if self.dialogDelegate is not None:
      self.dialogDelegate.activate()
    
    
  def findPickDelegate(self):
    '''
    Find the model component of self's view.
    The model is a delegate.  When it's doActivated() method is called, it delegates
    to a QML control (menu or other dialog.)
    ??? Why can't we just call the method on the QML control.
    '''
    result = self.qmlMaster.findComponent(self.pickerView, className=model.person.Person, objectName="person")
    assert result is not None
    return result
    
  
    
  
  
        
        
  
    