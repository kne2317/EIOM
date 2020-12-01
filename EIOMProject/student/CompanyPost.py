import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
from student.Company import Company
import student.CompanyList

class CompanyPost(QWidget):

    def __init__(self, company=Company()):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.companyInfo=company
        self.initUI()

    def initUI(self):
        if self.companyInfo.major==None:
            self.companyInfo.major='-'
        if self.companyInfo.introduce==None:
            self.companyInfo.introduce
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


        cNameL1=QLabel("기업명",self.w)
        cNameL1.setFont(QFont(self.basicInfo.font1,15))
        cNameL1.setGeometry(150,160,500,50)

        cNameL2 = QLabel(self.companyInfo.companyname, self.w)
        cNameL2.setFont(QFont(self.basicInfo.font1, 15))
        cNameL2.setGeometry(350, 160, 500, 50)

        employeeL1 = QLabel("사원수", self.w)
        employeeL1.setFont(QFont(self.basicInfo.font1, 15))
        employeeL1.setGeometry(650, 160, 500, 50)


        employeeL2 = QLabel(str(self.companyInfo.employees_num), self.w)
        employeeL2.setFont(QFont(self.basicInfo.font1, 15))
        employeeL2.setGeometry(850, 160, 500, 50)

        majorL1 = QLabel("분야", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(150, 240, 500, 50)

        majorL2 = QLabel(self.companyInfo.major, self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 15))
        majorL2.setGeometry(350, 240, 500, 50)

        salesL1 = QLabel("연매출", self.w)
        salesL1.setFont(QFont(self.basicInfo.font1, 15))
        salesL1.setGeometry(650, 240, 500, 50)

        salesL2 = QLabel(self.companyInfo.annualsales, self.w)
        salesL2.setFont(QFont(self.basicInfo.font1, 15))
        salesL2.setGeometry(850, 240, 500, 50)

        companyIntroL = QLabel("기업소개", self.w)
        companyIntroL.setFont(QFont(self.basicInfo.font1, 15))
        companyIntroL.setGeometry(150, 320, 500, 50)

        companyIntro = QTextBrowser(self.w)
        companyIntro.setFont(QFont(self.basicInfo.font1, 12))
        companyIntro.setGeometry(350, 330, 720, 130)
        companyIntro.setText(self.companyInfo.introduce)
        companyIntro.setStyleSheet('border:0px;')

        webL1 = QLabel("웹사이트 ", self.w)
        webL1.setFont(QFont(self.basicInfo.font1, 15))
        webL1.setGeometry(150, 490, 500, 50)

        webL2 = QLabel(self.companyInfo.web, self.w)
        webL2.setFont(QFont(self.basicInfo.font1, 15))
        webL2.setGeometry(350, 490, 500, 50)

        addressL1 = QLabel("주소", self.w)
        addressL1.setFont(QFont(self.basicInfo.font1, 15))
        addressL1.setGeometry(150, 570, 500, 50)

        addressL2 = QLabel(self.companyInfo.address, self.w)
        addressL2.setFont(QFont(self.basicInfo.font1, 15))
        addressL2.setGeometry(350, 570, 1000, 50)

        likeBtn = QPushButton('관심회사', self.w)
        likeBtn.setFont(QFont(self.basicInfo.font1, 12))
        likeBtn.setGeometry(810, 630, 120, 40)
        likeBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')
        likeBtn.clicked.connect(self.like)

        backBtn = QPushButton('뒤로가기', self.w)
        backBtn.setFont(QFont(self.basicInfo.font1, 12))
        backBtn.setGeometry(950, 630, 120, 40)
        backBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')
        backBtn.clicked.connect(self.back)

    def like(self):
        print('관심회사 등록')
    def back(self):
        self.b=student.CompanyList.CompanyList()
        self.b.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = CompanyPost()
    ex.show()
    sys.exit(app.exec_())