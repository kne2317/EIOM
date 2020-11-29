import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore


class JoinS(QWidget):

    def __init__(self):
        super().__init__()
        self.w = QWidget(self)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.w.setWindowTitle('EIOM')
        self.w.resize(1200, 700)
        self.move(400, 100)
        self.setFixedSize(1200, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/join_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - JOIN [ Teacher ]", self.w)
        title.setFont(QFont('Candara', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 45, 1000, 50)

        nameInput = QLineEdit(self.w)
        nameInput.setGeometry(350, 180, 500, 50)
        nameInput.setFont(QFont('맑은 고딕', 12))
        nameInput.setPlaceholderText('이름 입력')

        idInput = QLineEdit(self.w)
        idInput.setGeometry(350, 250, 380, 50)
        idInput.setFont(QFont('맑은 고딕', 12))
        idInput.setPlaceholderText('아이디 입력')

        idCheck = QPushButton('중복체크', self.w)
        idCheck.setFont(QFont('맑은 고딕', 12))
        idCheck.setGeometry(750, 250, 100, 50)

        pwInput = QLineEdit(self.w)
        pwInput.setEchoMode(QLineEdit.Password)
        pwInput.setGeometry(350, 320, 500, 50)
        pwInput.setFont(QFont('맑은 고딕', 12))
        pwInput.setPlaceholderText('비밀번호 입력')

        pwInput = QLineEdit(self.w)
        pwInput.setEchoMode(QLineEdit.Password)
        pwInput.setGeometry(350, 390, 500, 50)
        pwInput.setFont(QFont('맑은 고딕', 12))
        pwInput.setPlaceholderText('비밀번호 확인')

        mailInput = QLineEdit(self.w)
        mailInput.setGeometry(350, 460, 500, 50)
        mailInput.setFont(QFont('맑은 고딕', 12))
        mailInput.setPlaceholderText('e-mail 입력')

        codeInput = QLineEdit(self.w)
        codeInput.setGeometry(350, 530, 500, 50)
        codeInput.setFont(QFont('맑은 고딕', 12))
        codeInput.setPlaceholderText('가입코드 입력')

        nextBtn = QPushButton('NEXT>>', self.w)
        nextBtn.setFont(QFont('맑은 고딕', 15))
        nextBtn.setGeometry(350, 600, 500, 50)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = JoinS()
    sys.exit(app.exec_())
