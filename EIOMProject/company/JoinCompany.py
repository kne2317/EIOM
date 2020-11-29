import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class JoinC(QWidget):

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
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/join_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - JOIN [ Company ]", self.w)
        title.setFont(QFont('impact', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 45, 1000, 50)

        nameInput = QLineEdit(self.w)
        nameInput.setGeometry(350, 230, 380, 50)
        nameInput.setFont(QFont('맑은 고딕', 12))
        nameInput.setPlaceholderText('회사명 입력')

        nameCheck = QPushButton('중복체크', self.w)
        nameCheck.setFont(QFont('맑은 고딕', 12))
        nameCheck.setGeometry(750, 230, 100, 50)

        idInput = QLineEdit(self.w)
        idInput.setGeometry(350, 300, 380, 50)
        idInput.setFont(QFont('맑은 고딕', 12))
        idInput.setPlaceholderText('아이디 입력')

        idCheck = QPushButton('중복체크', self.w)
        idCheck.setFont(QFont('맑은 고딕', 12))
        idCheck.setGeometry(750, 300, 100, 50)

        pwInput = QLineEdit(self.w)
        pwInput.setEchoMode(QLineEdit.Password)
        pwInput.setGeometry(350, 370, 500, 50)
        pwInput.setFont(QFont('맑은 고딕', 12))
        pwInput.setPlaceholderText('비밀번호 입력')

        pwInput = QLineEdit(self.w)
        pwInput.setEchoMode(QLineEdit.Password)
        pwInput.setGeometry(350, 440, 500, 50)
        pwInput.setFont(QFont('맑은 고딕', 12))
        pwInput.setPlaceholderText('비밀번호 확인')

        nextBtn = QPushButton('NEXT>>', self.w)
        nextBtn.setFont(QFont('맑은 고딕', 15))
        nextBtn.setGeometry(350, 520, 500, 50)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = JoinC()
    sys.exit(app.exec_())
