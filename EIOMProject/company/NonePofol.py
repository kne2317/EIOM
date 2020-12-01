import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from company.Company import Company
import company.NoneEmployementRequest
import company.CompanyEmploymentRequest
import company.CompanyInfo
import company.RequestPortfolio
from BasicInfo import BasicInfo
import company.PofolList

class NonePofol(QWidget):

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
        stateBtn.setGeometry(0, 70, self.basicInfo.WindowWidth/3, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        pfBtn = QPushButton('포트폴리오', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(self.basicInfo.WindowWidth/3*1, 70, self.basicInfo.WindowWidth/3, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(self.basicInfo.WindowWidth/3*2, 70, self.basicInfo.WindowWidth/3, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noRequest = QLabel("포트폴리오 열람 권한이 없습니다.",self.w)
        noRequest.setFont(QFont(self.basicInfo.font1,13))
        noRequest.setGeometry(0,300,1200,100)
        noRequest.setAlignment(QtCore.Qt.AlignCenter)

        requestBtn = QPushButton('포트폴리오 열람 권한 신청하기', self.w)
        requestBtn.setFont(QFont(self.basicInfo.font1, 15))
        requestBtn.setGeometry(100, 600, 1000, 50)
        requestBtn.clicked.connect(self.pofol)

        stateBtn.clicked.connect(self.state)
        pfBtn.clicked.connect(self.pf)
        infoBtn.clicked.connect(self.info)
    def pofol(self):
        self.pf=company.RequestPortfolio.RequestPortfolio()
        self.pf.show()
        self.hide()

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
