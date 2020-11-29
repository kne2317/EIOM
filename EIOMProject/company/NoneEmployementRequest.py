import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class NoneEmployementRequest(QWidget):

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
        stateBtn.setGeometry(0, 70, self.basicInfo.WindowWidth/3, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(self.basicInfo.WindowWidth/3*1, 70, self.basicInfo.WindowWidth/3, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('회사', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(self.basicInfo.WindowWidth/3*2, 70, self.basicInfo.WindowWidth/3, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noRequest = QLabel("귀하는 취업 의뢰 내역이 존재하지 않습니다.",self.w)
        noRequest.setFont(QFont(self.basicInfo.font1,13))
        noRequest.setGeometry(0,300,1200,100)
        noRequest.setAlignment(QtCore.Qt.AlignCenter)

        requestBtn = QPushButton('취업 의뢰하기', self.w)
        requestBtn.setFont(QFont(self.basicInfo.font1, 15))
        requestBtn.setGeometry(100, 600, 1000, 50)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = NoneEmployementRequest()
    sys.exit(app.exec_())