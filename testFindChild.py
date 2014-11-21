'''
Demonstrate a bug? in findChild: fails to find a child that findChildren() shows does exist.

There is another report of this bug? at 
http://stackoverflow.com/questions/16329622/findchild-returns-none-with-custom-widget
so although this example uses QML, the bug might be more general.
'''
import sys

from PyQt5.QtCore import QObject,QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import qmlRegisterType
from PyQt5.QtQuick import QQuickView, QQuickItem


class Person(QObject):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
def main():
    print("start")
    app = QApplication(sys.argv)
    qmlRegisterType(Person, 'People', 1, 0, 'Person')
    v = QQuickView(QUrl("testFindChild.qml"))
    qmlRoot = v.rootObject()
    assert isinstance(qmlRoot, QQuickItem)
    assert isinstance(qmlRoot, QObject)
    dumpQMLComponents(qmlRoot)
    result = qmlRoot.findChild(Person, "person")
    assert result is not None
    
    sys.exit(app.exec_())

def dumpQMLComponents(root):
    children = root.findChildren(QObject)
    for item in children:
      # Note the QML id property is NOT the objectName
      print(item, item.objectName())
      if isinstance(item, Person) and item.objectName() == "person":
        print("Object of type: Person having name: person")
        
main()