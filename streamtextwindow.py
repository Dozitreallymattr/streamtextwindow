#!/usr/bin/python
# Creates a transparent window with Streamtext.net captions appearing on the screen showing through whatever is behind
# Potential uses for captioning over powerpoint
# Need to add way to choose streamtext event id and perhaps change settings including adding and removing the background

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("Captions")
        self.setAttribute(Qt.WA_TranslucentBackground,True)

        # open the window up to a specific size
        newWidth = 1280
        newHeight = 140
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        x = (width // 2 ) - (newWidth // 2)
        y = (height // 2 ) - (newHeight // 2)
        self.setGeometry(x,y,newWidth,newHeight)

        ''' creates a frameless window'''
        ''' figure out how to create a window that shows the frame on mouseover so it can be moved'''
        ''' but hidden otherwise '''
        self.setWindowFlags(Qt.FramelessWindowHint);

        ''' Keeps the window on top of all other windows'''
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.browser = QWebEngineView()
        self.browser.page().setBackgroundColor(Qt.transparent)

        ''' Grabs the mouse and allows the user to use the events to move the window '''
        self.browser.grabMouse()

        self.setCentralWidget(self.browser)
        self.oldPos = self.pos()
        self.initUI()

    def initUI(self):
        ''' Get value for the sesssion to start'''
        mytext = self.getText()

        # Url for configuration possibilites https://streamtext.zendesk.com/hc/en-us/articles/210923103-Controlling-the-streaming-text-page-display
        self.browser.setUrl(QUrl("http://streamtext.net/player?event=" + mytext + "&ff=Verdana,sans-serif&fs=30&fgc=ffff00&spacing=2&scroll=0&indicator=0&header=false&controls=false&footer=false&chat=false"))
        self.show()

    def getText(self):
        ''' Get the name of the session to load'''
        text, okPressed = QInputDialog.getText(self, "StreamText Session Name", "Session Name:", QLineEdit.Normal, "")
        mytext = text
        return mytext
        #if okPressed and text != '':
        #    print(text)

    def mousePressEvent(self, event):
        if Qt.MouseButtons == Qt.RightButton:
            print ("Right Button Pressed")

    def mouseMoveEvent(self, event):
        ''' Move the window by clicking and dragging'''
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


app = QApplication(sys.argv)
window = MainWindow()
app.exec()