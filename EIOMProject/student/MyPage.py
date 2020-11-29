import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class MyPage(QWidget):

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
        stateBtn.setGeometry(0, 70, 200, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(200, 70, 200, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('회사', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(400, 70, 200, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        postBtn = QPushButton('취업의뢰', self.w)
        postBtn.setFont(QFont(self.basicInfo.font1, 13))
        postBtn.setGeometry(600, 70, 200, 50)
        postBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        pfBtn = QPushButton('포트폴리오', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(800, 70, 200, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내 정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(1000, 70, 200, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')


        nameL1 = QLabel("이름", self.w)
        nameL1.setFont(QFont(self.basicInfo.font1, 15))
        nameL1.setGeometry(150, 140, 500, 50)

        nameL2 = QLabel("김나은", self.w)
        nameL2.setFont(QFont(self.basicInfo.font1, 15))
        nameL2.setGeometry(350, 140, 500, 50)

        majorL1 = QLabel("학과", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(650, 140, 500, 50)

        majorL2 = QLabel("뉴미디어 소프트웨어과", self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 15))
        majorL2.setGeometry(850, 140, 500, 50)

        emailL1 = QLabel("이메일", self.w)
        emailL1.setFont(QFont(self.basicInfo.font1, 15))
        emailL1.setGeometry(150, 220, 500, 50)

        emailL2 = QLabel("s2019s06@e-mirim.hs.kr", self.w)
        emailL2.setFont(QFont(self.basicInfo.font1, 15))
        emailL2.setGeometry(350, 220, 500, 50)

        majorL1 = QLabel("학년 반", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(650, 220, 500, 50)

        majorL2 = QLabel("2학년 2반", self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 15))
        majorL2.setGeometry(850, 220, 500, 50)

        useLangL1 = QLabel("사용 가능 언어", self.w)
        useLangL1.setFont(QFont(self.basicInfo.font1, 15))
        useLangL1.setGeometry(150, 300, 500, 50)

        useLangL2 = QLabel("java, php, python, c++", self.w)
        useLangL2.setFont(QFont(self.basicInfo.font1, 15))
        useLangL2.setGeometry(350, 300, 500, 50)

        likeCompanyL= QLabel("관심 회사", self.w)
        likeCompanyL.setFont(QFont(self.basicInfo.font1, 15))
        likeCompanyL.setGeometry(150, 380, 500, 50)

        portfolioL = QLabel("포트폴리오", self.w)
        portfolioL.setFont(QFont(self.basicInfo.font1, 15))
        portfolioL.setGeometry(150, 460, 500, 50)

        likeCompanyL1 = QLabel("자기소개서", self.w)
        likeCompanyL1.setFont(QFont(self.basicInfo.font1, 15))
        likeCompanyL1.setGeometry(150, 540, 500, 50)




        modifyBtn=QPushButton('수정',self.w)
        modifyBtn.setFont(QFont(self.basicInfo.font1, 12))
        modifyBtn.setGeometry(800,600,120,40)
        modifyBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

        backBtn = QPushButton('뒤로가기', self.w)
        backBtn.setFont(QFont(self.basicInfo.font1, 12))
        backBtn.setGeometry(950, 600, 120, 40)
        backBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = MyPage()
    sys.exit(app.exec_())
