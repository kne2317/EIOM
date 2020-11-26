import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore


class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        w = QWidget(self)
        layout = QVBoxLayout()
        self.setWindowTitle('EIOM')
        self.move(350, 150)
        self.resize(1200, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/login_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM")
        layout.addWidget(title)
        w.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
