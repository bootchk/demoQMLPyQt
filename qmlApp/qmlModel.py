
from PyQt5.QtQml import qmlRegisterType
# qmlRegisterSingletonType #, QQmlComponent, QQmlEngine

from model.person import Person

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
