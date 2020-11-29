import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class JoinS(QWidget):

    def __init__(self):
        super().__init__()
        self.w = QWidget(self)
        self.initUI()

    def initUI(self):
        self.basicInfo = BasicInfo()

        layout = QVBoxLayout()
        self.w.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/join_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - JOIN [ Student ]", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 45, 1000, 50)

        nameInput = QLineEdit(self.w)
        nameInput.setGeometry(350, 200, 500, 50)
        nameInput.setFont(QFont(self.basicInfo.font1, 12))
        nameInput.setPlaceholderText('이름 입력')

        idInput = QLineEdit(self.w)
        idInput.setGeometry(350, 270, 380, 50)
        idInput.setFont(QFont(self.basicInfo.font1, 12))
        idInput.setPlaceholderText('아이디 입력')

        idCheck = QPushButton('중복체크', self.w)
        idCheck.setFont(QFont(self.basicInfo.font1, 12))
        idCheck.setGeometry(750, 270, 100, 50)

        pwInput = QLineEdit(self.w)
        pwInput.setEchoMode(QLineEdit.Password)
        pwInput.setGeometry(350, 340, 500, 50)
        pwInput.setFont(QFont(self.basicInfo.font1, 12))
        pwInput.setPlaceholderText('비밀번호 입력')

        pwInput = QLineEdit(self.w)
        pwInput.setEchoMode(QLineEdit.Password)
        pwInput.setGeometry(350, 410, 500, 50)
        pwInput.setFont(QFont(self.basicInfo.font1, 12))
        pwInput.setPlaceholderText('비밀번호 확인')

        mailInput = QLineEdit(self.w)
        mailInput.setGeometry(350, 480, 500, 50)
        mailInput.setFont(QFont(self.basicInfo.font1, 12))
        mailInput.setPlaceholderText('e-mail 입력')

        nextBtn = QPushButton('NEXT>>', self.w)
        nextBtn.setFont(QFont(self.basicInfo.font1, 15))
        nextBtn.setGeometry(350, 550, 500, 50)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = JoinS()
    sys.exit(app.exec_())
