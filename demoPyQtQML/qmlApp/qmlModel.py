
from PyQt5.QtQml import qmlRegisterType
# qmlRegisterSingletonType #, QQmlComponent, QQmlEngine

from demoPyQtQML.model.person import Person
from demoPyQtQML.model.qmlDelegate import QmlDelegate
from demoPyQtQML.model.clan import Clan
from demoPyQtQML.model.slottedModel import SlottedModel

class QmlModel(object):
  '''
  App's model (of MVC pattern.)
  '''
  
  def __init__(self):
    pass
  
  def register(self):
    uri = "org.qtproject.demo.weather"
    '''
    Register the Python type.
    - URI is 'People' (i.e. library or module e.g. 'import People 1.0' in QML
    - it's v1.0 
    - type will be called 'Person' in QML.
    '''
    # C++ qmlRegisterSingletonType(uri, 1, 0, "ApplicationInfo", systeminfo_provider)
    # Python signature: qmlRegisterSingletonType(type, str, int, int, str, callable)
    #qmlRegisterSingletonType("ApplicationInfo", 1, 0, "ApplicationInfo")
    '''
    Unlike c++, where you cast result to a type, in Python first arg is type
    '''
    qmlRegisterType(Person, 'People', 1, 0, 'Person')
    qmlRegisterType(QmlDelegate, 'QmlDelegate', 1, 0, 'DialogDelegate')
    qmlRegisterType(Clan, 'Clan', 1, 0, 'Clan')
    qmlRegisterType(SlottedModel, 'SlottedModel', 1, 0, 'SlottedModel')
