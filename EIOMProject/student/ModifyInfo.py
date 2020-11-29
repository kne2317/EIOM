import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class ModifyInfo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.basicInfo = BasicInfo()

        w = QWidget(self)
        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
        w.setPalette(palette)

        w.setLayout(layout)

        nameL = QLabel("이름", w)
        nameL.setFont(QFont('맑은 고딕', 15))
        nameL.setGeometry(100, 150, 100, 50)

        name = QLineEdit('김나은', w)

        major = QComboBox(w)
        major.move(280, 200)
        major.setFixedHeight(50)
        major.setFixedWidth(330)
        major.setFont(QFont(self.basicInfo.font1, 13))
        major.addItem('뉴미디어 소프트웨어과')
        major.addItem('뉴미디어 웹솔루션과')
        major.addItem('뉴미디어 디자인과')

        grade = QComboBox(w)
        grade.move(630, 200)
        grade.setFixedHeight(50)
        grade.setFixedWidth(130)
        grade.setFont(QFont(self.basicInfo.font1, 13))
        grade.addItem('1학년')
        grade.addItem('2학년')
        grade.addItem('3학년')

        ban = QComboBox(w)
        ban.move(780, 200)
        ban.setFixedHeight(50)
        ban.setFixedWidth(130)
        ban.setFont(QFont(self.basicInfo.font1, 13))

        ban.addItem('1반')
        ban.addItem('2반')
        ban.addItem('3반')
        ban.addItem('4반')
        ban.addItem('5반')
        ban.addItem('6반')

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(w)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = ModifyInfo()
    sys.exit(app.exec_())
