// QML views

import QtQuick 2.4
import QtQuick.Controls 1.3

// Need layouts for toolbar
import QtQuick.Layouts 1.1


ApplicationWindow {
    visible: true
    title: "Test "

    width: 640
    height: 420
    minimumHeight: 400
    minimumWidth: 600

    

    // Actions
    Action {
        id: fileAction
        text: "&File"
        shortcut: StandardKey.Open
        tooltip: "Choose file"
    }
    

  
    TabView {
        enabled: enabledCheck.checked
        tabPosition: controlPage.item ? controlPage.item.tabPosition : Qt.TopEdge
        anchors.fill: parent
        anchors.margins: Qt.platform.os === "osx" ? 12 : 2

        Tab {
            id: controlPage
            title: "Tabbed"
            TabView {
              id:nestedTab
              enabled: enabledCheck.checked
              tabPosition: controlPage.item ? controlPage.item.tabPosition : Qt.TopEdge
              anchors.fill: parent
              anchors.margins: Qt.platform.os === "osx" ? 12 : 2
      
              Tab {
                  id: controlPage
                  title: "One"
               }
              Tab {
                  title: "Two"   
              }
           }
        }
        Tab {
            title: "Split"
            SplitView {
              Label { text: "foo" }
              Label { text: "bar" }
              Label { text: "baz" }
            }
        }
        Tab {
            title: "Scroll"
            ScrollView {
              Label { text: "foo" }
            }
        }
        Tab {
            title: "Stack"
            StackView {
               id: stack
               initialItem: view

                Component {
                  id: view
          
                  MouseArea {
                      Text {
                          text: stack.depth
                          anchors.centerIn: parent
                      }
                      onClicked: stack.push(view)
                   }
                }
            }
        }
        ListModel {
           id: libraryModel
           ListElement{ title: "A Masterpiece" ; author: "Gabriel" }
           ListElement{ title: "Brilliance"    ; author: "Jens" }
           ListElement{ title: "Outstanding"   ; author: "Frederik" }
        }
        Tab {
            title: "Table"
            TableView {
               TableViewColumn{ role: "title"  ; title: "Title" ; width: 100 }
               TableViewColumn{ role: "author" ; title: "Author" ; width: 200 }
               model: libraryModel
            }
         }
    }
    
}