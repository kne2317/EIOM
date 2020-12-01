import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class ModifyInfo(QWidget):

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, 1250)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, 700)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/background.png")))
        self.w.setPalette(palette)

        self.w.setLayout(layout)

        title = QLabel("정보수정", self.w)
        title.setFont(QFont(self.basicInfo.font1, 20))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 10, 1000, 50)

        nameL = QLabel("이름", self.w)
        nameL.setFont(QFont(self.basicInfo.font1, 15))
        nameL.setGeometry(100, 150, 100, 40)

        name = QLineEdit('김나은', self.w)
        name.setFont(QFont(self.basicInfo.font1, 13))
        name.setGeometry(250, 150, 250, 40)

        major = QComboBox(self.w)
        major.move(100, 230)
        major.setFixedHeight(50)
        major.setFixedWidth(400)
        major.setFont(QFont(self.basicInfo.font1, 13))
        major.addItem('뉴미디어 소프트웨어과')
        major.addItem('뉴미디어 웹솔루션과')
        major.addItem('뉴미디어 디자인과')

        gradeL = QLabel("학년", self.w)
        gradeL.setFont(QFont(self.basicInfo.font1, 15))
        gradeL.setGeometry(730, 150, 100, 40)

        grade = QComboBox(self.w)
        grade.move(900, 150)
        grade.setFixedHeight(50)
        grade.setFixedWidth(130)
        grade.setFont(QFont(self.basicInfo.font1, 13))
        grade.addItem('1학년')
        grade.addItem('2학년')
        grade.addItem('3학년')

        banL = QLabel("반", self.w)
        banL.setFont(QFont(self.basicInfo.font1, 15))
        banL.setGeometry(730, 230, 100, 40)

        ban = QComboBox(self.w)
        ban.move(900, 230)
        ban.setFixedHeight(50)
        ban.setFixedWidth(130)
        ban.setFont(QFont(self.basicInfo.font1, 13))

        ban.addItem('1반')
        ban.addItem('2반')
        ban.addItem('3반')
        ban.addItem('4반')
        ban.addItem('5반')
        ban.addItem('6반')

        useLangL = QLabel("사용 가능 언어", self.w)
        useLangL.setFont(QFont(self.basicInfo.font1, 12))
        useLangL.setGeometry(100, 320, 200, 40)

        c = QCheckBox('c', self.w)
        c.setFont(QFont(self.basicInfo.font1, 15))
        c.setGeometry(120, 360, 150, 50)

        cpp = QCheckBox('c++', self.w)
        cpp.setFont(QFont(self.basicInfo.font1, 15))
        cpp.setGeometry(400, 360, 150, 50)

        cs = QCheckBox('c#', self.w)
        cs.setFont(QFont(self.basicInfo.font1, 15))
        cs.setGeometry(680, 360, 150, 50)

        py = QCheckBox('python', self.w)
        py.setFont(QFont(self.basicInfo.font1, 15))
        py.setGeometry(960, 360, 150, 50)

        html = QCheckBox('html', self.w)
        html.setFont(QFont(self.basicInfo.font1, 15))
        html.setGeometry(120, 430, 150, 50)

        css = QCheckBox('css', self.w)
        css.setFont(QFont(self.basicInfo.font1, 15))
        css.setGeometry(400, 430, 150, 50)

        js = QCheckBox('javascript', self.w)
        js.setFont(QFont(self.basicInfo.font1, 15))
        js.setGeometry(680, 430, 150, 50)

        jq = QCheckBox('jQuery', self.w)
        jq.setFont(QFont(self.basicInfo.font1, 15))
        jq.setGeometry(960, 430, 150, 50)

        jsp = QCheckBox('jsp', self.w)
        jsp.setFont(QFont(self.basicInfo.font1, 15))
        jsp.setGeometry(120, 510, 150, 50)

        php = QCheckBox('php', self.w)
        php.setFont(QFont(self.basicInfo.font1, 15))
        php.setGeometry(400, 510, 150, 50)

        node = QCheckBox('node.js', self.w)
        node.setFont(QFont(self.basicInfo.font1, 15))
        node.setGeometry(680, 510, 150, 50)

        react = QCheckBox('react', self.w)
        react.setFont(QFont(self.basicInfo.font1, 15))
        react.setGeometry(960, 510, 150, 50)

        java = QCheckBox('java', self.w)
        java.setFont(QFont(self.basicInfo.font1, 15))
        java.setGeometry(120, 580, 150, 50)

        spring = QCheckBox('spring', self.w)
        spring.setFont(QFont(self.basicInfo.font1, 15))
        spring.setGeometry(400, 580, 150, 50)

        servlet = QCheckBox('servlet', self.w)
        servlet.setFont(QFont(self.basicInfo.font1, 15))
        servlet.setGeometry(680, 580, 150, 50)

        kotlin = QCheckBox('kotlin', self.w)
        kotlin.setFont(QFont(self.basicInfo.font1, 15))
        kotlin.setGeometry(960, 580, 150, 50)

        android = QCheckBox('android', self.w)
        android.setFont(QFont(self.basicInfo.font1, 15))
        android.setGeometry(120, 650, 150, 50)

        linux = QCheckBox('Linux', self.w)
        linux.setFont(QFont(self.basicInfo.font1, 15))
        linux.setGeometry(400, 650, 150, 50)

        oracle = QCheckBox('oracle', self.w)
        oracle.setFont(QFont(self.basicInfo.font1, 15))
        oracle.setGeometry(680, 650, 150, 50)

        mysql = QCheckBox('mySQL', self.w)
        mysql.setFont(QFont(self.basicInfo.font1, 15))
        mysql.setGeometry(960, 650, 150, 50)

        etc = QCheckBox('etc', self.w)
        etc.setFont(QFont(self.basicInfo.font1, 15))
        etc.setGeometry(120, 720, 1000, 50)

        etcInput = QLineEdit(etc)
        etcInput.move(130, 10)
        etcInput.resize(840, 40)
        etcInput.setFont(QFont(self.basicInfo.font1, 12))

        likeCompanyL = QLabel("관심 회사", self.w)
        likeCompanyL.setFont(QFont(self.basicInfo.font1, 15))
        likeCompanyL.setGeometry(100, 810, 500, 50)

        pfL = QLabel('포트폴리오', self.w)
        pfL.setFont(QFont(self.basicInfo.font1, 15))
        pfL.move(100, 900)

        self.pfInput = QLineEdit(self.w)
        self.pfInput.setFont(QFont(self.basicInfo.font1, 10))
        self.pfInput.setGeometry(100, 950, 820, 50)

        pfBtn = QPushButton('Browse', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 12))
        pfBtn.setGeometry(950, 950, 130, 50)
        pfBtn.clicked.connect(self.show_file_open_p)

        introduceL = QLabel('자기소개서', self.w)
        introduceL.setFont(QFont(self.basicInfo.font1, 15))
        introduceL.move(100, 1050)

        self.introduceInput = QLineEdit(self.w)
        self.introduceInput.setFont(QFont(self.basicInfo.font1, 10))
        self.introduceInput.setGeometry(100, 1100, 820, 50)

        introduceBtn = QPushButton('Browse', self.w)
        introduceBtn.setFont(QFont(self.basicInfo.font1, 12))
        introduceBtn.setGeometry(950, 1100, 130, 50)
        introduceBtn.clicked.connect(self.show_file_open_i)

        modifyBtn = QPushButton('수정', self.w)
        modifyBtn.setFont(QFont(self.basicInfo.font1, 12))
        modifyBtn.setGeometry(950, 1200, 130, 30)
        modifyBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.w)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        vLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vLayout)

        self.show()

    def show_file_open_p(self):
        fname = QFileDialog.getOpenFileName()
        self.pfInput.setText(fname[0])

    def show_file_open_i(self):
        fname = QFileDialog.getOpenFileName()
        self.introduceInput.setText(fname[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = ModifyInfo()
    sys.exit(app.exec_())
