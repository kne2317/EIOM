import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
from datetime import datetime
from BasicInfo import BasicInfo
from employmentRate.EmploymentRate import eRateDB, updateRate


class MyPage(QWidget):

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)

        self.initUI()

    def initUI(self):
        self.y1 = eRateDB(1)
        self.y2 = eRateDB(2)
        self.y3 = eRateDB(3)

        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, 1000)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
        self.w.setPalette(palette)

        self.w.setLayout(layout)

        title = QLabel("취업률 상세 정보", self.w)
        title.setFont(QFont(self.basicInfo.font1, 20))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 10, 1000, 50)

        stateBtn = QPushButton('통계', self.w)
        stateBtn.setFont(QFont(self.basicInfo.font1, 13))
        stateBtn.setGeometry(0, 70, self.basicInfo.WindowWidth/5, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(self.basicInfo.WindowWidth/5*1, 70, self.basicInfo.WindowWidth/5, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('취업의뢰', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(self.basicInfo.WindowWidth/5*2, 70, self.basicInfo.WindowWidth/5, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        postBtn = QPushButton('포트폴리오', self.w)
        postBtn.setFont(QFont(self.basicInfo.font1, 13))
        postBtn.setGeometry(self.basicInfo.WindowWidth/5*3, 70, self.basicInfo.WindowWidth/5, 50)
        postBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        pfBtn = QPushButton('내 정보', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(self.basicInfo.WindowWidth/5*4, 70, self.basicInfo.WindowWidth/5, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        la1 = QLabel("3학년 인원 수",self.w)
        la1.setFont(QFont(self.basicInfo.font1,13))
        la1.setGeometry(100,150,200,40)

        y1_1=QLabel(self.y3['year'] + '년',self.w)
        y1_1.setFont(QFont(self.basicInfo.font1, 15))
        y1_1.setGeometry(300, 200, 200, 40)

        s1_1=QSpinBox(self.w)
        s1_1.setFont(QFont(self.basicInfo.font1,13))
        s1_1.setGeometry(300,250,200,40)
        s1_1.setRange(0,120)
        s1_1.setValue(self.y3['grade3'])

        y1_2 = QLabel(self.y2['year'] + '년', self.w)
        y1_2.setFont(QFont(self.basicInfo.font1, 15))
        y1_2.setGeometry(600, 200, 200, 40)

        s1_2 = QSpinBox(self.w)
        s1_2.setFont(QFont(self.basicInfo.font1, 13))
        s1_2.setGeometry(600, 250, 200, 40)
        s1_2.setRange(0, 120)
        s1_2.setValue(self.y2['grade3'])

        y1_3 = QLabel(self.y1['year'] + '년', self.w)
        y1_3.setFont(QFont(self.basicInfo.font1, 15))
        y1_3.setGeometry(900, 200, 200, 40)

        s1_3 = QSpinBox(self.w)
        s1_3.setFont(QFont(self.basicInfo.font1, 13))
        s1_3.setGeometry(900, 250, 200, 40)
        s1_3.setRange(0, 120)
        s1_3.setValue(self.y1['grade3'])

        la2 = QLabel("EIOM 취업", self.w)
        la2.setFont(QFont(self.basicInfo.font1, 13))
        la2.setGeometry(100, 350, 200, 40)

        y2_1 = QLabel(self.y3['year'] + '년', self.w)
        y2_1.setFont(QFont(self.basicInfo.font1, 15))
        y2_1.setGeometry(300, 400, 200, 40)

        s2_1 = QSpinBox(self.w)
        s2_1.setFont(QFont(self.basicInfo.font1, 13))
        s2_1.setGeometry(300, 450, 200, 40)
        s2_1.setRange(0, 120)
        s2_1.setValue(self.y3['eiom'])

        y2_2 = QLabel(self.y2['year'] + '년', self.w)
        y2_2.setFont(QFont(self.basicInfo.font1, 15))
        y2_2.setGeometry(600, 400, 200, 40)

        s2_2 = QSpinBox(self.w)
        s2_2.setFont(QFont(self.basicInfo.font1, 13))
        s2_2.setGeometry(600, 450, 200, 40)
        s2_2.setRange(0, 120)
        s2_2.setValue(self.y2['eiom'])

        y2_3 = QLabel(y1['year'] + '년', self.w)
        y2_3.setFont(QFont(self.basicInfo.font1, 15))
        y2_3.setGeometry(900, 400, 200, 40)

        s2_3 = QSpinBox(self.w)
        s2_3.setFont(QFont(self.basicInfo.font1, 13))
        s2_3.setGeometry(900, 450, 200, 40)
        s2_3.setRange(0, 120)
        s2_3.setValue(self.y1['eiom'])

        la3 = QLabel("현장 취업", self.w)
        la3.setFont(QFont(self.basicInfo.font1, 13))
        la3.setGeometry(100, 550, 200, 40)

        y3_1 = QLabel(self.y3['year'] + '년', self.w)
        y3_1.setFont(QFont(self.basicInfo.font1, 15))
        y3_1.setGeometry(300, 600, 200, 40)

        s3_1 = QSpinBox(self.w)
        s3_1.setFont(QFont(self.basicInfo.font1, 13))
        s3_1.setGeometry(300, 650, 200, 40)
        s3_1.setRange(0, 120)
        s3_1.setValue(self.y3['scene'])

        y3_2 = QLabel(self.y2['year'] + '년', self.w)
        y3_2.setFont(QFont(self.basicInfo.font1, 15))
        y3_2.setGeometry(600, 600, 200, 40)

        s3_2 = QSpinBox(self.w)
        s3_2.setFont(QFont(self.basicInfo.font1, 13))
        s3_2.setGeometry(600, 650, 200, 40)
        s3_2.setRange(0, 120)
        s3_2.setValue(self.y2['scene'])

        y3_3 = QLabel(self.y1['year'] + '년', self.w)
        y3_3.setFont(QFont(self.basicInfo.font1, 15))
        y3_3.setGeometry(900, 600, 200, 40)

        s3_3 = QSpinBox(self.w)
        s3_3.setFont(QFont(self.basicInfo.font1, 13))
        s3_3.setGeometry(900, 650, 200, 40)
        s3_3.setRange(0, 120)
        s3_3.setValue(self.y1['scene'])

        la4 = QLabel("자가 취업", self.w)
        la4.setFont(QFont(self.basicInfo.font1, 13))
        la4.setGeometry(100, 750, 200, 40)

        y4_1 = QLabel(self.y3['year'] + '년', self.w)
        y4_1.setFont(QFont(self.basicInfo.font1, 15))
        y4_1.setGeometry(300, 800, 200, 40)

        s4_1 = QSpinBox(self.w)
        s4_1.setFont(QFont(self.basicInfo.font1, 13))
        s4_1.setGeometry(300, 850, 200, 40)
        s4_1.setRange(0, 120)
        s4_1.setValue(self.y3['self'])

        y4_2 = QLabel(self.y2['year'] + '년', self.w)
        y4_2.setFont(QFont(self.basicInfo.font1, 15))
        y4_2.setGeometry(600, 800, 200, 40)

        s4_2 = QSpinBox(self.w)
        s4_2.setFont(QFont(self.basicInfo.font1, 13))
        s4_2.setGeometry(600, 850, 200, 40)
        s4_2.setRange(0, 120)
        s4_2.setValue(self.y2['self'])

        y4_3 = QLabel(self.y1['year'] + '년', self.w)
        y4_3.setFont(QFont(self.basicInfo.font1, 15))
        y4_3.setGeometry(900, 800, 200, 40)

        s4_3 = QSpinBox(self.w)
        s4_3.setFont(QFont(self.basicInfo.font1, 13))
        s4_3.setGeometry(900, 850, 200, 40)
        s4_3.setRange(0, 120)
        s4_3.setValue(self.y1['self'])

        okayBtn = QPushButton('확인', self.w)
        okayBtn.setFont(QFont(self.basicInfo.font1, 12))
        okayBtn.setGeometry(850, 950, 120, 40)
        okayBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')


        cancleBtn = QPushButton('취소', self.w)
        cancleBtn.setFont(QFont(self.basicInfo.font1, 12))
        cancleBtn.setGeometry(980, 950, 120, 40)
        cancleBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.w)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        vLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vLayout)

    def okay(self):
        updateRate(self.y1,self.y2,self.y3)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPage()
    ex.show()
    app.exec_()
