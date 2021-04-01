import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

#app = QApplication(sys.argv)
#window = QWidget()
#window.setWindowTitle('PyQt5 App')
#window.setGeometry (100, 100, 280, 80)
#window.move(600, 15)
#helloMsg = QLabel('<h1> Hello World!</h1>', parent=window)
#helloMsg.move(60, 15)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Layout managers demo')
layout = QHBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Centre'))
layout.addWidget(QPushButton('Right'))
window.setLayout(layout)



window.show()
sys.exit(app.exec_())
