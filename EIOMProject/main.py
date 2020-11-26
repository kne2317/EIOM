import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore, QtGui


class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        w = QWidget(self)
        layout = QVBoxLayout()
        w.setWindowTitle('EIOM')
        w.resize(1200, 700)
        self.move(400,100)
        self.setFixedSize(1200,700)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/login_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM", w)
        title.setFont(QFont('Candara', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 80, 1000, 400)

        title2 = QLabel("Employment Information Of Mirim", w)
        title2.setFont(QFont('Candara', 25))
        title2.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title2)
        title2.setGeometry(100, 80, 1000, 500)

        idInput = QLineEdit(w)
        idInput.setGeometry(350,420,350,50)
        idInput.setFont(QFont('맑은 고딕',12))
        idInput.setPlaceholderText('아이디를 입력하시오')

        pwInput = QLineEdit(w)
        pwInput.setEchoMode(QLineEdit.Password)
        pwInput.setGeometry(350, 490, 350, 50)
        pwInput.setFont(QFont('맑은 고딕', 12))
        pwInput.setPlaceholderText('패스워드를 입력하시오')


        loginBtn = QPushButton('LOGIN', w)
        loginBtn.setFont(QFont('맑은 고딕',15))
        loginBtn.setGeometry(720,418,130,125)

        student = QRadioButton('학생',w)
        teacher = QRadioButton('선생님',w)
        company = QRadioButton('회사',w)

        student.setGeometry(350,520,100,100)
        teacher.setGeometry(450,520,100,100)
        company.setGeometry(580,520,100,100)

        student.setFont(QFont('맑은 고딕', 12))
        teacher.setFont(QFont('맑은 고딕', 12))
        company.setFont(QFont('맑은 고딕', 12))

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor(144, 112, 144))

        joinBtn = QPushButton('회원가입', w)
        joinBtn.setFont(QFont('맑은 고딕', 13))
        joinBtn.setGeometry(735, 540, 100, 50)
        joinBtn.setStyleSheet('background-color: rgb(0,0,0,0); ')

        '''
        searchBtn = QPushButton('ID / PW 찾기', w)
        searchBtn.setFont(QFont('맑은 고딕', 13))
        searchBtn.setGeometry(550, 600, 120, 50)
        searchBtn.setStyleSheet('background-color: rgb(0,0,0,0); ')
        '''

        self.show()



    def groupboxRadFunction(self):
        if self.student.isChecked():
            print("학생")
        elif self.teacher.isChecked():
            print("선생님")
        elif self.company.isChecked():
            print("회사")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
