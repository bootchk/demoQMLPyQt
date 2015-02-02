
from PyQt5.QtCore import pyqtProperty, QObject
from PyQt5.QtCore import pyqtSlot as Slot
from PyQt5.QtCore import pyqtSignal as Signal

'''
A type that will be registered with QML.  
Must be a sub-class of QObject.

Largely from example in PyQt documentation.
'''
class Person(QObject):
  
    personChanged = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._name = 'BillyDefault'
        self._shoeSize = 0

    # Define the getter of the 'name' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString')
    def name(self):
        return self._name

    # Define the setter of the 'name' property.
    @name.setter
    def name(self, name):
        self._name = name

    # Define the getter of the 'shoeSize' property.  The C++ type and
    # Python type of the property is int.
    @pyqtProperty(int)
    def shoeSize(self):
        return self._shoeSize

    # Define the setter of the 'shoeSize' property.
    @shoeSize.setter
    def shoeSize(self, shoeSize):
        self._shoeSize = shoeSize
    
    " Must be slot to be callable/invokeable from QML JS"
    @Slot()
    def activate(self):
      '''
      Handle activated signal.
      
      Note connections (for instances) can be made from QML or from Python?
      '''
      print("Person.activate slot called")
      print("Emitting personChanged")
      self.personChanged.emit()
      
      
"""
Cruft from original example code in PyQt docs.
Here the component is created from the Python side.
I chose instead to create the component in the qml file.

from PyQt5.QtCore import QCoreApplication, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine


def main2():
  # Create the application instance.
  app = QCoreApplication(sys.argv)
  
  # Register the Python type.  Its URI is 'People', it's v1.0 and the type
  # will be called 'Person' in QML.
  qmlRegisterType(Person, 'People', 1, 0, 'Person')
  
  # Create a QML engine.
  engine = QQmlEngine()
  
  # Create a component factory and load the QML script.
  component = QQmlComponent(engine)
  component.loadUrl(QUrl('example.qml'))
  
  # Create an instance of the component.
  person = component.create()
  
  if person is not None:
      # Print the value of the properties.
      print("The person's name is %s." % person.name)
      print("They wear a size %d shoe." % person.shoeSize)
  else:
      # Print all errors that occurred.
      for error in component.errors():
          print(error.toString())
"""