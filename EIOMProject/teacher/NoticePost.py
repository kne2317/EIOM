import os
import sys
from datetime import time

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
from pip._vendor.distlib._backport import shutil

from BasicInfo import BasicInfo, BasicDB
import teacher.Rate
import teacher.MyPage
import teacher.NoticeContent
from teacher import Teacher


class NoticePost(QWidget):

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
        stateBtn.setGeometry(0, 70, self.basicInfo.WindowWidth/5, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(self.basicInfo.WindowWidth/5*1, 70, self.basicInfo.WindowWidth/5, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('취업의뢰', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(self.basicInfo.WindowWidth/5*2, 70, self.basicInfo.WindowWidth/5, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        pfBtn = QPushButton('포트폴리오', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(self.basicInfo.WindowWidth/5*3, 70, self.basicInfo.WindowWidth/5, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내 정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(self.basicInfo.WindowWidth/5*4, 70, self.basicInfo.WindowWidth/5, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        self.titleInput = QLineEdit(self.w)
        self.titleInput.setFont(QFont(self.basicInfo.font1,13))
        self.titleInput.setPlaceholderText('제목을 입력하시오.')
        self.titleInput.setGeometry(100,150,1000,40)

        self.contentInput = QTextEdit(self.w)
        self.contentInput.setFont(QFont(self.basicInfo.font1,12))
        self.contentInput.setPlaceholderText('내용을 입력하시오.')
        self.contentInput.setGeometry(100,200,1000,380)

        fileL = QLabel('첨부 파일', self.w)
        fileL.setFont(QFont(self.basicInfo.font1, 12))
        fileL.move(100, 600)

        self.fileInput = QLineEdit(self.w)
        self.fileInput.setFont(QFont(self.basicInfo.font1, 10))
        self.fileInput.setGeometry(200, 600, 750, 40)

        fileBtn = QPushButton('Browse', self.w)
        fileBtn.setFont(QFont(self.basicInfo.font1, 12))
        fileBtn.setGeometry(990, 600, 110, 40)
        fileBtn.clicked.connect(self.show_file_open)

        okayBtn = QPushButton('확인', self.w)
        okayBtn.setFont(QFont(self.basicInfo.font1, 12))
        okayBtn.setGeometry(480, 650, 110, 30)
        okayBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')
        okayBtn.clicked.connect(self.uploadPost)

        cancleBtn = QPushButton('취소', self.w)
        cancleBtn.setFont(QFont(self.basicInfo.font1, 12))
        cancleBtn.setGeometry(630, 650, 110, 30)
        cancleBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

        stateBtn.clicked.connect(self.state)
        noticeBtn.clicked.connect(self.notice)
        companyBtn.clicked.connect(self.company)
        pfBtn.clicked.connect(self.post)
        infoBtn.clicked.connect(self.info)

    def state(self):
        self.s=teacher.Rate.tRate()
        self.s.show()
        self.hide()
    def notice(self):
        self.n = teacher.NoticeContent.noticeList()
        self.n.show()
        self.hide()
    def company(self):
        print('아직')
    def post(self):
        print('아직')
    def info(self):
        self.i=teacher.MyPage.MyPage()
        self.i.show()
        self.hide()
    def show_file_open(self):
        fname = QFileDialog.getOpenFileName()
        self.fileInput.setText(fname[0])

    def uploadPost(self):
        # 포스트 업로드
        try:
            basicDB = BasicDB()
            conn = basicDB.conn
            curs = conn.cursor()

            # 자소서 추가
            ifile_name = self.fileInput.split('/')[-1]
            ioriginal_path = self.fileInput.replace('/' + ifile_name, '')
            idestination_path = os.path.dirname(os.path.realpath(__file__)) + "\\notice"
            shutil.copyfile(os.path.join(ioriginal_path, ifile_name),
                            os.path.join(idestination_path, ifile_name))

            sql = "INSERT INTO `eiom_db`.`notice` (`writer`, `date`, `title`, `content`, `file`) VALUES ('"+Teacher.name+"', '"+time.strftime('%Y-%m-%d', time.localtime(time.time()))+"', '"+self.titleInput.text()+"', '"+self.contentInput.text()+"', 'ㅁㅇㄴㄹ');"

            curs.execute(sql)
            conn.commit()

            conn.close()

            
            r = teacher.Rate.tRate()
            r.show()
            self.hide()
        except Exception as e:
            print(e)

