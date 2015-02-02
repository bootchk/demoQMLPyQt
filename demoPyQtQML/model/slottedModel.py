
from PyQt5.QtCore import QObject, pyqtSlot

from demoPyQtQML.model.person import Person

'''
A type that will be registered with QML.  
Must be a sub-class of QObject.

Here Clan has property person which has property name
'''
class SlottedModel(QObject):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._person = Person()
        

    '''
    Define getter of 'person' property. 
    The C++ type of the property is QObject !!!
    '''
    # @pyqtProperty('QObject') this doesn't work
    @pyqtSlot(str, result=Person)
    def get(self, submodelName):
        # Really want to lookup the submodel, like a dictionary, but for testing just return one
        print("get() called with arg:", submodelName)
        return self._person




      
