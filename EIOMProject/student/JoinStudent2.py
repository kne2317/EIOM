import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore, QtGui

from BasicInfo import BasicInfo


class JoinS2(QWidget):

    def __init__(self, student):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.student = student
        self.student.print()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/join_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - JOIN [ Student ]", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 45, 1000, 50)

        major = QComboBox(self.w)
        major.move(280,200)
        major.setFixedHeight(50)
        major.setFixedWidth(330)
        major.setFont(QFont(self.basicInfo.font1, 13))
        major.addItem('뉴미디어 소프트웨어과')
        major.addItem('뉴미디어 웹솔루션과')
        major.addItem('뉴미디어 디자인과')

        grade = QComboBox(self.w)
        grade.move(630, 200)
        grade.setFixedHeight(50)
        grade.setFixedWidth(130)
        grade.setFont(QFont(self.basicInfo.font1, 13))
        grade.addItem('1학년')
        grade.addItem('2학년')
        grade.addItem('3학년')

        ban = QComboBox(self.w)
        ban.move(780, 200)
        ban.setFixedHeight(50)
        ban.setFixedWidth(130)
        ban.setFont(QFont(self.basicInfo.font1, 13))

        ban.addItem('1반')
        ban.addItem('2반')
        ban.addItem('3반')
        ban.addItem('4반')
        ban.addItem('5반')
        ban.addItem('6반')

        pfL= QLabel('포트폴리오',self.w)
        pfL.setFont(QFont(self.basicInfo.font1,15))
        pfL.move(280,300)

        self.pfInput = QLineEdit(self.w)
        self.pfInput.setFont(QFont(self.basicInfo.font1,10))
        self.pfInput.setGeometry(280,350,500,50)

        pfBtn = QPushButton('Browse', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 12))
        pfBtn.setGeometry(800, 350, 110, 50)
        pfBtn.clicked.connect(self.show_file_open_p)

        introduceL = QLabel('자기소개서', self.w)
        introduceL.setFont(QFont(self.basicInfo.font1, 15))
        introduceL.move(280, 450)

        self.introduceInput = QLineEdit(self.w)
        self.introduceInput.setFont(QFont(self.basicInfo.font1, 10))
        self.introduceInput.setGeometry(280, 500, 500, 50)

        introduceBtn = QPushButton('Browse', self.w)
        introduceBtn.setFont(QFont(self.basicInfo.font1, 12))
        introduceBtn.setGeometry(800, 500, 110, 50)
        introduceBtn.clicked.connect(self.show_file_open_i)

        joinBtn = QPushButton('JOIN', self.w)
        joinBtn.setFont(QFont(self.basicInfo.font1, 15))
        joinBtn.setGeometry(280, 600, 630, 50)

        self.show()

    def show_file_open_p(self):
        fname = QFileDialog.getOpenFileName()
        self.pfInput.setText(fname[0])

    def show_file_open_i(self):
        fname = QFileDialog.getOpenFileName()
        self.introduceInput.setText(fname[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = JoinS2()
    sys.exit(app.exec_())


