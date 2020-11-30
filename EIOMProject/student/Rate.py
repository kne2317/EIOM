import sys
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
import employmentRate.EmploymentRate

import company.EmployeeRequestDB


class sRate(QWidget):

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)

        self.initUI()

    def initUI(self):
        y1 = employmentRate.EmploymentRate.eRateDB(1)
        y2 = employmentRate.EmploymentRate.eRateDB(2)
        y3 = employmentRate.EmploymentRate.eRateDB(3)

        mainLayout = QVBoxLayout(self)
        self.w.setLayout(mainLayout)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight+700)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/background.png")))
        self.setPalette(palette)


        title = QLabel("EIOM", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 10, 1000, 50)



        stateBtn = QPushButton('통계', self.w)
        stateBtn.setFont(QFont(self.basicInfo.font1, 13))
        stateBtn.setGeometry(0, 70, 200, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(200, 70, 200, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('회사', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(400, 70, 200, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        postBtn = QPushButton('취업의뢰', self.w)
        postBtn.setFont(QFont(self.basicInfo.font1, 13))
        postBtn.setGeometry(600, 70, 200, 50)
        postBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        pfBtn = QPushButton('포트폴리오', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(800, 70, 200, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내 정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(1000, 70, 200, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        contentLayout = QVBoxLayout()

        emptyLabel = QLabel("\n\n\n\n\n\n\n\n\n\n\n\n")
        contentLayout.addWidget(emptyLabel)

        label_employment_rate = QPushButton('취업률', self.w)
        label_employment_rate.setFont(QFont(self.basicInfo.font1, 18))
        label_employment_rate.setGeometry(50, 150, 200, 50)
        label_employment_rate.setStyleSheet('background-color: rgba(255,255,255,0); border:0px')

        label_1 = QPushButton(y3['year'] + '년', self.w)
        label_1.setFont(QFont(self.basicInfo.font1, 13))
        label_1.setGeometry(150, 230, 301, 51)
        label_1.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_2 = QPushButton(y2['year'] + '년', self.w)
        label_2.setFont(QFont(self.basicInfo.font1, 13))
        label_2.setGeometry(150 + 300 * 1, 230, 301, 51)
        label_2.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_3 = QPushButton(y1['year'] + '년', self.w)
        label_3.setFont(QFont(self.basicInfo.font1, 13))
        label_3.setGeometry(150 + 300 * 2, 230, 300, 51)
        label_3.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_4 = QPushButton(str(round(employmentRate.EmploymentRate.employRate(y3['grade3'], (y3['self'] + y3['eiom'] + y3['scene'])),2)) + "%", self.w)
        label_4.setFont(QFont(self.basicInfo.font1, 13))
        label_4.setGeometry(150, 280, 301, 50)
        label_4.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_5 = QPushButton(str(round(employmentRate.EmploymentRate.employRate(y2['grade3'], (y2['self'] + y2['eiom'] + y2['scene'])),2)) + "%", self.w)
        label_5.setFont(QFont(self.basicInfo.font1, 13))
        label_5.setGeometry(150 + 300 * 1, 280, 301, 50)
        label_5.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_6 = QPushButton(str(round(employmentRate.EmploymentRate.employRate(y1['grade3'], (y1['self'] + y1['eiom'] + y1['scene'])),2)) + "%", self.w)
        label_6.setFont(QFont(self.basicInfo.font1, 13))
        label_6.setGeometry(150 + 300 * 2, 280, 300, 50)
        label_6.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_employment_rate = QPushButton('취업 의뢰', self.w)
        label_employment_rate.setFont(QFont(self.basicInfo.font1, 18))
        label_employment_rate.setGeometry(50, 450, 200, 50)
        label_employment_rate.setStyleSheet('background-color: rgba(255,255,255,0); border:0px')

        label_1 = QPushButton(y3['year'] + '년', self.w)
        label_1.setFont(QFont(self.basicInfo.font1, 13))
        label_1.setGeometry(150, 530, 301, 51)
        label_1.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_2 = QPushButton(y2['year'] + '년', self.w)
        label_2.setFont(QFont(self.basicInfo.font1, 13))
        label_2.setGeometry(150 + 300 * 1, 530, 301, 51)
        label_2.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_3 = QPushButton(y1['year'] + '년', self.w)
        label_3.setFont(QFont(self.basicInfo.font1, 13))
        label_3.setGeometry(150 + 300 * 2, 530, 300, 51)
        label_3.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_4 = QPushButton(str(y3['request_cnt']) + "건", self.w)
        label_4.setFont(QFont(self.basicInfo.font1, 13))
        label_4.setGeometry(150, 580, 301, 50)
        label_4.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_5 = QPushButton(str(y2['request_cnt']) + "건", self.w)
        label_5.setFont(QFont(self.basicInfo.font1, 13))
        label_5.setGeometry(150 + 300 * 1, 580, 301, 50)
        label_5.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        label_6 = QPushButton(str(y1['request_cnt']) + "건", self.w)
        label_6.setFont(QFont(self.basicInfo.font1, 13))
        label_6.setGeometry(150 + 300 * 2, 580, 300, 50)
        label_6.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')


        label_employment_rate = QPushButton('취업 의뢰', self.w)
        label_employment_rate.setFont(QFont(self.basicInfo.font1, 18))
        label_employment_rate.setGeometry(50, 450, 200, 50)
        label_employment_rate.setStyleSheet('background-color: rgba(255,255,255,0); border:0px')


        label_employment_rate = QPushButton('취업 의뢰 언어 비율', self.w)
        label_employment_rate.setFont(QFont(self.basicInfo.font1, 18))
        label_employment_rate.setGeometry(50, 750, 300, 50)
        label_employment_rate.setStyleSheet('background-color: rgba(255,255,255,0); border:0px')



        contentLayout.addWidget(emptyLabel)
        emptyLabel = QLabel("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        contentLayout.addWidget(emptyLabel)

        N = 4

        lang = company.EmployeeRequestDB.orderByBestLang()

        best4 = {}
        for key, value in lang.items():
            if len(best4) == N:
                break
            else:
                best4[key] = value
        b_lang = []
        for key in best4.keys():
            b_lang.append(key)

        b_value = []
        for value in best4.values():
            b_value.append(value)
        print(b_value)

        value = b_value
        ind = np.arange(N)
        width = 0.2
        fig = plt.Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot()
        ax.bar(ind, value, width, color='lightblue')
        ax.set_xticks(ind + width / 20)
        ax.set_xticklabels(b_lang)

        contentLayout.addWidget(canvas)
        emptyLabel = QLabel("\n\n\n\n\n\n")
        contentLayout.addWidget(emptyLabel)
        mainLayout.addLayout(contentLayout)



        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.w)

        basicLayout = QVBoxLayout(self)
        basicLayout.addWidget(scroll)
        basicLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(basicLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = sRate()
    ex.show()
    app.exec_()
