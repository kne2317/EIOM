import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class PortfolioRequest(QWidget):

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

        allowBtn = QPushButton('승인', self.w)
        allowBtn.setFont(QFont(self.basicInfo.font1, 12))
        allowBtn.setGeometry(850, 150, 120, 40)
        allowBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

        refusalBtn = QPushButton('거절', self.w)
        refusalBtn.setFont(QFont(self.basicInfo.font1, 12))
        refusalBtn.setGeometry(980, 150, 120, 40)
        refusalBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

        contTitle = QLabel('제목 \n', self.w)
        contTitle.setFont(QFont(self.basicInfo.font1, 13))
        contTitle.setGeometry(100, 200, 1000, 90)
        contTitle.setStyleSheet('border-top:1px solid black; border-bottom:1px solid black; ')
        contTitle.setAlignment(QtCore.Qt.AlignCenter)

        writer = QLabel('유병석 선생님 | 2020.12.01', contTitle)
        writer.setFont(QFont(self.basicInfo.font1, 10))
        writer.setGeometry(0, 60, 1000, 20)
        writer.setStyleSheet('color:gray; border:0px;')
        writer.setAlignment(QtCore.Qt.AlignCenter)

        content = QTextBrowser(self.w)
        content.setFont(QFont(self.basicInfo.font1, 12))
        content.setGeometry(100, 300, 1000, 300)
        content.setStyleSheet('border:0px;border-bottom:1px solid black; ')

        backBtn = QPushButton('뒤로가기', self.w)
        backBtn.setFont(QFont(self.basicInfo.font1, 12))
        backBtn.setGeometry(980, 630, 120, 40)
        backBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')



        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = PortfolioRequest()
    sys.exit(app.exec_())
