import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar


#app = QApplication(sys.argv)
#window = QWidget()
#window.setWindowTitle('PyQt5 App')
#window.setGeometry (100, 100, 280, 80)
#window.move(600, 15)
#helloMsg = QLabel('<h1> Hello World!</h1>', parent=window)
#helloMsg.move(60, 15)

#app = QApplication(sys.argv)
#window = QWidget()
#window.setWindowTitle('Layout managers demo')
#layout = QHBoxLayout()
#layout.addWidget(QPushButton('Left'))
#layout.addWidget(QPushButton('Centre'))
#layout.addWidget(QPushButton('Right'))
#window.setLayout(layout)

class Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('My main window')
        self.setCentralWidget(QLabel("I'm the central widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the status bar")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

