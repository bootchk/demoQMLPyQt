
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import qWarning, QObject
from PyQt5.QtQuick import QQuickItem

#from model.person import Person
import model

class MyGraphicsView(QGraphicsView):
  '''
  GV with GS having an item.
  When mouse pressed, emit signal to open QML context menu (mocking a pick of an item.)
  '''
  
  def __init__(self, pickerView):
    scene = QGraphicsScene()
    scene.addText("foo")
    QGraphicsView.__init__(self, scene)
    
    '''
    See the QML, created there?
    
    " A Person model which is mock-picked"
    self.model = Person()
    '''
    self.pickerView = pickerView
    " Find the picker"
    self.picker = self.findPicker()

  
    
    
  def mousePressEvent(self, event):
    self.picker.doActivated()  # cause signal to be emitted to QML
    print("pressed")
    
    
  def findPicker(self):
    try:
      qmlRoot = self.pickerView.rootObject()  # objects()[0]
    except:
      qWarning("Failed to read or parse qml.")
      raise
    
    print(qmlRoot)
    assert isinstance(qmlRoot, QQuickItem)
    
    result = self.findComponent(qmlRoot)
    
    '''
    self.dumpQMLComponents(qmlRoot)
    
    #result = qmlRoot.findChild(Person, "person")
    result = qmlRoot.findChild(model.person.Person, "person")
    '''
    assert result is not None
    return result
    
  
  def dumpQMLComponents(self, root):
    children = root.findChildren(QObject)
    for item in children:
      # Note the QML id property is NOT the objectName
      print(item, "name is:", item.objectName())
      if isinstance(item, model.person.Person):
        print("Is Person")
        
  def findComponent(self, root):
    result = None
    children = root.findChildren(QObject)
    for item in children:
      # Note the QML id property is NOT the objectName
      if isinstance(item, model.person.Person) and item.objectName()=="person":
        print("Found Person", item.objectName())
        result = item
        break
    return result
    