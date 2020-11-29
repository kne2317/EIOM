import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore


class CompanyInfo(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        w = QWidget(self)
        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
        self.setPalette(palette)

        w.setLayout(layout)

        title = QLabel("EIOM", w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 10, 1000, 50)

        cNameL1=QLabel("기업명",w)
        cNameL1.setFont(QFont(self.basicInfo.font1,15))
        cNameL1.setGeometry(150,100,500,50)

        cNameL2 = QLabel("연지 소프트", w)
        cNameL2.setFont(QFont(self.basicInfo.font1, 15))
        cNameL2.setGeometry(350, 100, 500, 50)

        employeeL1 = QLabel("사원수", w)
        employeeL1.setFont(QFont(self.basicInfo.font1, 15))
        employeeL1.setGeometry(650, 100, 500, 50)

        employeeL2 = QLabel("10", w)
        employeeL2.setFont(QFont(self.basicInfo.font1, 15))
        employeeL2.setGeometry(850, 100, 500, 50)

        majorL1 = QLabel("분야", w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(150, 180, 500, 50)

        majorL2 = QLabel("개발", w)
        majorL2.setFont(QFont(self.basicInfo.font1, 15))
        majorL2.setGeometry(350, 180, 500, 50)

        salesL1 = QLabel("연매출", w)
        salesL1.setFont(QFont(self.basicInfo.font1, 15))
        salesL1.setGeometry(650, 180, 500, 50)

        salesL2 = QLabel("10억", w)
        salesL2.setFont(QFont(self.basicInfo.font1, 15))
        salesL2.setGeometry(850, 180, 500, 50)

        companyIntroL = QLabel("기업소개", w)
        companyIntroL.setFont(QFont(self.basicInfo.font1, 15))
        companyIntroL.setGeometry(150, 260, 500, 50)

        companyIntro = QTextBrowser(w)
        companyIntro.setFont(QFont(self.basicInfo.font1, 12))
        companyIntro.setGeometry(270, 270, 800, 130)

        webL1 = QLabel("웹사이트 ", w)
        webL1.setFont(QFont(self.basicInfo.font1, 15))
        webL1.setGeometry(150, 430, 500, 50)

        webL2 = QLabel("www.e-mirim.hs.kr", w)
        webL2.setFont(QFont(self.basicInfo.font1, 15))
        webL2.setGeometry(350, 430, 500, 50)

        addressL1 = QLabel("주소", w)
        addressL1.setFont(QFont(self.basicInfo.font1, 15))
        addressL1.setGeometry(150, 510, 500, 50)

        addressL2 = QLabel("남양주시 화도읍", w)
        addressL2.setFont(QFont(self.basicInfo.font1, 15))
        addressL2.setGeometry(350, 510, 1000, 50)

        likeCompany=QPushButton('관심회사',w)
        likeCompany.setFont(QFont(self.basicInfo.font1, 12))
        likeCompany.setGeometry(800,600,120,40)
        likeCompany.setStyleSheet('background-color: white; border:1px solid lightgray;')

        backBtn = QPushButton('뒤로가기', w)
        backBtn.setFont(QFont(self.basicInfo.font1, 12))
        backBtn.setGeometry(950, 600, 120, 40)
        backBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = CompanyInfo()
    sys.exit(app.exec_())
