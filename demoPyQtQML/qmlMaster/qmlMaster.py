'''
Object with methods (utilities) dealing with QML.

Hides details but also more robust than Qt methods.

Note findChild was broken until recently, see PyQt mail list report.
result = qmlRoot.findChild(model.person.Person, "person")
'''
from PyQt5.QtCore import qWarning, QObject
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtQuick import QQuickItem, QQuickView
from PyQt5.QtQml import QQmlProperty
from PyQt5.QtQuickWidgets import QQuickWidget

from qtEmbeddedQmlFramework.resourceManager import resourceMgr



class QmlMaster(object):
  
  def quickRoot(self, quickThing):
    '''
    quickThing has a tree of QML objects.
    Root of the tree.
    
    quickThing is QQuickView is a QWindow
    OR quickThing is a QQuickWidget
    '''
    assert isinstance(quickThing, QQuickView) or isinstance(quickThing, QQuickWidget)
    try:
      qmlRoot = quickThing.rootObject()  # objects()[0]
    except:
      qWarning("quickThing empty: failed to read or parse qml?")
      raise
    
    #print(qmlRoot)
    assert isinstance(qmlRoot, QQuickItem)
    return qmlRoot

  
  def findComponent(self, quickview, className, objectName):
      '''
      In quickview, find child with class className and objectName equal to objectName.
      '''
      root = self.quickRoot(quickview)
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
    
  """
  Deprecated: qtEmbeddedQmlFramework has more nuanced getting of QUrl
  This doesn't work for embedded resources.
  
  def qmlFilenameToQUrl(self, qml):
    qmlUrl=QUrl(qml)
    assert qmlUrl.isValid()
    #print(qmlUrl.path())
    #assert qmlUrl.isLocalFile()
    return qmlUrl
  """
    
  def quickViewForQML(self, qmlFilename, transientParent=None):
    '''
    Create a QQuickView for qmlFilename.
    More robust: connects to error
    '''
    
    quickView = QQuickView()
    quickView.statusChanged.connect(self.onStatusChanged)
    
    qurl = resourceMgr.urlToQMLResource(resourceSubpath=qmlFilename)
    quickView.setSource(qurl)
    '''
    Show() the enclosing QWindow?
    But this means the window for e.g. the toolbar is visible separately?
    '''
    #quickView.show()
    print("Created QQuickView for:", qurl.path())
    if transientParent is not None:
      quickView.setTransientParent(transientParent)
    return quickView
    

  def widgetForQMLUsingQQuickWidget(self, qmlFilename, parentWindow):
    widget = QQuickWidget()
    qurl = resourceMgr.urlToQMLResource(resourceSubpath=qmlFilename)
    widget.setSource(qurl)
    widget.show()
    " Return widget both as widget and quickThing having rootObject() "
    return widget, widget
  
  
  def widgetAndQuickViewForQML(self, qmlFilename, parentWindow):
    '''
    widget containing quickview, and quickview itself.
    
    Uses old Qt API: QQuickView and CreateWindowContainer
    See QTBUG-32934, you can't find the QWindow from the container QWidget, you must remember it.
    '''
    quickview = self.quickViewForQML(qmlFilename)
    widget = self.widgetForQuickView(quickview, parentWindow)
    return widget, quickview
  
  
  
  def widgetForQML(self, qmlFilename, parentWindow):
    ''' 
    Put QML in QQuickView and wrap in QWidget window. 
    
    I found that if you don't parent the widget,
    you get strange behaviour such as QML Dialog not visible when you open() it.
    '''
    quickview = self.quickViewForQML(qmlFilename)
    result = self.widgetForQuickView(quickview, parentWindow)
    return result
  
  
  def widgetForQuickView(self, quickview, parentWindow):
    ''' Wrap QQuickView in QWidget window. '''
    return QWidget.createWindowContainer(quickview, parent=parentWindow)
  
  
  def appQWindow(self):
    '''
    QWindow of app, or None.
    
    Needed to transientParent a QQuickView to app QWindow.
    '''
    qwinList = QGuiApplication.topLevelWindows()
    #print("window count", len(qwinList))
    #print(qwinList[0])
    if len(qwinList)==1:
      result = qwinList[0]
    else:
      print("Fail to find single QWindow for app.")
      result = None
    return result
    
    
    
  def onStatusChanged(self, status):
    " Handler for signal from QQuickView. "
    print("status changed", status)
    # TODO look for errors
    