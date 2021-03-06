import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
from student.Notice import Notice
import student.Rate
import student.NoticeList
import student.MyPage

class NoticeContent(QWidget):

    def __init__(self, notice=Notice()):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.noticeinfo = notice
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
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

        contTitle=QLabel(self.noticeinfo.title+' \n',self.w)
        contTitle.setFont(QFont(self.basicInfo.font1,13))
        contTitle.setGeometry(100,150,1000,90)
        contTitle.setStyleSheet('border-top:1px solid black; border-bottom:1px solid black; ')
        contTitle.setAlignment(QtCore.Qt.AlignCenter)

        writer=QLabel(self.noticeinfo.writer+' | '+str(self.noticeinfo.date),contTitle)
        writer.setFont(QFont(self.basicInfo.font1, 10))
        writer.setGeometry(0,60,1000,20)
        writer.setStyleSheet('color:gray; border:0px;')
        writer.setAlignment(QtCore.Qt.AlignCenter)


        content=QTextBrowser(self.w)
        st = self.noticeinfo.content.split("\\n")
        for i in st:
            content.append(i)
        content.setFont(QFont(self.basicInfo.font1, 12))
        content.setGeometry(100, 240, 1000, 300)
        content.setStyleSheet('border:0px;border-bottom:1px solid black; padding: 10px; ')


        file = QLabel('첨부파일',self.w)
        file.setFont(QFont(self.basicInfo.font1, 12))
        file.setGeometry(100, 540, 1000, 50)
        file.setStyleSheet('border:0px;border-bottom:1px solid black; ')

        backBtn = QPushButton('뒤로가기', self.w)
        backBtn.setFont(QFont(self.basicInfo.font1, 12))
        backBtn.setGeometry(980, 630, 120, 40)
        backBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

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