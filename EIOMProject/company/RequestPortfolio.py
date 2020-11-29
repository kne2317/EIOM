import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class RequestPortfolio(QWidget):

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
        self.setPalette(palette)

        self.w.setLayout(layout)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 10, 1000, 50)

        stateBtn = QPushButton('취업의뢰', self.w)
        stateBtn.setFont(QFont(self.basicInfo.font1, 13))
        stateBtn.setGeometry(0, 70, self.basicInfo.WindowWidth / 3, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(self.basicInfo.WindowWidth / 3 * 1, 70, self.basicInfo.WindowWidth / 3, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('회사', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(self.basicInfo.WindowWidth / 3 * 2, 70, self.basicInfo.WindowWidth / 3, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        periodL=QLabel("기간",self.w)
        periodL.setFont(QFont(self.basicInfo.font1,15))
        periodL.setGeometry(150,180,500,50)

        l = QLabel(" ~ ", self.w)
        l.setFont(QFont(self.basicInfo.font1, 15))
        l.setGeometry(640, 180, 500, 50)

        year1=QLineEdit(self.w)
        year1.setPlaceholderText('연도')
        year1.setFont(QFont(self.basicInfo.font1,13))
        year1.setGeometry(250,190,100,40)

        month1=QComboBox(self.w)
        month1.setFont(QFont(self.basicInfo.font1, 13))
        month1.setGeometry(380,190,100,40)
        for i in range (0,12):
            month1.addItem(str(i+1)+"월")

        day1 = QComboBox(self.w)
        day1.setFont(QFont(self.basicInfo.font1, 13))
        day1.setGeometry(510, 190, 100, 40)
        for i in range(0, 30):
            day1.addItem(str(i + 1) + "일")

        year2 = QLineEdit(self.w)
        year2.setPlaceholderText('연도')
        year2.setFont(QFont(self.basicInfo.font1, 13))
        year2.setGeometry(700, 190, 100, 40)

        month2 = QComboBox(self.w)
        month2.setFont(QFont(self.basicInfo.font1, 13))
        month2.setGeometry(830, 190, 100, 40)
        for i in range(0, 12):
            month2.addItem(str(i + 1) + "월")

        day2 = QComboBox(self.w)
        day2.setFont(QFont(self.basicInfo.font1, 13))
        day2.setGeometry(960, 190, 100, 40)
        for i in range(0, 30):
            day2.addItem(str(i + 1) + "일")

        reasonL = QLabel('열람사유',self.w)
        reasonL.setFont(QFont(self.basicInfo.font1,15))
        reasonL.setGeometry(150,320,500,50)

        reason = QTextBrowser(self.w)
        reason.setFont(QFont(self.basicInfo.font1, 12))
        reason.setGeometry(270, 330, 800, 130)


        requestBtn = QPushButton('신청', self.w)
        requestBtn.setFont(QFont(self.basicInfo.font1, 12))
        requestBtn.setGeometry(950, 630, 120, 40)
        requestBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = RequestPortfolio()
    sys.exit(app.exec_())
