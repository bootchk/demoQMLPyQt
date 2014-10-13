
from PyQt5.QtQml import qmlRegisterType
# qmlRegisterSingletonType #, QQmlComponent, QQmlEngine

from person import Person

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
    Its URI is 'People', it's v1.0 and the type
    # will be called 'Person' in QML.
    '''
    # C++ qmlRegisterSingletonType(uri, 1, 0, "ApplicationInfo", systeminfo_provider)
    # Python signature: qmlRegisterSingletonType(type, str, int, int, str, callable)
    #qmlRegisterSingletonType("ApplicationInfo", 1, 0, "ApplicationInfo")
    qmlRegisterType(Person, 'People', 1, 0, 'Person')
