
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication

#from qmlApp.quickWindow import QuickWindowFactory
from qmlApp.qmlModel import QmlModel

from PyQt5.QtQml import QQmlApplicationEngine

class QmlApp(object):
  '''
  Contains QApp having QQuickWindow
  
  Has event loop (never returns)
  '''
  def __init__(self, qml):
    app = QGuiApplication(sys.argv)
    
    model = QmlModel()
    model.register()
    
    qmlUrl=QUrl(qml)
    assert qmlUrl.isValid()
    print(qmlUrl.path())
    #assert qmlUrl.isLocalFile()
    
    """
    Create an engine a reference to the window?
    
    window = QuickWindowFactory().create(qmlUrl=qmlUrl)
    window.show() # visible
    """
    engine = QQmlApplicationEngine()
    '''
    Need this if no stdio, i.e. Android, OSX, iOS.
    OW, qWarnings to stdio.
    engine.warnings.connect(self.errors)
    '''
    engine.load(qmlUrl)
    engine.quit.connect(app.quit)
    
    app.exec_()   # !!! C exec => Python exec_
    print("Application returned")
    
  def errors(self, warningList):
    for item in warningList:
      # syslog on Android and OSX and iOS
      print(item)
    