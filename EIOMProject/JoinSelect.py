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
        title.setFont(QFont('impact', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 50, 1000, 200)

        studentBtn = QPushButton(w)
        studentBtn.setStyleSheet('background-color: rgb(0,0,0,0); ')
        studentBtn.setIcon(QIcon('img/student.png'))
        studentBtn.setIconSize(QSize(180,180))
        studentBtn.setGeometry(200,320,200,200)

        companyBtn = QPushButton(w)
        companyBtn.setStyleSheet('background-color: rgb(0,0,0,0); ')
        companyBtn.setIcon(QIcon('img/company.png'))
        companyBtn.setIconSize(QSize(180, 180))
        companyBtn.setGeometry(500, 320, 200, 200)

        teacherBtn = QPushButton(w)
        teacherBtn.setStyleSheet('background-color: rgb(0,0,0,0); ')
        teacherBtn.setIcon(QIcon('img/teacher.png'))
        teacherBtn.setIconSize(QSize(180, 180))
        teacherBtn.setGeometry(800, 320, 200, 200)

        sL = QLabel("학생", w)
        sL.setFont(QFont('맑은 고딕', 18))
        sL.setAlignment(QtCore.Qt.AlignCenter)
        sL.setGeometry(250, 500, 100, 100)

        cL = QLabel("회사", w)
        cL.setFont(QFont('맑은 고딕', 18))
        cL.setAlignment(QtCore.Qt.AlignCenter)
        cL.setGeometry(550, 500, 100, 100)

        tL = QLabel("교사", w)
        tL.setFont(QFont('맑은 고딕', 18))
        tL.setAlignment(QtCore.Qt.AlignCenter)
        tL.setGeometry(850, 500, 100, 100)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = JoinSelect()
    ex.show()
    app.exec_()