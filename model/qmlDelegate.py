
from PyQt5.QtCore import pyqtProperty, QObject
from PyQt5.QtCore import pyqtSlot as Slot
from PyQt5.QtCore import pyqtSignal as Signal

'''
A type that will be registered with QML.  
Must be a sub-class of QObject.
'''
class QmlDelegate(QObject):
  
    activated = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        # self._name = ''
        
    # Define the getter of the 'name' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString')
    def name(self):
        return self._name

    # Define the setter of the 'name' property.
    @name.setter
    def name(self, name):
        self._name = name

    
    " Must be slot to be callable/invokeable from QML JS"
    @Slot()
    def activate(self):
      '''
      Slot called from:
      - business side (business knows dialog is needed)
      - OR QML (business has opened widget e.g. menu which chains to a dialog.)
      In turn, emit signal to be handled in QML.
      
      Note connections (for instances) can be made from QML or from Python?
      '''
      print(".activate slot called")
      print("Emitting activated")
      self.activated.emit()
      
    