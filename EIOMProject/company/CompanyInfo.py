import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class CompanyInfo(QWidget):

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

        stateBtn = QPushButton('통계', self.w)
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

        cNameL1=QLabel("기업명",self.w)
        cNameL1.setFont(QFont(self.basicInfo.font1,15))
        cNameL1.setGeometry(150,160,500,50)

        cNameL2 = QLabel("연지 소프트", self.w)
        cNameL2.setFont(QFont(self.basicInfo.font1, 15))
        cNameL2.setGeometry(350, 160, 500, 50)

        employeeL1 = QLabel("사원수", self.w)
        employeeL1.setFont(QFont(self.basicInfo.font1, 15))
        employeeL1.setGeometry(650, 160, 500, 50)

        employeeL2 = QLabel("10", self.w)
        employeeL2.setFont(QFont(self.basicInfo.font1, 15))
        employeeL2.setGeometry(850, 160, 500, 50)

        majorL1 = QLabel("분야", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(150, 240, 500, 50)

        majorL2 = QLabel("개발", self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 15))
        majorL2.setGeometry(350, 240, 500, 50)

        salesL1 = QLabel("연매출", self.w)
        salesL1.setFont(QFont(self.basicInfo.font1, 15))
        salesL1.setGeometry(650, 240, 500, 50)

        salesL2 = QLabel("10억", self.w)
        salesL2.setFont(QFont(self.basicInfo.font1, 15))
        salesL2.setGeometry(850, 240, 500, 50)

        companyIntroL = QLabel("기업소개", self.w)
        companyIntroL.setFont(QFont(self.basicInfo.font1, 15))
        companyIntroL.setGeometry(150, 320, 500, 50)

        companyIntro = QTextBrowser(self.w)
        companyIntro.setFont(QFont(self.basicInfo.font1, 12))
        companyIntro.setGeometry(270, 330, 800, 130)

        webL1 = QLabel("웹사이트 ", self.w)
        webL1.setFont(QFont(self.basicInfo.font1, 15))
        webL1.setGeometry(150, 490, 500, 50)

        webL2 = QLabel("www.e-mirim.hs.kr", self.w)
        webL2.setFont(QFont(self.basicInfo.font1, 15))
        webL2.setGeometry(350, 490, 500, 50)

        addressL1 = QLabel("주소", self.w)
        addressL1.setFont(QFont(self.basicInfo.font1, 15))
        addressL1.setGeometry(150, 570, 500, 50)

        addressL2 = QLabel("남양주시 화도읍", self.w)
        addressL2.setFont(QFont(self.basicInfo.font1, 15))
        addressL2.setGeometry(350, 570, 1000, 50)


        modifyBtn = QPushButton('수정', self.w)
        modifyBtn.setFont(QFont(self.basicInfo.font1, 12))
        modifyBtn.setGeometry(950, 630, 120, 40)
        modifyBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = CompanyInfo()
    sys.exit(app.exec_())
