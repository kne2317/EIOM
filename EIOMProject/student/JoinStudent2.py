import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore


class JoinS2(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        w = QWidget(self)
        self.setWindowTitle('EIOM')
        w.resize(1200, 700)
        self.move(400, 100)
        self.setFixedSize(1200, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/join_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - JOIN [ Student ]", w)
        title.setFont(QFont('Candara', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 45, 1000, 50)

        major = QComboBox(w)
        major.move(280,200)
        major.setFixedHeight(50)
        major.setFixedWidth(330)
        major.setFont(QFont('맑은 고딕', 13))
        major.addItem('뉴미디어 소프트웨어과')
        major.addItem('뉴미디어 웹솔루션과')
        major.addItem('뉴미디어 디자인과')

        grade = QComboBox(w)
        grade.move(630, 200)
        grade.setFixedHeight(50)
        grade.setFixedWidth(130)
        grade.setFont(QFont('맑은 고딕', 13))
        grade.addItem('1학년')
        grade.addItem('2학년')
        grade.addItem('3학년')

        ban = QComboBox(w)
        ban.move(780, 200)
        ban.setFixedHeight(50)
        ban.setFixedWidth(130)
        ban.setFont(QFont('맑은 고딕', 13))

        ban.addItem('1반')
        ban.addItem('2반')
        ban.addItem('3반')
        ban.addItem('4반')
        ban.addItem('5반')
        ban.addItem('6반')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = JoinS2()
    sys.exit(app.exec_())


