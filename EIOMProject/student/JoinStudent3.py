
import sys

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
from Join import StudentJoin
import main
from student.Student import Student, Languages


class JoinS3(QWidget):

    def __init__(self):
        super().__init__()
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

        title = QLabel("EIOM - JOIN [ Student ]", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 45, 1000, 50)

        self.c = QCheckBox('c',self.w)
        self.c.setFont(QFont(self.basicInfo.font1,18))
        self.c.setGeometry(120,180,150,50)

        self.cpp = QCheckBox('c++', self.w)
        self.cpp.setFont(QFont(self.basicInfo.font1, 18))
        self.cpp.setGeometry(400, 180, 150, 50)

        self.cs = QCheckBox('c#', self.w)
        self.cs.setFont(QFont(self.basicInfo.font1, 18))
        self.cs.setGeometry(680, 180, 150, 50)

        self.py = QCheckBox('python', self.w)
        self.py.setFont(QFont(self.basicInfo.font1, 18))
        self.py.setGeometry(960, 180, 150, 50)

        self.html = QCheckBox('html', self.w)
        self.html.setFont(QFont(self.basicInfo.font1, 18))
        self.html.setGeometry(120, 250, 150, 50)

        self.css = QCheckBox('css', self.w)
        self.css.setFont(QFont(self.basicInfo.font1, 18))
        self.css.setGeometry(400, 250, 150, 50)

        self.js = QCheckBox('javascript', self.w)
        self.js.setFont(QFont(self.basicInfo.font1, 18))
        self.js.setGeometry(680, 250, 150, 50)

        self.jq = QCheckBox('jQuery', self.w)
        self.jq.setFont(QFont(self.basicInfo.font1, 18))
        self.jq.setGeometry(960, 250, 150, 50)

        self.jsp = QCheckBox('jsp', self.w)
        self.jsp.setFont(QFont(self.basicInfo.font1, 18))
        self.jsp.setGeometry(120, 320, 150, 50)

        self.php = QCheckBox('php', self.w)
        self.php.setFont(QFont(self.basicInfo.font1, 18))
        self.php.setGeometry(400, 320, 150, 50)

        self.node = QCheckBox('node.js', self.w)
        self.node.setFont(QFont(self.basicInfo.font1, 18))
        self.node.setGeometry(680, 320, 150, 50)

        self.react = QCheckBox('react', self.w)
        self.react.setFont(QFont(self.basicInfo.font1, 18))
        self.react.setGeometry(960, 320, 150, 50)

        self.java = QCheckBox('java', self.w)
        self.java.setFont(QFont(self.basicInfo.font1, 18))
        self.java.setGeometry(120, 390, 150, 50)

        self.spring = QCheckBox('spring', self.w)
        self.spring.setFont(QFont(self.basicInfo.font1, 18))
        self.spring.setGeometry(400, 390, 150, 50)

        self.servlet = QCheckBox('servlet', self.w)
        self.servlet.setFont(QFont(self.basicInfo.font1, 18))
        self.servlet.setGeometry(680, 390, 150, 50)

        self.kotlin = QCheckBox('kotlin', self.w)
        self.kotlin.setFont(QFont(self.basicInfo.font1, 18))
        self.kotlin.setGeometry(960, 390, 150, 50)

        self.android = QCheckBox('android', self.w)
        self.android.setFont(QFont(self.basicInfo.font1, 18))
        self.android.setGeometry(120, 460, 150, 50)

        self.linux = QCheckBox('Linux', self.w)
        self.linux.setFont(QFont(self.basicInfo.font1, 18))
        self.linux.setGeometry(400, 460, 150, 50)

        self.oracle = QCheckBox('oracle', self.w)
        self.oracle.setFont(QFont(self.basicInfo.font1, 18))
        self.oracle.setGeometry(680, 460, 150, 50)

        self.mysql = QCheckBox('mySQL', self.w)
        self.mysql.setFont(QFont(self.basicInfo.font1, 18))
        self.mysql.setGeometry(960, 460, 150, 50)

        self.etc = QCheckBox('etc', self.w)
        self.etc.setFont(QFont(self.basicInfo.font1, 18))
        self.etc.setGeometry(120, 540, 1000, 50)

        self.etcInput = QLineEdit(self.etc)
        self.etcInput.move(130,10)
        self.etcInput.resize(860,40)
        self.etcInput.setFont(QFont(self.basicInfo.font1, 12))

        self.JoinBtn = QPushButton('JOIN', self.w)
        self.JoinBtn.setFont(QFont(self.basicInfo.font1, 15))
        self.JoinBtn.setGeometry(110, 620, 1000, 50)
        self.JoinBtn.clicked.connect(self.Join)


        self.show()

    def Join(self):
        if self.c.isChecked():
            Languages.c = True

        if self.cpp.isChecked():
            Languages.cpp = True

        if self.cs.isChecked():
            Languages.cs = True

        if self.py.isChecked():
            Languages.py = True

        if self.html.isChecked():
            Languages.html = True

        if self.css.isChecked():
            Languages.css = True

        if self.js.isChecked():
            Languages.js = True

        if self.jq.isChecked():
            Languages.jp = True

        if self.jsp.isChecked():
            Languages.jsp = True

        if self.php.isChecked():
            Languages.php = True

        if self.node.isChecked():
            Languages.node = True

        if self.react.isChecked():
            Languages.react = True

        if self.java.isChecked():
            Languages.java = True

        if self.spring.isChecked():
            Languages.spring = True

        if self.servlet.isChecked():
            Languages.servlet = True

        if self.kotlin.isChecked():
            Languages.kotlin = True

        if self.android.isChecked():
            Languages.android = True

        if self.linux.isChecked():
            Languages.linux = True

        if self.oracle.isChecked():
            Languages.oracle = True

        if self.mysql.isChecked():
            Languages.mysql = True

        if self.etc.isChecked():
            Languages.etc = self.etcInput.text()



        if StudentJoin():
            # 회원가입 성공
            print("회원가입에 성공하였습니다.")

            self.nextPage = main.Main()
            self.close()
            self.nextPage.show()
        else:
            print("회원가입이 실패하였습니다.")
        # Join


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = JoinS3()
    sys.exit(app.exec_())