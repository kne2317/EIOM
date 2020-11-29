import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore, QtGui

from BasicInfo import BasicInfo
from student.JoinStudent3 import JoinS3
from student.Student import Student


class JoinS2(QWidget):

    def __init__(self, student=Student()):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.student = student

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

        self.major = QComboBox(self.w)
        self.major.move(280,200)
        self.major.setFixedHeight(50)
        self.major.setFixedWidth(330)
        self.major.setFont(QFont(self.basicInfo.font1, 13))
        self.major.addItem('뉴미디어 소프트웨어과')
        self.major.addItem('뉴미디어 웹솔루션과')
        self.major.addItem('뉴미디어 디자인과')

        self.grade = QComboBox(self.w)
        self.grade.move(630, 200)
        self.grade.setFixedHeight(50)
        self.grade.setFixedWidth(130)
        self.grade.setFont(QFont(self.basicInfo.font1, 13))
        self.grade.addItem('1학년')
        self.grade.addItem('2학년')
        self.grade.addItem('3학년')

        self.ban = QComboBox(self.w)
        self.ban.move(780, 200)
        self.ban.setFixedHeight(50)
        self.ban.setFixedWidth(130)
        self.ban.setFont(QFont(self.basicInfo.font1, 13))

        self.ban.addItem('1반')
        self.ban.addItem('2반')
        self.ban.addItem('3반')
        self.ban.addItem('4반')
        self.ban.addItem('5반')
        self.ban.addItem('6반')

        self.pfL= QLabel('포트폴리오',self.w)
        self.pfL.setFont(QFont(self.basicInfo.font1,15))
        self.pfL.move(280,300)

        self.pfInput = QLineEdit(self.w)
        self.pfInput.setFont(QFont(self.basicInfo.font1,10))
        self.pfInput.setGeometry(280,350,500,50)

        self.pfBtn = QPushButton('Browse', self.w)
        self.pfBtn.setFont(QFont(self.basicInfo.font1, 12))
        self.pfBtn.setGeometry(800, 350, 110, 50)
        self.pfBtn.clicked.connect(self.show_file_open_p)

        self.introduceL = QLabel('자기소개서', self.w)
        self.introduceL.setFont(QFont(self.basicInfo.font1, 15))
        self.introduceL.move(280, 450)

        self.introduceInput = QLineEdit(self.w)
        self.introduceInput.setFont(QFont(self.basicInfo.font1, 10))
        self.introduceInput.setGeometry(280, 500, 500, 50)

        self.introduceBtn = QPushButton('Browse', self.w)
        self.introduceBtn.setFont(QFont(self.basicInfo.font1, 12))
        self.introduceBtn.setGeometry(800, 500, 110, 50)
        self.introduceBtn.clicked.connect(self.show_file_open_i)

        self.nextBtn = QPushButton('NEXT>>', self.w)
        self.nextBtn.setFont(QFont(self.basicInfo.font1, 15))
        self.nextBtn.setGeometry(280, 600, 630, 50)
        self.nextBtn.clicked.connect(self.goNextPage)

        self.show()

    def goNextPage(self):
        # 위치 지정
        self.student.setMajor(self.major.currentText())
        self.student.setGrade(self.grade.currentText())
        self.student.setClass(self.ban.currentText())

        self.nextPage = JoinS3(self.student)

        geo = self.geometry()
        titlebar_height = QApplication.style().pixelMetric(QStyle.PM_TitleBarHeight)
        self.nextPage.move(geo.x(), geo.y() - titlebar_height)
        self.hide()

        self.nextPage.show()


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


