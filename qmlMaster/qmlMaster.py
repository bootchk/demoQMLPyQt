'''
Object with methods (utilities) dealing with QML.

Hides details but also more robust than Qt methods.

Note findChild was broken until recently, see PyQt mail list report.
result = qmlRoot.findChild(model.person.Person, "person")
'''
from PyQt5.QtCore import qWarning, QObject, QUrl
from PyQt5.QtWidgets import QWidget
from PyQt5.QtQuick import QQuickItem, QQuickView
from PyQt5.QtQml import QQmlProperty


class QmlMaster(object):
  
  def quickViewRoot(self, quickview):
    '''
    QQuickView is a QWindow having a tree of QML objects.
    Root of the tree.
    '''
    assert isinstance(quickview, QQuickView)
    try:
      qmlRoot = quickview.rootObject()  # objects()[0]
    except:
      qWarning("Failed to read or parse qml.")
      raise
    
    print(qmlRoot)
    assert isinstance(qmlRoot, QQuickItem)
    return qmlRoot


  def findComponent(self, quickview, className, objectName):
      '''
      In quickview, find child with class className and objectName equal to objectName.
      '''
      root = self.quickViewRoot(quickview)
      return self.findComponentFromRoot(root, className, objectName)
  
  
  def findComponentFromRoot(self, root, className, objectName):
      '''
      In tree at root, find child with class className and objectName equal to objectName.
      '''
      result = None
      
      children = root.findChildren(QObject)
      for item in children:
        # Note the QML id property is NOT the objectName
        if isinstance(item, className) and item.objectName()==objectName:
          print("Found object of class", className, objectName)
          result = item
          break
      if result is None:
        print("Failed to find component named:", objectName)
      return result
  
  
  '''
  Find without searching.  Broken by bug in PyQt, reported and since fixed.
  '''
  def findComponent2(self, aType, name):
    assert isinstance(name, str)
    result = self.getWindow().findChild(aType, name)
    #result = self.getWindow().findChild(QObject, name)

    if result is None:
      print("Failed to find instance named:", name, " of type:", aType)
      raise RuntimeError
    assert result is None or isinstance(result, QQuickItem)
    return result
    
    
  def dumpQMLComponents(self, root):
    children = root.findChildren(QObject)
    for item in children:
      # Note the QML id property is NOT the objectName
      print(item, "name is:", item.objectName() )
      try:
        '''
        Apparently you can't just access item's properties: item.id
        Also, the id property apparently is not accessible via QQmlProperty.
        '''
        foo = QQmlProperty.read(item, "shoeSize")
        print("shoeSize property:", foo)
      except AttributeError:
        pass
      #if isinstance(item, model.person.Person):
      #  print("Is Person")
    
  def qmlFilenameToQUrl(self, qml):
    qmlUrl=QUrl(qml)
    assert qmlUrl.isValid()
    print(qmlUrl.path())
    #assert qmlUrl.isLocalFile()
    return qmlUrl
    
    
  def quickViewForQML(self, qmlFilename):
    '''
    Create a QQuickView for qmlFilename.
    More robust: connects to error
    '''
    quickView = QQuickView()
    quickView.statusChanged.connect(self.onStatusChanged)
    quickView.setSource(self.qmlFilenameToQUrl(qmlFilename))
    return quickView
  
  
  def widgetForQML(self, qmlFilename):
    ''' Wrap QQuickView in QWidget window. '''
    quickview = QQuickView(self.qmlFilenameToQUrl(qmlFilename))
    result = QWidget.createWindowContainer(quickview)
    return result
  
    
  def onStatusChanged(self, status):
    print("status changed", status)
    