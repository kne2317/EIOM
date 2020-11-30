import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
from company.Company import Company


class JoinC2(QWidget):

    def __init__(self, company=Company()):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.initUI()
        self.company = company

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

        addInput = QLineEdit(self.w)
        addInput.setGeometry(350, 180, 500, 50)
        addInput.setFont(QFont(self.basicInfo.font1, 12))
        addInput.setPlaceholderText('주소 입력')

        annualSalesInput = QLineEdit(self.w)
        annualSalesInput.setGeometry(350, 250, 500, 50)
        annualSalesInput.setFont(QFont(self.basicInfo.font1, 12))
        annualSalesInput.setPlaceholderText('연매출 입력')

        webInput = QLineEdit(self.w)
        webInput.setGeometry(350, 320, 500, 50)
        webInput.setFont(QFont(self.basicInfo.font1, 12))
        webInput.setPlaceholderText('웹사이트 주소 입력')

        nameInput = QLineEdit(self.w)
        nameInput.setGeometry(350, 390, 500, 50)
        nameInput.setFont(QFont(self.basicInfo.font1, 12))
        nameInput.setPlaceholderText('담당자 이름 입력')

        mailInput = QLineEdit(self.w)
        mailInput.setGeometry(350, 460, 500, 50)
        mailInput.setFont(QFont(self.basicInfo.font1, 12))
        mailInput.setPlaceholderText('담당자 e-mail 입력')

        phInput = QLineEdit(self.w)
        phInput.setGeometry(350, 530, 500, 50)
        phInput.setFont(QFont(self.basicInfo.font1, 12))
        phInput.setPlaceholderText('담당자 연락처 입력')

        joinBtn = QPushButton('JOIN', self.w)
        joinBtn.setFont(QFont(self.basicInfo.font1, 15))
        joinBtn.setGeometry(350, 600, 500, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = JoinS()
    sys.exit(app.exec_())
