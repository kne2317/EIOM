import os

import shutil
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from company.Company import Company
import company.NoneEmployementRequest
import company.CompanyEmploymentRequest
import company.CompanyInfo
import company.RequestPortfolio
from BasicInfo import BasicInfo, BasicDB
from teacher.PofolPost import PofolPost, PofolRequestPost
import teacher.PortfolioRequest

class pofolList(QWidget):
    currentpage = 1
    pageCount = 0
    c_currentpage = 1
    c_pageCount = 0
    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.list_len = 9
        self.pofols = []
        self.pofols.append(PofolPost())
        self.pofols.append(PofolPost())
        self.pofols.append(PofolPost())
        self.pofols.append(PofolPost())
        self.pofols.append(PofolPost())
        self.pofols.append(PofolPost())
        self.pofols.append(PofolPost())
        self.pofols.append(PofolPost())
        self.pofols.append(PofolPost())
        self.reque = []
        self.reque.append(PofolRequestPost())
        self.reque.append(PofolRequestPost())
        self.reque.append(PofolRequestPost())
        self.reque.append(PofolRequestPost())
        self.reque.append(PofolRequestPost())
        self.reque.append(PofolRequestPost())
        self.reque.append(PofolRequestPost())
        self.reque.append(PofolRequestPost())
        self.reque.append(PofolRequestPost())
        self.getNoticeData()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
        self.setPalette(palette)

        self.w.setLayout(layout)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
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

        pfBtn = QPushButton('포트폴리오', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(self.basicInfo.WindowWidth/5*3, 70, self.basicInfo.WindowWidth/5, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내 정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(self.basicInfo.WindowWidth/5*4, 70, self.basicInfo.WindowWidth/5, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        stateBtn.clicked.connect(self.state)
        pfBtn.clicked.connect(self.pf)
        infoBtn.clicked.connect(self.info)

        name_width = 170
        pofol_width = 520
        hakbun_width = 170

        listX = 50
        listY = 180
        blankHeigth = 40

        fontsize = 12

        i = 0


        name_header = QPushButton("이름", self.w)
        name_header.setFont(QFont(self.basicInfo.font1, fontsize))
        name_header.setGeometry(listX, listY+blankHeigth*i, name_width+1, blankHeigth+1)
        name_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        pofol_header = QPushButton("포트폴리오", self.w)
        pofol_header.setFont(QFont(self.basicInfo.font1, fontsize))
        pofol_header.setGeometry(listX + name_width, listY+blankHeigth*i, pofol_width+1, blankHeigth+1)
        pofol_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        hakbun_header = QPushButton("학번", self.w)
        hakbun_header.setFont(QFont(self.basicInfo.font1, fontsize))
        hakbun_header.setGeometry(listX + name_width + pofol_width, listY+blankHeigth*i, hakbun_width, blankHeigth+1)
        hakbun_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        self.name = []
        self.pofol = []
        self.hakbun = []

        #0
        i=0
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY+blankHeigth*(i+1), name_width+1, blankHeigth+1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY+blankHeigth*(i+1), pofol_width+1, blankHeigth+1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; color: #3c78d8;')
        self.pofol[i].clicked.connect(lambda v: self.func(0))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY+blankHeigth*(i+1), hakbun_width, blankHeigth+1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')

        #1
        i+=1
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY + blankHeigth * (i + 1), name_width + 1, blankHeigth + 1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY + blankHeigth * (i + 1), pofol_width + 1, blankHeigth + 1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; color: #3c78d8;')
        self.pofol[i].clicked.connect(lambda v: self.func(1))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY + blankHeigth * (i + 1), hakbun_width, blankHeigth + 1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')

        #2
        i+=1
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY + blankHeigth * (i + 1), name_width + 1, blankHeigth + 1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY + blankHeigth * (i + 1), pofol_width + 1, blankHeigth + 1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; color: #3c78d8;')
        self.pofol[i].clicked.connect(lambda v: self.func(2))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY + blankHeigth * (i + 1), hakbun_width, blankHeigth + 1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')

        #3
        i+=1
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY + blankHeigth * (i + 1), name_width + 1, blankHeigth + 1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY + blankHeigth * (i + 1), pofol_width + 1, blankHeigth + 1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; color: #3c78d8;')
        self.pofol[i].clicked.connect(lambda v: self.func(3))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY + blankHeigth * (i + 1), hakbun_width, blankHeigth + 1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')

        #4
        i+=1
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY + blankHeigth * (i + 1), name_width + 1, blankHeigth + 1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY + blankHeigth * (i + 1), pofol_width + 1, blankHeigth + 1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; color: #3c78d8;')
        self.pofol[i].clicked.connect(lambda v: self.func(4))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY + blankHeigth * (i + 1), hakbun_width, blankHeigth + 1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')

        #5
        i+=1
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY + blankHeigth * (i + 1), name_width + 1, blankHeigth + 1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY + blankHeigth * (i + 1), pofol_width + 1, blankHeigth + 1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; color: #3c78d8;')
        self.pofol[i].clicked.connect(lambda v: self.func(5))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY + blankHeigth * (i + 1), hakbun_width, blankHeigth + 1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')

        #6
        i+=1
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY + blankHeigth * (i + 1), name_width + 1, blankHeigth + 1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY + blankHeigth * (i + 1), pofol_width + 1, blankHeigth + 1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; color: #3c78d8;')
        self.pofol[i].clicked.connect(lambda v: self.func(6))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY + blankHeigth * (i + 1), hakbun_width, blankHeigth + 1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')

        #7
        i+=1
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY + blankHeigth * (i + 1), name_width + 1, blankHeigth + 1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY + blankHeigth * (i + 1), pofol_width + 1, blankHeigth + 1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; color: #3c78d8;')
        self.pofol[i].clicked.connect(lambda v: self.func(7))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY + blankHeigth * (i + 1), hakbun_width, blankHeigth + 1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')

        #8
        i+=1
        self.name.append('')
        self.name[i] = QPushButton(self.pofols[i].name, self.w)
        self.name[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.name[i].setGeometry(listX, listY + blankHeigth * (i + 1), name_width + 1, blankHeigth + 1)
        self.name[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px;text-align: left; border-bottom:2px solid #ababab; padding-left: 30px; ')

        self.pofol.append('')
        self.pofol[i] = QPushButton(self.pofols[i].pofol, self.w)
        self.pofol[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.pofol[i].setGeometry(listX + name_width, listY + blankHeigth * (i + 1), pofol_width + 1, blankHeigth + 1)
        self.pofol[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; border-bottom:2px solid #ababab; ')
        self.pofol[i].clicked.connect(lambda v: self.func(8))

        self.hakbun.append('')
        self.hakbun[i] = QPushButton(self.pofols[i].hakbun, self.w)
        self.hakbun[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.hakbun[i].setGeometry(listX + name_width + pofol_width, listY + blankHeigth * (i + 1), hakbun_width, blankHeigth + 1)
        self.hakbun[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; border-bottom:2px solid #ababab; ')


        firstBtnX = 380
        prevPageBtn = QPushButton("<", self.w)
        prevPageBtn.setFont(QFont(self.basicInfo.font1, 14))
        prevPageBtn.setGeometry(firstBtnX, 600, 15, 20)
        prevPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        prevPageBtn.clicked.connect(self.prevPage)

        self.pageBtn_1 = QPushButton(self.currentpage>2 and str(self.currentpage-2) or '', self.w)
        self.pageBtn_1.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_1.setGeometry(firstBtnX+40, 600, 15, 20)
        self.pageBtn_1.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_1.clicked.connect(self.prev2Page)

        self.pageBtn_2 = QPushButton(self.currentpage>1 and str(self.currentpage-1) or '', self.w)
        self.pageBtn_2.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_2.setGeometry(firstBtnX*40*2, 600, 15, 20)
        self.pageBtn_2.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_2.clicked.connect(self.prev1Page)

        self.currentPageBtn = QPushButton(str(self.currentpage), self.w)
        self.currentPageBtn.setFont(QFont(self.basicInfo.font1, fontsize))
        self.currentPageBtn.setGeometry(firstBtnX+40*3, 600, 15, 20)
        self.currentPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); font-weight: bold;')
        self.currentPageBtn.clicked.connect(self.currentPage)

        self.pageBtn_3 = QPushButton(self.pageCount >= self.currentpage+1 and str(self.currentpage+1) or '', self.w)
        self.pageBtn_3.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_3.setGeometry(firstBtnX+40*4, 600, 15, 20)
        self.pageBtn_3.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_3.clicked.connect(self.next1Page)

        self.pageBtn_4 = QPushButton(self.pageCount >= self.currentpage+2 and str(self.currentpage+2) or '', self.w)
        self.pageBtn_4.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_4.setGeometry(firstBtnX+40*5, 600, 15, 20)
        self.pageBtn_4.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_4.clicked.connect(self.next2Page)

        nextPageBtn = QPushButton(">", self.w)
        nextPageBtn.setFont(QFont(self.basicInfo.font1, 14))
        nextPageBtn.setGeometry(firstBtnX+40*6, 600, 15, 20)
        nextPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        nextPageBtn.clicked.connect(self.nextPage)





        requestWidth = 200

        c_listX = 960
        c_listY = 180
        #blankHeigth = 40

        fontsize = 12

        i = 0
        name_header = QPushButton("열람신청", self.w)
        name_header.setFont(QFont(self.basicInfo.font1, fontsize))
        name_header.setGeometry(c_listX, c_listY+blankHeigth*i, requestWidth, blankHeigth)
        name_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        self.request = []

        #0
        i=0
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY+blankHeigth*(i+1), requestWidth, blankHeigth+1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.request[i].clicked.connect(lambda v: self.func2(0))

        #1
        i+=1
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY + blankHeigth * (i + 1), requestWidth, blankHeigth + 1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.request[i].clicked.connect(lambda v: self.func2(1))

        #2
        i+=1
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY + blankHeigth * (i + 1), requestWidth, blankHeigth + 1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.request[i].clicked.connect(lambda v: self.func2(2))

        #3
        i+=1
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY + blankHeigth * (i + 1), requestWidth, blankHeigth + 1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.request[i].clicked.connect(lambda v: self.func2(3))

        #4
        i+=1
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY + blankHeigth * (i + 1), requestWidth, blankHeigth + 1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.request[i].clicked.connect(lambda v: self.func2(4))

        #5
        i+=1
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY + blankHeigth * (i + 1), requestWidth, blankHeigth + 1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.request[i].clicked.connect(lambda v: self.func2(5))

        #6
        i+=1
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY + blankHeigth * (i + 1), requestWidth, blankHeigth + 1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.request[i].clicked.connect(lambda v: self.func2(6))

        #7
        i+=1
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY + blankHeigth * (i + 1), requestWidth, blankHeigth + 1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.request[i].clicked.connect(lambda v: self.func2(7))

        #8
        i+=1
        self.request.append('')
        self.request[i] = QPushButton(self.reque[i].companyname, self.w)
        self.request[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.request[i].setGeometry(c_listX, c_listY + blankHeigth * (i + 1), requestWidth, blankHeigth + 1)
        self.request[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px;text-align: left; border-bottom:2px solid #ababab; padding-left: 30px; ')
        self.request[i].clicked.connect(lambda v: self.func2(8))

        firstBtnX = 1020
        c_prevPageBtn = QPushButton("<", self.w)
        c_prevPageBtn.setFont(QFont(self.basicInfo.font1, 14))
        c_prevPageBtn.setGeometry(firstBtnX, 600, 15, 20)
        c_prevPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        c_prevPageBtn.clicked.connect(self.c_prevPage)

        c_prevPageBtn = QPushButton(">", self.w)
        c_prevPageBtn.setFont(QFont(self.basicInfo.font1, 14))
        c_prevPageBtn.setGeometry(firstBtnX+70, 600, 15, 20)
        c_prevPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        c_prevPageBtn.clicked.connect(self.c_nextPage)


        self.show()

    def prevPage(self):
        if(self.currentpage-1 >= 1):
            self.currentpage -= 1
            self.getNoticeData()
            self.setPageText()

    def prev2Page(self):
        if(self.currentpage-2 >= 1):
            self.currentpage -= 2
            self.getNoticeData()
            self.setPageText()

    def prev1Page(self):
        if(self.currentpage-1 >= 1):
            self.currentpage -= 1
            self.getNoticeData()
            self.setPageText()

    def currentPage(self):
        self.setPageText()

    def next1Page(self):
        if(self.currentpage+1 <= self.pageCount):
            self.currentpage += 1
            self.getNoticeData()
            self.setPageText()

    def next2Page(self):
        if(self.currentpage+2 <= self.pageCount):
            self.currentpage += 2
            self.getNoticeData()
            self.setPageText()

    def nextPage(self):
        if(self.currentpage+1 <= self.pageCount):
            self.currentpage += 1
            self.getNoticeData()
            self.setPageText()

    def c_prevPage(self):
        if (self.c_currentpage - 1 >= 1):
            self.c_currentpage -= 1
            self.getNoticeData()
            self.setPageText()

    def c_nextPage(self):
        if(self.c_currentpage+1 <= self.c_pageCount):
            self.c_currentpage += 1
            self.getNoticeData()
            self.setPageText()

    def setPageText(self):
        self.close()
        self.show()
        self.pageBtn_1.setText(self.currentpage>2 and str(self.currentpage-2) or '')
        self.pageBtn_2.setText(self.currentpage>1 and str(self.currentpage-1) or '')
        self.currentPageBtn.setText(str(self.currentpage))
        self.pageBtn_3.setText(self.pageCount >= self.currentpage+1 and str(self.currentpage+1) or '')
        self.pageBtn_4.setText(self.pageCount >= self.currentpage+2 and str(self.currentpage+2) or '')

        for i in range(self.list_len):
            self.name[i].setText(self.pofols[i].name)
            self.pofol[i].setText(self.pofols[i].pofol)
            self.hakbun[i].setText(str(self.pofols[i].hakbun))
            self.request[i].setText(self.reque[i].companyname)


    def getNoticeData(self):
        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()

        sql = "SELECT * FROM eiom_db.student where portfolio like '%';"
        curs.execute(sql)

        rows = curs.fetchall()

        for i in range((self.currentpage-1)*9, self.currentpage*9):
            if i < len(rows) :
                self.pofols[i%9].name = rows[i][2]
                self.pofols[i%9].pofol = rows[i][6]
                self.pofols[i%9].hakbun = str(rows[i][4]) + "학년" + str(rows[i][5]) + "반"
            else:
                self.pofols[i%9].name = ''
                self.pofols[i%9].pofol = ''
                self.pofols[i%9].hakbun = ''

        self.pageCount = len(rows) // 9 + 1


        sql = "SELECT * FROM eiom_db.portfolio_request;"
        curs.execute(sql)

        rows = curs.fetchall()

        for i in range((self.c_currentpage-1)*9, self.c_currentpage*9):
            if i < len(rows) :
                self.reque[i%9].id = rows[i][0]
                self.reque[i%9].companyname = rows[i][1]
                self.reque[i%9].pfrequest = rows[i][2]
                self.reque[i%9].pfperiod = rows[i][3]
                self.reque[i%9].com_id = rows[i][4]
            else:
                self.reque[i%9].id = ''
                self.reque[i%9].companyname = ''
                self.reque[i%9].pfrequest = ''
                self.reque[i%9].pfperiod = ''
                self.reque[i%9].com_id = ''

        self.c_pageCount = len(rows) // 9 + 1

        conn.close()

    def func(self, noticeNum):
        # 포폴다운
        try:
            pfile_name = self.pofols[noticeNum].pofol
            poriginal_path = os.path.dirname(os.path.realpath(__file__)) + "\\..\\portfolio"
            pdestination_path = os.path.expanduser("~")+"/Downloads"
            shutil.copyfile(os.path.join(poriginal_path, pfile_name), os.path.join(pdestination_path, pfile_name))
            QMessageBox.about(self, "완료", "다운로드가 완료되었습니다")
        except Exception as e:
            print(e)

    def func2(self, noticeNum):
        try:
            print(self.reque[noticeNum].companyname)
            self.cp = teacher.PortfolioRequest.PortfolioRequest(self.reque[noticeNum])
            self.cp.show()
            self.hide()
        except Exception as e:
            print(e)

    def state(self):
        if Company.request_authority == 0:
            self.ncr = company.NoneEmployementRequest.NoneEmployementRequest()
            self.ncr.show()
            self.hide()
        else:
            self.cr = company.CompanyEmploymentRequest.CompanyEmploymentRequest()
            self.cr.show()
            self.hide()

    def pf(self):
        if Company.pfauthority == 0:
            self.np = company.NonePofol.NonePofol()
            self.np.show()
            self.hide()
        else:
            self.p=company.PofolList.pofolList()
            self.p.show()
            self.hide()

    def info(self):
        self.ci = company.CompanyInfo.CompanyInfo()
        self.ci.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = pofolList()
    sys.exit(app.exec_())
