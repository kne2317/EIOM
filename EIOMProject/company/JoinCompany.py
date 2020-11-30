import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo, BasicDB
from Join import CompanyJoin
from company.Company import Company
from company.JoinCompany2 import JoinC2


class JoinC(QWidget):

    def __init__(self):
        super().__init__()
        self.company = Company()
        self.idOverlapChecked = False
        self.CompanyNameOverlapChecked = False
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/join_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - JOIN [ Company ]", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 45, 1000, 50)

        self.nameInput = QLineEdit(self.w)
        self.nameInput.setGeometry(350, 230, 380, 50)
        self.nameInput.setFont(QFont(self.basicInfo.font1, 12))
        self.nameInput.setPlaceholderText('회사명 입력')

        nameCheck = QPushButton('중복체크', self.w)
        nameCheck.setFont(QFont(self.basicInfo.font1, 12))
        nameCheck.setGeometry(750, 230, 100, 50)
        nameCheck.clicked.connect(self.nameOverlapCheck)

        self.idInput = QLineEdit(self.w)
        self.idInput.setGeometry(350, 300, 380, 50)
        self.idInput.setFont(QFont(self.basicInfo.font1, 12))
        self.idInput.setPlaceholderText('아이디 입력')

        idCheck = QPushButton('중복체크', self.w)
        idCheck.setFont(QFont(self.basicInfo.font1, 12))
        idCheck.setGeometry(750, 300, 100, 50)
        idCheck.clicked.connect(self.idOverlapCheck)

        self.pwInput = QLineEdit(self.w)
        self.pwInput.setEchoMode(QLineEdit.Password)
        self.pwInput.setGeometry(350, 370, 500, 50)
        self.pwInput.setFont(QFont(self.basicInfo.font1, 12))
        self.pwInput.setPlaceholderText('비밀번호 입력')

        self.pwCheck = QLineEdit(self.w)
        self.pwCheck.setEchoMode(QLineEdit.Password)
        self.pwCheck.setGeometry(350, 440, 500, 50)
        self.pwCheck.setFont(QFont(self.basicInfo.font1, 12))
        self.pwCheck.setPlaceholderText('비밀번호 확인')

        nextBtn = QPushButton('NEXT>>', self.w)
        nextBtn.setFont(QFont(self.basicInfo.font1, 15))
        nextBtn.setGeometry(350, 520, 500, 50)
        nextBtn.clicked.connect(self.goNextPage)

    def goNextPage(self):
        # 위치 지정
        if (len(self.nameInput.text()) > 0 \
                and len(self.idInput.text()) > 0 \
                and len(self.pwInput.text()) > 0):

            if self.idOverlapChecked:
                if self.CompanyNameOverlapChecked:


                    self.company.setCompanyname(self.nameInput.text())
                    self.company.setID(self.idInput.text())
                    self.company.setPassword(self.pwInput.text())

                    self.nextPage = JoinC2(self.company)
                    geo = self.geometry()
                    titlebar_height = QApplication.style().pixelMetric(QStyle.PM_TitleBarHeight)
                    self.nextPage.move(geo.x(), geo.y() - titlebar_height)
                    self.hide()

                    self.nextPage.show()

                else:
                    print("회사명 중복 체크를 해주시기 바랍니다.")
            else:
                print("아이디 중복 체크를 해주시기 바랍니다.")
        else:
            print("입력되지 않은 항목이 존재합니다")

    def idOverlapCheck(self):

        if len(self.idInput.text()) > 0:
            basicDB = BasicDB()
            conn = basicDB.conn
            curs = conn.cursor()

            sql = "select EXISTS (select * from company where id='" + self.idInput.text() + "') as success;"
            curs.execute(sql)

            result = curs.fetchall()
            conn.close()
            if result[0][0] == 1:
                print("중복되는 아이디입니다.")
                self.idOverlapChecked = False
            elif result[0][0] == 0:
                print("사용 가능한 아이디입니다.")
                self.idOverlapChecked = True

        else:
            print("아이디를 입력하십시오.")
            self.idOverlapChecked = False

    def nameOverlapCheck(self):

        if len(self.nameInput.text()) > 0:
            basicDB = BasicDB()
            conn = basicDB.conn
            curs = conn.cursor()

            sql = "select EXISTS (select * from company where companyname='" + self.idInput.text() + "') as success;"
            curs.execute(sql)

            result = curs.fetchall()
            conn.close()
            if result[0][0] == 1:
                print("이미 가입된 회사명입니다.")
                self.CompanyNameOverlapChecked = False
            elif result[0][0] == 0:
                print("가입 가능한 회사명입니다.")
                self.CompanyNameOverlapChecked = True

        else:
            print("회사명을 입력하십시오.")
            self.CompanyNameOverlapChecked = False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = JoinC()
    ex.show()
    app.exec_()
