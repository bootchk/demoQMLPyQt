
from PyQt5.QtCore import qWarning
#from PyQt5.QtGui import QWindow
from PyQt5.QtQml import QQmlApplicationEngine
#from PyQt5.QtQuick import QQuickWindow


class QuickWindowFactory(object):
  
  def create(self, qmlUrl):
    # assert isinstance(qmlUrl, QUrl)
    engine = QQmlApplicationEngine(qmlUrl)
  
    try:
      qmlRoot = engine.rootObjects()[0]
    except:
      qWarning("Failed to read or parse qml.")
      raise
    
    print(qmlRoot)
    #assert isinstance(qmlRoot, QQuickWindow)
    return qmlRoot
  
    #super().__init__(qmlRoot)
    '''
    if result is None:
      qWarning("Error: Root of QML must be a Window.")
      raise RuntimeError
    '''