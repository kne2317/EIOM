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
        self.setWindowTitle('EIOM')
        self.w.resize(1200, 700)
        self.move(400, 100)
        self.setFixedSize(1200, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/join_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM - JOIN [ Student ]", self.w)
        title.setFont(QFont('impact', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 45, 1000, 50)

        c = QCheckBox('c',self.w)
        c.setFont(QFont('맑은 고딕',18))
        c.setGeometry(120,180,150,50)

        cpp = QCheckBox('c++', self.w)
        cpp.setFont(QFont('맑은 고딕', 18))
        cpp.setGeometry(400, 180, 150, 50)

        cs = QCheckBox('c#', self.w)
        cs.setFont(QFont('맑은 고딕', 18))
        cs.setGeometry(680, 180, 150, 50)

        py = QCheckBox('python', self.w)
        py.setFont(QFont('맑은 고딕', 18))
        py.setGeometry(960, 180, 150, 50)

        html = QCheckBox('html', self.w)
        html.setFont(QFont('맑은 고딕', 18))
        html.setGeometry(120, 250, 150, 50)

        css = QCheckBox('css', self.w)
        css.setFont(QFont('맑은 고딕', 18))
        css.setGeometry(400, 250, 150, 50)

        js = QCheckBox('javascript', self.w)
        js.setFont(QFont('맑은 고딕', 18))
        js.setGeometry(680, 250, 150, 50)

        jq = QCheckBox('jQuery', self.w)
        jq.setFont(QFont('맑은 고딕', 18))
        jq.setGeometry(960, 250, 150, 50)

        jsp = QCheckBox('jsp', self.w)
        jsp.setFont(QFont('맑은 고딕', 18))
        jsp.setGeometry(120, 320, 150, 50)

        php = QCheckBox('php', self.w)
        php.setFont(QFont('맑은 고딕', 18))
        php.setGeometry(400, 320, 150, 50)

        node = QCheckBox('node.js', self.w)
        node.setFont(QFont('맑은 고딕', 18))
        node.setGeometry(680, 320, 150, 50)

        react = QCheckBox('react', self.w)
        react.setFont(QFont('맑은 고딕', 18))
        react.setGeometry(960, 320, 150, 50)

        java = QCheckBox('java', self.w)
        java.setFont(QFont('맑은 고딕', 18))
        java.setGeometry(120, 390, 150, 50)

        spring = QCheckBox('spring', self.w)
        spring.setFont(QFont('맑은 고딕', 18))
        spring.setGeometry(400, 390, 150, 50)

        servlet = QCheckBox('servlet', self.w)
        servlet.setFont(QFont('맑은 고딕', 18))
        servlet.setGeometry(680, 390, 150, 50)

        kotlin = QCheckBox('kotlin', self.w)
        kotlin.setFont(QFont('맑은 고딕', 18))
        kotlin.setGeometry(960, 390, 150, 50)

        android = QCheckBox('android', self.w)
        android.setFont(QFont('맑은 고딕', 18))
        android.setGeometry(120, 460, 150, 50)

        linux = QCheckBox('Linux', self.w)
        linux.setFont(QFont('맑은 고딕', 18))
        linux.setGeometry(400, 460, 150, 50)

        oracle = QCheckBox('oracle', self.w)
        oracle.setFont(QFont('맑은 고딕', 18))
        oracle.setGeometry(680, 460, 150, 50)

        mysql = QCheckBox('mySQL', self.w)
        mysql.setFont(QFont('맑은 고딕', 18))
        mysql.setGeometry(960, 460, 150, 50)

        etc = QCheckBox('etc', self.w)
        etc.setFont(QFont('맑은 고딕', 18))
        etc.setGeometry(120, 540, 1000, 50)

        etcInput = QLineEdit(etc)
        etcInput.move(130,10)
        etcInput.resize(860,40)
        etcInput.setFont(QFont('맑은 고딕', 12))

        nextBtn = QPushButton('JOIN', self.w)
        nextBtn.setFont(QFont('맑은 고딕', 15))
        nextBtn.setGeometry(110, 620, 1000, 50)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = JoinS()
    sys.exit(app.exec_())
