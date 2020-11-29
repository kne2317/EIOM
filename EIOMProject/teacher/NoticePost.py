import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


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
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
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

        postBtn = QPushButton('포트폴리오', self.w)
        postBtn.setFont(QFont(self.basicInfo.font1, 13))
        postBtn.setGeometry(self.basicInfo.WindowWidth/5*3, 70, self.basicInfo.WindowWidth/5, 50)
        postBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        pfBtn = QPushButton('내 정보', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(self.basicInfo.WindowWidth/5*4, 70, self.basicInfo.WindowWidth/5, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        titleInput = QLineEdit(self.w)
        titleInput.setFont(QFont(self.basicInfo.font1,13))
        titleInput.setPlaceholderText('제목을 입력하시오.')
        titleInput.setGeometry(100,150,1000,40)

        contentInput = QTextEdit(self.w)
        contentInput.setFont(QFont(self.basicInfo.font1,12))
        contentInput.setPlaceholderText('내용을 입력하시오.')
        contentInput.setGeometry(100,200,1000,380)

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

        cancleBtn = QPushButton('취소', self.w)
        cancleBtn.setFont(QFont(self.basicInfo.font1, 12))
        cancleBtn.setGeometry(630, 650, 110, 30)
        cancleBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

        self.show()

    def show_file_open(self):
        fname = QFileDialog.getOpenFileName()
        self.fileInput.setText(fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = NoticePost()
    sys.exit(app.exec_())
