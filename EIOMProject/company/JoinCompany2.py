import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
from Join import CompanyJoin
from company.Company import Company
import main


class JoinC2(QWidget):

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        self.w.setWindowTitle('EIOM')
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

        self.addInput = QLineEdit(self.w)
        self.addInput.setGeometry(350, 180, 500, 50)
        self.addInput.setFont(QFont(self.basicInfo.font1, 12))
        self.addInput.setPlaceholderText('주소 입력')

        self.annualSalesInput = QLineEdit(self.w)
        self.annualSalesInput.setGeometry(350, 250, 500, 50)
        self.annualSalesInput.setFont(QFont(self.basicInfo.font1, 12))
        self.annualSalesInput.setPlaceholderText('연매출 입력')

        self.webInput = QLineEdit(self.w)
        self.webInput.setGeometry(350, 320, 500, 50)
        self.webInput.setFont(QFont(self.basicInfo.font1, 12))
        self.webInput.setPlaceholderText('웹사이트 주소 입력')

        self.nameInput = QLineEdit(self.w)
        self.nameInput.setGeometry(350, 390, 500, 50)
        self.nameInput.setFont(QFont(self.basicInfo.font1, 12))
        self.nameInput.setPlaceholderText('담당자 이름 입력')

        self.emailInput = QLineEdit(self.w)
        self.emailInput.setGeometry(350, 460, 500, 50)
        self.emailInput.setFont(QFont(self.basicInfo.font1, 12))
        self.emailInput.setPlaceholderText('담당자 이메일 입력')

        self.phInput = QLineEdit(self.w)
        self.phInput.setGeometry(350, 530, 500, 50)
        self.phInput.setFont(QFont(self.basicInfo.font1, 12))
        self.phInput.setPlaceholderText('담당자 연락처 입력')

        joinBtn = QPushButton('JOIN', self.w)
        joinBtn.setFont(QFont(self.basicInfo.font1, 15))
        joinBtn.setGeometry(350, 600, 500, 50)
        joinBtn.clicked.connect(self.goNextPage)


    def goNextPage(self):
        # 위치 지정
        if (len(self.addInput.text()) > 0 \
                and len(self.annualSalesInput.text()) > 0 \
                and len(self.webInput.text()) > 0 \
                and len(self.nameInput.text()) > 0 \
                and len(self.emailInput.text()) > 0 \
                and len(self.phInput.text()) > 0):


            Company.address = self.addInput.text()
            Company.annualsale = self.annualSalesInput.text()
            Company.web = self.webInput.text()
            Company.manager_name = self.nameInput.text()
            Company.email = self.emailInput.text()
            Company.manager_ph = self.phInput.text()

            if CompanyJoin():

                print("회원가입에 성공하였습니다.")

                self.nextPage = main.Main()
                self.hide()

                self.nextPage.show()
            else:
                print("회원가입이 실패하였습니다.")

        else:
            print("입력되지 않은 항목이 존재합니다")