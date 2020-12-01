import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo

from company.Company import Company
import company.NoneEmployementRequest
import company.CompanyEmploymentRequest
import company.CompanyInfo
import company.NonePofol
import company.EmployeeRequestDB
import company.PofolList

class ModifyInfo(QWidget):

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

        cNameL1=QLabel("기업명",self.w)
        cNameL1.setFont(QFont(self.basicInfo.font1,15))
        cNameL1.setGeometry(150,160,500,40)

        self.cNameL2 = QLineEdit("연지 소프트", self.w)
        self.cNameL2.setFont(QFont(self.basicInfo.font1, 13))
        self.cNameL2.setGeometry(350, 160, 250, 40)
        self.cNameL2.setText(Company.companyname)

        employeeL1 = QLabel("사원수", self.w)
        employeeL1.setFont(QFont(self.basicInfo.font1, 15))
        employeeL1.setGeometry(650, 160, 500, 40)

        self.employeeL2 = QLineEdit("10", self.w)
        self.employeeL2.setFont(QFont(self.basicInfo.font1, 13))
        self.employeeL2.setGeometry(850, 160, 250, 40)
        self.employeeL2.setText(str(Company.employees_num))

        majorL1 = QLabel("분야", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(150, 240, 500, 40)

        self.majorL2 = QLineEdit("개발", self.w)
        self.majorL2.setFont(QFont(self.basicInfo.font1, 13))
        self.majorL2.setGeometry(350, 240, 250, 40)
        self.majorL2.setText(Company.major)

        salesL1 = QLabel("연매출", self.w)
        salesL1.setFont(QFont(self.basicInfo.font1, 15))
        salesL1.setGeometry(650, 240, 500, 40)

        self.salesL2 = QLineEdit("10억", self.w)
        self.salesL2.setFont(QFont(self.basicInfo.font1, 13))
        self.salesL2.setGeometry(850, 240, 250, 40)
        self.salesL2.setText(Company.annualsale)

        companyIntroL = QLabel("기업소개", self.w)
        companyIntroL.setFont(QFont(self.basicInfo.font1, 15))
        companyIntroL.setGeometry(150, 320, 500, 50)

        self.companyIntro = QTextEdit(self.w)
        self.companyIntro.setFont(QFont(self.basicInfo.font1, 12))
        self.companyIntro.setGeometry(350, 330, 750, 130)
        self.companyIntro.setText(Company.introduce)

        webL1 = QLabel("웹사이트 ", self.w)
        webL1.setFont(QFont(self.basicInfo.font1, 15))
        webL1.setGeometry(150, 490, 500, 50)

        self.webL2 = QLineEdit("www.e-mirim.hs.kr", self.w)
        self.webL2.setFont(QFont(self.basicInfo.font1, 15))
        self.webL2.setGeometry(350, 490, 750, 50)
        self.webL2.setText(Company.web)

        addressL1 = QLabel("주소", self.w)
        addressL1.setFont(QFont(self.basicInfo.font1, 15))
        addressL1.setGeometry(150, 570, 500, 50)

        self.addressL2 = QLineEdit("남양주시 화도읍", self.w)
        self.addressL2.setFont(QFont(self.basicInfo.font1, 15))
        self.addressL2.setGeometry(350, 570, 750, 50)
        self.addressL2.setText(Company.address)


        modifyBtn = QPushButton('확인', self.w)
        modifyBtn.setFont(QFont(self.basicInfo.font1, 12))
        modifyBtn.setGeometry(980, 630, 120, 40)
        modifyBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')
        modifyBtn.clicked.connect(self.modify)

        stateBtn.clicked.connect(self.state)
        pfBtn.clicked.connect(self.pf)
        infoBtn.clicked.connect(self.info)

    def modify(self):
        company.EmployeeRequestDB.updateCompanyInfo(self.cNameL2.text(),self.employeeL2.text(),self.majorL2.text(),self.salesL2.text(),
                                                    self.companyIntro.toPlainText(),self.webL2.text(),self.addressL2.text())
        self.info()

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
            self.p=company.PofolList.pofolList()
            self.p.show()
            self.hide()

    def info(self):
        self.ci = company.CompanyInfo.CompanyInfo()
        self.ci.show()
        self.hide()
