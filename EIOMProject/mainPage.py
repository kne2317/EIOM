import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PySide2 import QtCore

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1300, 900)
    w.setWindowTitle("EIOM")

    label = QLabel("자퇴하고싶어 살려줘", w)

    label.setGeometry(100, 100, 200, 100)


    w.show()
    app.exec_()



