
from PyQt5.QtCore import pyqtProperty, QObject

from demoPyQtQML.model.person import Person

'''
A type that will be registered with QML.  
Must be a sub-class of QObject.

Here Clan has property person which has property name
'''
class Clan(QObject):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._person = Person()
        

    '''
    Define getter of 'person' property. 
    The C++ type of the property is QObject !!!
    '''
    # @pyqtProperty('QObject') this doesn't work
    @pyqtProperty(Person)
    def person(self):
        return self._person

    # Define the setter of the 'person' property.
    @person.setter
    def person(self, person):
        self._person = person


      
