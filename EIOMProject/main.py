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
        w.setWindowTitle('EIOM')
        w.resize(1200, 700)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/login_background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM", w)
        title.setFont(QFont('Bauhaus 93', 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 100, 1000, 400)

        title2 = QLabel("Employment Information Of Mirim", w)
        title2.setFont(QFont('Bauhaus 93', 20))
        title2.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title2)
        title2.setGeometry(100, 100, 1000, 500)


        #w.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
