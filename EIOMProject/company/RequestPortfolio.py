import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
import company.EmployeeRequestDB
from company.Company import Company
import company.NoneEmployementRequest
import company.CompanyEmploymentRequest
import company.CompanyInfo
import company.NonePofol
import company.PofolList
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
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/background.png")))
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

        pfBtn = QPushButton('포트폴리오', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(self.basicInfo.WindowWidth / 3 * 1, 70, self.basicInfo.WindowWidth / 3, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(self.basicInfo.WindowWidth / 3 * 2, 70, self.basicInfo.WindowWidth / 3, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        periodL=QLabel("기간",self.w)
        periodL.setFont(QFont(self.basicInfo.font1,15))
        periodL.setGeometry(150,180,500,50)

        l = QLabel(" ~ ", self.w)
        l.setFont(QFont(self.basicInfo.font1, 15))
        l.setGeometry(640, 180, 500, 50)

        self.year1=QLineEdit(self.w)
        self.year1.setPlaceholderText('연도')
        self.year1.setFont(QFont(self.basicInfo.font1,13))
        self.year1.setGeometry(250,190,100,40)

        self.month1=QComboBox(self.w)
        self.month1.setFont(QFont(self.basicInfo.font1, 13))
        self.month1.setGeometry(380,190,100,40)
        for i in range (0,12):
            self.month1.addItem(str(i+1)+"월")

        self.day1 = QComboBox(self.w)
        self.day1.setFont(QFont(self.basicInfo.font1, 13))
        self.day1.setGeometry(510, 190, 100, 40)
        for i in range(0, 30):
            self.day1.addItem(str(i + 1) + "일")

        self.year2 = QLineEdit(self.w)
        self.year2.setPlaceholderText('연도')
        self.year2.setFont(QFont(self.basicInfo.font1, 13))
        self.year2.setGeometry(700, 190, 100, 40)

        self.month2 = QComboBox(self.w)
        self.month2.setFont(QFont(self.basicInfo.font1, 13))
        self.month2.setGeometry(830, 190, 100, 40)
        for i in range(0, 12):
            self.month2.addItem(str(i + 1) + "월")

        self.day2 = QComboBox(self.w)
        self.day2.setFont(QFont(self.basicInfo.font1, 13))
        self.day2.setGeometry(960, 190, 100, 40)
        for i in range(0, 30):
            self.day2.addItem(str(i + 1) + "일")

        reasonL = QLabel('열람사유',self.w)
        reasonL.setFont(QFont(self.basicInfo.font1,15))
        reasonL.setGeometry(150,320,500,50)

        self.reason = QTextEdit(self.w)
        self.reason.setFont(QFont(self.basicInfo.font1, 12))
        self.reason.setGeometry(270, 330, 800, 130)


        requestBtn = QPushButton('신청', self.w)
        requestBtn.setFont(QFont(self.basicInfo.font1, 12))
        requestBtn.setGeometry(950, 630, 120, 40)
        requestBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')
        requestBtn.clicked.connect(self.request)

        stateBtn.clicked.connect(self.state)
        pfBtn.clicked.connect(self.pf)
        infoBtn.clicked.connect(self.info)
    def request(self):
        recruit = self.year1.text() + "년" + self.month1.currentText() + self.day1.currentText() + \
                  " ~ " + self.year2.text() + "년" + self.month2.currentText() + self.day2.currentText();
        company.EmployeeRequestDB.pofolRequestInsert(self.reason.toPlainText(),recruit)
        self.pf()
    def state(self):
        if Company.request_authority == 0:
            self.ncr = company.NoneEmployementRequest.NoneEmployementRequest()
            self.ncr.show()
            self.hide()
        else:
            self.cr = company.CompanyEmploymentRequest.CompanyEmploymentRequest()
            self.cr.show()
            self.hide()

    def pf(self):
        if Company.pfauthority == 0:
            self.np = company.NonePofol.NonePofol()
            self.np.show()
            self.hide()
        else:
            self.p = company.PofolList.pofolList()
            self.p.show()
            self.hide()

    def info(self):
        self.ci = company.CompanyInfo.CompanyInfo()
        self.ci.show()
        self.hide()

