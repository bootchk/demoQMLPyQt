#! /usr/local/bin/python3

'''
Drawn from examples:
- PyQt 5.3.2 Reference Quide "Integrating Python and QML"
- PySide wiki
- Qt gallery example
- Qt QML reference guide
-- "Interacting with QML Objects from C++"
'''

import sys

from qtEmbeddedQmlFramework.resourceManager import resourceMgr
from demoPyQtQML.app import createApp


def main():
  # establish location of resources (either platform file system or embedded resource file system (.qrc)
  resourceMgr.setResourceRoot(fileMainWasLoadedFrom=__file__, appPackageName='demoPyQtQML')
  
  app = createApp()
  
  print("Created app")
  # Qt Main loop
  sys.exit(app.exec_())  # !!! C exec => Python exec_

main()