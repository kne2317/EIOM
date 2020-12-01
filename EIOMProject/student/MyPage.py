import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
from student.Student import Student
import student.Student
import student.Rate
import student.NoticeList
import student.MyPage
import student.ModifyInfo
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
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/background.png")))
        self.setPalette(palette)

        self.w.setLayout(layout)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 10, 1000, 50)

        stateBtn = QPushButton('통계', self.w)
        stateBtn.setFont(QFont(self.basicInfo.font1, 13))
        stateBtn.setGeometry(0, 70, 240, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(240, 70, 240, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('회사', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(480, 70, 240, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        postBtn = QPushButton('취업의뢰', self.w)
        postBtn.setFont(QFont(self.basicInfo.font1, 13))
        postBtn.setGeometry(720, 70, 240, 50)
        postBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내 정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(960, 70, 240, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        stateBtn.clicked.connect(self.state)
        noticeBtn.clicked.connect(self.notice)
        companyBtn.clicked.connect(self.company)
        postBtn.clicked.connect(self.post)
        infoBtn.clicked.connect(self.info)


        nameL1 = QLabel("이름", self.w)
        nameL1.setFont(QFont(self.basicInfo.font1, 15))
        nameL1.setGeometry(150, 140, 500, 50)

        nameL2 = QLabel("김나은", self.w)
        nameL2.setFont(QFont(self.basicInfo.font1, 15))
        nameL2.setGeometry(350, 140, 500, 50)
        nameL2.setText(Student.name)

        majorL1 = QLabel("학과", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(650, 140, 500, 50)

        majorL2 = QLabel("뉴미디어 소프트웨어과", self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 15))
        majorL2.setGeometry(850, 140, 500, 50)
        majorL2.setText(Student.major)

        emailL1 = QLabel("이메일", self.w)
        emailL1.setFont(QFont(self.basicInfo.font1, 15))
        emailL1.setGeometry(150, 220, 500, 50)

        emailL2 = QLabel("s2019s06@e-mirim.hs.kr", self.w)
        emailL2.setFont(QFont(self.basicInfo.font1, 15))
        emailL2.setGeometry(350, 220, 500, 50)
        emailL2.setText(Student.email)

        majorL1 = QLabel("학년 반", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(650, 220, 500, 50)

        majorL2 = QLabel("2학년 2반", self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 15))
        majorL2.setGeometry(850, 220, 500, 50)
        majorL2.setText(str(Student.grade)+"학년  "+str(Student.class_)+"반")

        useLangL1 = QLabel("사용 가능 언어", self.w)
        useLangL1.setFont(QFont(self.basicInfo.font1, 15))
        useLangL1.setGeometry(150, 300, 500, 50)

        useLangL2 = QLabel("java, php, python, c++", self.w)
        useLangL2.setFont(QFont(self.basicInfo.font1, 15))
        useLangL2.setGeometry(350, 300, 500, 50)
        useLangL2.setText(student.Student.uselang())

        likeCompanyL= QLabel("관심 회사", self.w)
        likeCompanyL.setFont(QFont(self.basicInfo.font1, 15))
        likeCompanyL.setGeometry(150, 380, 500, 50)

        portfolioL = QLabel("포트폴리오", self.w)
        portfolioL.setFont(QFont(self.basicInfo.font1, 15))
        portfolioL.setGeometry(150, 460, 500, 50)

        portfolioL2 = QLabel("포트폴리오", self.w)
        portfolioL2.setFont(QFont(self.basicInfo.font1, 14))
        portfolioL2.setGeometry(300, 460, 500, 50)
        portfolioL2.setText(Student.portfolio)

        introduceL1 = QLabel("자기소개서", self.w)
        introduceL1.setFont(QFont(self.basicInfo.font1, 15))
        introduceL1.setGeometry(150, 540, 500, 50)

        introduceL2= QLabel("자기소개서", self.w)
        introduceL2.setFont(QFont(self.basicInfo.font1, 15))
        introduceL2.setGeometry(300, 540, 500, 50)
        introduceL2.setText(Student.introduce)

        modifyBtn=QPushButton('수정',self.w)
        modifyBtn.setFont(QFont(self.basicInfo.font1, 12))
        modifyBtn.setGeometry(950,600,120,40)
        modifyBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')
        modifyBtn.clicked.connect(self.modify)

    def modify(self):
        self.mo=student.ModifyInfo.ModifyInfo()
        self.mo.show()
        self.hide()
    def state(self):
        self.sr = student.Rate.sRate()
        self.sr.show()
        self.hide()

    def notice(self):
        self.nl = student.NoticeList.noticeList()
        self.nl.show()
        self.hide()

    def company(self):
        print('아직')

    def post(self):
        print('아직')

    def info(self):
        self.mp = student.MyPage.MyPage()
        self.mp.show()
        self.hide()