import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
from BasicInfo import BasicInfo


class noticeList(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.w = QWidget(self)
        layout = QVBoxLayout()
        self.setWindowTitle('EIOM')
        self.basicInfo = BasicInfo()
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(400, 100)
        self.setFixedSize(1200, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont('impact', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 10, 1000, 50)

        stateBtn = QPushButton('통계', self.w)
        stateBtn.setFont(QFont('맑은 고딕', 13))
        stateBtn.setGeometry(0, 70, 200, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont('맑은 고딕', 13))
        noticeBtn.setGeometry(200, 70, 200, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('회사', self.w)
        companyBtn.setFont(QFont('맑은 고딕', 13))
        companyBtn.setGeometry(400, 70, 200, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = noticeList()
    sys.exit(app.exec_())
