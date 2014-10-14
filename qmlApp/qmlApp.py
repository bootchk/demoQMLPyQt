
import sys

from PyQt5.QtCore import QObject, QUrl
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickItem, QQuickWindow

from qmlApp.qmlModel import QmlModel
from model.person import Person

from PyQt5.QtQml import QQmlApplicationEngine

class QmlApp(object):
  '''
  Contains QApp without reference to a window.
  I.E. all windows defined in qml file.
  
  Has event loop (never returns)
  '''
  def __init__(self, qml):
    app = QGuiApplication(sys.argv)
    
    '''
    Register our Python model (classes/types to be registered with QML.)
    '''
    model = QmlModel()
    model.register()
    
    engine = QQmlApplicationEngine()
    '''
    Need this if no stdio, i.e. Android, OSX, iOS.
    OW, qWarnings to stdio.
    engine.warnings.connect(self.errors)
    '''
    engine.load(self.qmlFilenameToQUrl(qml))
    engine.quit.connect(app.quit)
    '''
    We really don't need to keep a reference to engine,
    the methods below that use it are fluff.
    '''
    self.engine = engine
    
    # Test must show window before can find objects?
    window = self.getWindow()
    window.show()
    
    '''
    Suggested architecture is for model layer (Python) not to know of UI layer,
    and thus not make connections.
    The model layer can emit signals to UI layer and vice versa,
    but only the UI layer knows what connections to make
    '''
    #self.makeConnections()
    
    app.exec_()   # !!! C exec => Python exec_
    print("Application returned")
    
    
  def qmlFilenameToQUrl(self,qml):
    qmlUrl=QUrl(qml)
    assert qmlUrl.isValid()
    print(qmlUrl.path())
    #assert qmlUrl.isLocalFile()
    return qmlUrl
    
    
  def makeConnections(self):
    '''
    Connections
    Here, make connection on the Python side
    
    NOT WORKING, and of dubious value
    '''
    # Connect button signal to person handler
    self.dumpQMLComponents()
    button = self.findComponent(QQuickItem, "button")
    foo = self.findComponent(Person, "foo")
    button.activated.connect(foo.doActivated)
    
  
  def findComponent(self, aType, name):
    assert isinstance(name, str)
    result = self.getWindow().findChild(aType, name)
    #result = self.getWindow().findChild(QObject, name)

    if result is None:
      print("Failed to find instance named:", name, " of type:", aType)
      raise RuntimeError
    assert result is None or isinstance(result, QQuickItem)
    return result
  
  
  def dumpQMLComponents(self):
    children = self.getWindow().findChildren(QObject)
    for item in children:
      # Note the QML id property is NOT the objectName
      print(item, "name is:", item.objectName())
    
    
  def getWindow(self):
    " QQuickWindow containing QML app's GUI"
    try:
      qmlRoot = self.engine.rootObjects()[0]
    except:
      qWarning("Failed to read or parse qml.")
      raise
    
    print(qmlRoot)
    assert isinstance(qmlRoot, QQuickWindow)
    return qmlRoot
    
  
    
  def errors(self, warningList):
    for item in warningList:
      # syslog on Android and OSX and iOS
      print(item)
    