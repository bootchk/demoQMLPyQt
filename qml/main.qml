    import QtQuick 2.1
    import QtQuick.Controls 1.0
    import QtQuick.Controls.Styles 1.0
    import org.qtproject.demo.weather 1.0
    
    ApplicationWindow {
    id: root
    height: 700
    width: 1200
    title: "Quick Forecast"
    property string statusBarMessage
    property Component citiesPage: CitiesPage {
      onUpdateStatusBar: statusBarMessage = message
      onNextPage: if (!isLocked) {
      pageView.push(longTermPage)
      clearSearchBox()
      }
    }
    property Component longTermPage: LongTermPage {
      onUpdateStatusBar: statusBarMessage = message
      onNextPage: if (!isLocked) {
      pageView.push(oneDayPage)
      }
      onPreviousPage: {
      ApplicationInfo.currentIndexDay = -1
      pageView.pop()
      }
    }
    property Component oneDayPage: OneDayPage {
      onUpdateStatusBar: statusBarMessage = message
      onPreviousPage: if (!isLocked) {
      pageView.pop()
      }
    }
    StackView {
    id: pageView
    anchors.fill: parent
    focus: true
    Keys.onReleased: {
    if (event.key === Qt.Key_Back ||
    (event.key === Qt.Key_Left && (event.modifiers & Qt.AltModifier))) {
    if (pageView.depth > 1) {
    event.accepted = true
    if (!currentItem.isLocked)
    currentItem.previousPage()
    } else {
    if (!currentItem.hasNoSearchText) {
    event.accepted = true
    currentItem.clearSearchBox()
    }
    }
    }
    }
    initialItem: citiesPage
    delegate: StackViewDelegate {
    pushTransition: StackViewTransition {
    function transitionFinished(properties)
    {
    properties.exitItem.opacity = 1
    }
    PropertyAnimation {
    target: enterItem
    property: "x"
    from: target.width
    to: 0
    duration: 500
    easing.type: Easing.OutSine
    }
    PropertyAnimation {
    target: exitItem
    property: "x"
    from: 0
    to: -target.width
    duration: 500
    easing.type: Easing.OutSine
    }
    }
    popTransition: StackViewTransition {
    function transitionFinished(properties)
    {
    properties.exitItem.opacity = 1
    }
    PropertyAnimation {
    target: enterItem
    property: "x"
    from: -target.width
    to: 0
    duration: 500
    easing.type: Easing.OutSine
    }
    PropertyAnimation {
    target: exitItem
    property: "x"
    from: 0
    to: target.width
    duration: 500
    easing.type: Easing.OutSine
    }
    }
    property Component replaceTransition: pushTransition
    }
    }
    statusBar: StatusBar {
    id: statusbar
    width: parent.width
    opacity: label.text !== "" ? 1 : 0
    property real statusBarHeight: 65 * ApplicationInfo.ratio
    height: label.text !== "" ? statusBarHeight : 0
    Behavior on height { NumberAnimation {easing.type: Easing.OutSine}}
    Behavior on opacity { NumberAnimation {}}
    style: StatusBarStyle {
    padding { left: 0; right: 0 ; top: 0 ; bottom: 0}
    property Component background: Rectangle {
    implicitHeight: 65 * ApplicationInfo.ratio
    implicitWidth: root.width
    color: ApplicationInfo.colors.smokeGray
    Rectangle {
    width: parent.width
    height: 1
    color: Qt.darker(parent.color, 1.5)
    }
    Rectangle {
    y: 1
    width: parent.width
    height: 1
    color: "white"
    }
    }
    }
    TouchLabel {
    id: label
    y: 32 * ApplicationInfo.ratio - height/2
    width: parent.width // The text will only wrap if an explicit width has been set
    text: statusBarMessage
    textFormat: Text.RichText
    onLinkActivated: Qt.openUrlExternally(link)
    wrapMode: Text.Wrap
    pixelSize: 18
    letterSpacing: -0.15
    color: ApplicationInfo.colors.mediumGray
    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
    function decreaseFontSizeOnNarrowScreen() {
    if (label.implicitHeight > statusbar.statusBarHeight)
    pixelSize = Math.floor(pixelSize * statusbar.statusBarHeight/label.implicitHeight)
    }
    onTextChanged: {
    if (text === "")
    pixelSize = 18
    else
    decreaseFontSizeOnNarrowScreen()
    }
    onWidthChanged: decreaseFontSizeOnNarrowScreen()
    }
    }
    }

