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



        nameL1 = QLabel("이름", self.w)
        nameL1.setFont(QFont(self.basicInfo.font1, 15))
        nameL1.setGeometry(150, 140, 500, 50)

        nameL2 = QLabel("유병석", self.w)
        nameL2.setFont(QFont(self.basicInfo.font1, 15))
        nameL2.setGeometry(350, 140, 500, 50)

        majorL1 = QLabel("아이디", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 15))
        majorL1.setGeometry(650, 140, 500, 50)

        majorL2 = QLabel("akaz", self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 15))
        majorL2.setGeometry(850, 140, 500, 50)

        emailL1 = QLabel("이메일", self.w)
        emailL1.setFont(QFont(self.basicInfo.font1, 15))
        emailL1.setGeometry(150, 220, 500, 50)

        emailL2 = QLabel("yubs87@e-mirim.hs.kr", self.w)
        emailL2.setFont(QFont(self.basicInfo.font1, 15))
        emailL2.setGeometry(350, 220, 500, 50)


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = MyPage()
    sys.exit(app.exec_())
