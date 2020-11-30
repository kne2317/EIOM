import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo, BasicDB
from student.JoinStudent2 import JoinS2
from student.Student import Student


class JoinS(QWidget):

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.initUI()
        self.idOverlapChecked = False

    def initUI(self):

        layout = QVBoxLayout()
        self.w.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/join_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - JOIN [ Student ]", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 45, 1000, 50)

        self.nameInput = QLineEdit(self.w)
        self.nameInput.setGeometry(350, 200, 500, 50)
        self.nameInput.setFont(QFont(self.basicInfo.font1, 12))
        self.nameInput.setPlaceholderText('이름 입력')

        self.idInput = QLineEdit(self.w)
        self.idInput.setGeometry(350, 270, 380, 50)
        self.idInput.setFont(QFont(self.basicInfo.font1, 12))
        self.idInput.setPlaceholderText('아이디 입력')

        idCheck = QPushButton('중복체크', self.w)
        idCheck.setFont(QFont(self.basicInfo.font1, 12))
        idCheck.setGeometry(750, 270, 100, 50)
        idCheck.clicked.connect(self.idOverlapCheck)

        self.pwInput = QLineEdit(self.w)
        self.pwInput.setEchoMode(QLineEdit.Password)
        self.pwInput.setGeometry(350, 340, 500, 50)
        self.pwInput.setFont(QFont(self.basicInfo.font1, 12))
        self.pwInput.setPlaceholderText('비밀번호 입력')

        self.pwCheck = QLineEdit(self.w)
        self.pwCheck.setEchoMode(QLineEdit.Password)
        self.pwCheck.setGeometry(350, 410, 500, 50)
        self.pwCheck.setFont(QFont(self.basicInfo.font1, 12))
        self.pwCheck.setPlaceholderText('비밀번호 확인')

        self.mailInput = QLineEdit(self.w)
        self.mailInput.setGeometry(350, 480, 500, 50)
        self.mailInput.setFont(QFont(self.basicInfo.font1, 12))
        self.mailInput.setPlaceholderText('e-mail 입력')

        nextBtn = QPushButton('NEXT>>', self.w)
        nextBtn.setFont(QFont(self.basicInfo.font1, 15))
        nextBtn.setGeometry(350, 550, 500, 50)
        nextBtn.clicked.connect(self.goNextPage)



    def goNextPage(self):
        # 위치 지정
        if(len(self.nameInput.text()) > 0 \
            and len(self.idInput.text()) > 0 \
            and len(self.pwInput.text()) > 0 \
            and len(self.mailInput.text()) > 0):
            if  self.idOverlapChecked:

                Student.name = self.nameInput.text()
                Student.ID = self.idInput.text()
                Student.password = self.pwInput.text()
                Student.email = self.mailInput.text()

                self.nextPage = JoinS2()
                geo = self.geometry()
                titlebar_height = QApplication.style().pixelMetric(QStyle.PM_TitleBarHeight)
                self.nextPage.move(geo.x(), geo.y() - titlebar_height)
                self.hide()

                self.nextPage.show()
            else:
                print("아이디 중복 체크를 해주시기 바랍니다.")
        else:
            print("입력되지 않은 항목이 존재합니다")


    def idOverlapCheck(self):

        try:
            if len(self.idInput.text()) > 0:
                basicDB = BasicDB()
                conn = basicDB.conn
                curs = conn.cursor()

                sql = "select EXISTS (select * from student where id='"+self.idInput.text()+"') as success;"
                curs.execute(sql)

                result = curs.fetchall()
                if result[0][0] == 1:
                    print("중복되는 아이디입니다.")
                    self.idOverlapChecked = False
                elif result[0][0] == 0:
                    print("사용 가능한 아이디입니다.")
                    self.idOverlapChecked = True

                conn.close()
            else:
                print("아이디를 입력하십시오.")
                self.idOverlapChecked = False
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = JoinS()
    ex.show()
    app.exec_()