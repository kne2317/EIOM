import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore, QtGui
from BasicInfo import BasicInfo, BasicDB
import Login
from JoinSelect import JoinSelect
from student.Rate import sRate
from teacher.Rate import tRate
from company.Company import Company
from company.NoneEmployementRequest import NoneEmployementRequest
from company.CompanyEmploymentRequest import CompanyEmploymentRequest

class Main(QWidget):

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
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/login_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont('impact', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 80, 1000, 400)

        title2 = QLabel("Employment Information Of Mirim", self.w)
        title2.setFont(QFont('impact', 25))
        title2.setAlignment(QtCore.Qt.AlignCenter)
        title2.setGeometry(100, 80, 1000, 500)

        self.idInput = QLineEdit(self.w)
        self.idInput.setGeometry(350, 420, 350, 50)
        self.idInput.setFont(QFont('맑은 고딕', 12))
        self.idInput.setPlaceholderText('아이디를 입력하시오')

        self.pwInput = QLineEdit(self.w)
        self.pwInput.setEchoMode(QLineEdit.Password)
        self.pwInput.setGeometry(350, 490, 350, 50)
        self.pwInput.setFont(QFont('맑은 고딕', 12))
        self.pwInput.setPlaceholderText('패스워드를 입력하시오')

        loginBtn = QPushButton('LOGIN', self.w)
        loginBtn.setFont(QFont('맑은 고딕', 15))
        loginBtn.setGeometry(720, 418, 130, 125)
        loginBtn.clicked.connect(self.login)

        self.student = QRadioButton('학생', self.w)
        self.student.setChecked(True)
        self.teacher = QRadioButton('선생님', self.w)
        self.company = QRadioButton('회사', self.w)

        self.student.setGeometry(350, 520, 100, 100)
        self.teacher.setGeometry(450, 520, 100, 100)
        self.company.setGeometry(580, 520, 100, 100)

        self.student.setFont(QFont('맑은 고딕', 12))
        self.teacher.setFont(QFont('맑은 고딕', 12))
        self.company.setFont(QFont('맑은 고딕', 12))

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor(144, 112, 144))

        joinBtn = QPushButton('회원가입', self.w)
        joinBtn.setFont(QFont('맑은 고딕', 13))
        joinBtn.setGeometry(735, 540, 100, 50)
        joinBtn.setStyleSheet('background-color: rgb(0,0,0,0); ')
        joinBtn.clicked.connect(self.join)

        '''
        searchBtn = QPushButton('ID / PW 찾기', w)
        searchBtn.setFont(QFont('맑은 고딕', 13))
        searchBtn.setGeometry(550, 600, 120, 50)
        searchBtn.setStyleSheet('background-color: rgb(0,0,0,0); ')
        '''

    def login(self):
        # 학생 로그인
        if self.student.isChecked():
            if Login.studentLogin(self.idInput.text(), self.pwInput.text()) == True:
                self.sLogin = sRate()
                self.close()
                self.sLogin.show()
            else:
                msgBox = QMessageBox()
                msgBox.setText("로그인 실패! \n아이디와 비밀번호를 다시 확인해 주세요")
                msgBox.exec_()

        # 교사 로그인
        if self.teacher.isChecked():
            if Login.teacherLogin(self.idInput.text(), self.pwInput.text()) == True:
                self.tLogin = tRate()
                self.close()
                self.tLogin.show()
            else:
                msgBox = QMessageBox()
                msgBox.setText("로그인 실패! \n아이디와 비밀번호를 다시 확인해 주세요")
                msgBox.exec_()

        # 회사 로그인
        # 로그인 후에 정보 반환환
        if self.company.isChecked():
            if Login.companyLogin(self.idInput.text(), self.pwInput.text()) == True:
                self.company = Company()
                if self.company.request_authority==0:
                    self.cLogin = NoneEmployementRequest()
                else:
                    self.cLogin=CompanyEmploymentRequest()
                self.close()
                self.cLogin.show()
            else:
                msgBox = QMessageBox()
                msgBox.setText("로그인 실패! \n아이디와 비밀번호를 다시 확인해 주세요")
                msgBox.exec_()

    def join(self):
        self.joinpage = JoinSelect()
        self.close()
        self.joinpage.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    app.exec_()