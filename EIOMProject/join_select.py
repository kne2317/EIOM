import sys

from PySide2.QtCore import QSize
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore, QtGui

class JoinSelect(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        w = QWidget(self)
        layout = QVBoxLayout()
        w.setWindowTitle('EIOM')
        w.resize(1200, 700)
        self.move(400,100)
        self.setFixedSize(1200,700)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/join_select_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - Join", w)
        title.setFont(QFont('Candara', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 50, 1000, 200)

        studentBtn = QPushButton(w)
        '''
        s = QIcon("img/student.png")
        s= s.scaled(QSize(500,500))
        studentBtn.setStyleSheet('background-color: rgb(0,0,0,0); ')
        studentBtn.setIcon(s)
        '''
        studentBtn.setGeometry(100,100,200,200)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = JoinSelect()
    sys.exit(app.exec_())
