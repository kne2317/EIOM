

import os
import shutil
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

import student.Rate
import student.NoticeList
import student.MyPage
from BasicInfo import BasicInfo, BasicDB
import student.CompanyPost
from student.Company import Company


class CompanyList(QWidget):
    currentpage = 1
    pageCount = 0

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.companies = []
        self.companies.append(Company())
        self.companies.append(Company())
        self.companies.append(Company())
        self.companies.append(Company())
        self.companies.append(Company())
        self.companies.append(Company())
        self.companies.append(Company())
        self.companies.append(Company())
        self.companies.append(Company())
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
        stateBtn.setGeometry(0, 70, 240, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(240, 70, 240, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('회사', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(480, 70, 240, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        postBtn = QPushButton('취업의뢰', self.w)
        postBtn.setFont(QFont(self.basicInfo.font1, 13))
        postBtn.setGeometry(720, 70, 240, 50)
        postBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내 정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(960, 70, 240, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        stateBtn.clicked.connect(self.state)
        noticeBtn.clicked.connect(self.notice)
        companyBtn.clicked.connect(self.company)
        postBtn.clicked.connect(self.post)
        infoBtn.clicked.connect(self.info)

        company_width = 800
        address_width = 200

        listX = 100
        listY = 180
        blankHeigth = 40

        fontsize = 12

        i = 0

        company_header = QPushButton("회사명", self.w)
        company_header.setFont(QFont(self.basicInfo.font1, fontsize))
        company_header.setGeometry(listX, listY + blankHeigth * i, company_width + 1, blankHeigth + 1)
        company_header.setStyleSheet(
            'background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        address_header = QPushButton("분야", self.w)
        address_header.setFont(QFont(self.basicInfo.font1, fontsize))
        address_header.setGeometry(listX + company_width, listY + blankHeigth * i, address_width + 1, blankHeigth + 1)
        address_header.setStyleSheet(
            'background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        self.company = []
        self.address = []

        # 0
        i = 0
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.company[i].clicked.connect(lambda v: self.func(0))

        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.address[i].clicked.connect(lambda v: self.func(0))

        # 1
        i += 1
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.company[i].clicked.connect(lambda v: self.func(1))

        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.address[i].clicked.connect(lambda v: self.func(1))

        # 2
        i += 1
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.company[i].clicked.connect(lambda v: self.func(2))

        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.address[i].clicked.connect(lambda v: self.func(2))

        # 3
        i += 1
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.company[i].clicked.connect(lambda v: self.func(3))

        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.address[i].clicked.connect(lambda v: self.func(3))

        # 4
        i += 1
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.company[i].clicked.connect(lambda v: self.func(4))

        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.address[i].clicked.connect(lambda v: self.func(4))

        # 5
        i += 1
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.company[i].clicked.connect(lambda v: self.func(5))

        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.address[i].clicked.connect(lambda v: self.func(5))

        # 6
        i += 1
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.company[i].clicked.connect(lambda v: self.func(6))
        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.address[i].clicked.connect(lambda v: self.func(6))

        # 7
        i += 1
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.company[i].clicked.connect(lambda v: self.func(7))

        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.address[i].clicked.connect(lambda v: self.func(7))

        # 8
        i += 1
        self.company.append('')
        self.company[i] = QPushButton(self.companies[i].companyname, self.w)
        self.company[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.company[i].setGeometry(listX, listY + blankHeigth * (i + 1), company_width + 1, blankHeigth + 1)
        self.company[i].setStyleSheet(
            'background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px;text-align: left; border-bottom:2px solid #ababab; padding-left: 30px; ')
        self.company[i].clicked.connect(lambda v: self.func(8))
        self.address.append('')
        self.address[i] = QPushButton(self.companies[i].address, self.w)
        self.address[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.address[i].setGeometry(listX + company_width, listY + blankHeigth * (i + 1), address_width + 1,
                                    blankHeigth + 1)
        self.address[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; border-bottom:2px solid #ababab;')
        self.address[i].clicked.connect(lambda v: self.func(8))

        prevPageBtn = QPushButton("<", self.w)
        prevPageBtn.setFont(QFont(self.basicInfo.font1, 14))
        prevPageBtn.setGeometry(430, 600, 15, 20)
        prevPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        prevPageBtn.clicked.connect(self.prevPage)

        self.pageBtn_1 = QPushButton(self.currentpage > 2 and str(self.currentpage - 2) or '', self.w)
        self.pageBtn_1.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_1.setGeometry(470, 600, 15, 20)
        self.pageBtn_1.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_1.clicked.connect(self.prev2Page)

        self.pageBtn_2 = QPushButton(self.currentpage > 1 and str(self.currentpage - 1) or '', self.w)
        self.pageBtn_2.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_2.setGeometry(510, 600, 15, 20)
        self.pageBtn_2.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_2.clicked.connect(self.prev1Page)

        self.currentPageBtn = QPushButton(str(self.currentpage), self.w)
        self.currentPageBtn.setFont(QFont(self.basicInfo.font1, fontsize))
        self.currentPageBtn.setGeometry(550, 600, 15, 20)
        self.currentPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); font-weight: bold;')
        self.currentPageBtn.clicked.connect(self.currentPage)

        self.pageBtn_3 = QPushButton(self.pageCount >= self.currentpage + 1 and str(self.currentpage + 1) or '', self.w)
        self.pageBtn_3.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_3.setGeometry(590, 600, 15, 20)
        self.pageBtn_3.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_3.clicked.connect(self.next1Page)

        self.pageBtn_4 = QPushButton(self.pageCount >= self.currentpage + 2 and str(self.currentpage + 2) or '', self.w)
        self.pageBtn_4.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_4.setGeometry(630, 600, 15, 20)
        self.pageBtn_4.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_4.clicked.connect(self.next2Page)

        nextPageBtn = QPushButton(">", self.w)
        nextPageBtn.setFont(QFont(self.basicInfo.font1, 14))
        nextPageBtn.setGeometry(670, 600, 15, 20)
        nextPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        nextPageBtn.clicked.connect(self.nextPage)

    def prevPage(self):
        if (self.currentpage - 1 >= 1):
            self.currentpage -= 1
            self.getNoticeData()
            self.setPageText()

    def prev2Page(self):
        if (self.currentpage - 2 >= 1):
            self.currentpage -= 2
            self.getNoticeData()
            self.setPageText()

    def prev1Page(self):
        if (self.currentpage - 1 >= 1):
            self.currentpage -= 1
            self.getNoticeData()
            self.setPageText()

    def currentPage(self):
        self.setPageText()

    def next1Page(self):
        if (self.currentpage + 1 <= self.pageCount):
            self.currentpage += 1
            self.getNoticeData()
            self.setPageText()

    def next2Page(self):
        if (self.currentpage + 2 <= self.pageCount):
            self.currentpage += 2
            self.getNoticeData()
            self.setPageText()

    def nextPage(self):
        if (self.currentpage + 1 <= self.pageCount):
            self.currentpage += 1
            self.getNoticeData()
            self.setPageText()

    def setPageText(self):
        self.close()
        self.show()
        self.pageBtn_1.setText(self.currentpage > 2 and str(self.currentpage - 2) or '')
        self.pageBtn_2.setText(self.currentpage > 1 and str(self.currentpage - 1) or '')
        self.currentPageBtn.setText(str(self.currentpage))
        self.pageBtn_3.setText(self.pageCount >= self.currentpage + 1 and str(self.currentpage + 1) or '')
        self.pageBtn_4.setText(self.pageCount >= self.currentpage + 2 and str(self.currentpage + 2) or '')

        for i in range(self.list_len):
            self.company()[i].setText(self.companies[i].company)
            self.address[i].setText(self.companies[i].address)

    def getNoticeData(self):
        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()

        sql = "SELECT * FROM eiom_db.company;"
        curs.execute(sql)

        rows = curs.fetchall()

        for i in range((self.currentpage - 1) * 9, self.currentpage * 9):
            if i < len(rows):
                self.companies[i % 9].companyname = rows[i][0]
                self.companies[i % 9].id = rows[i][1]
                self.companies[i%9].address=rows[i][3]
                self.companies[i % 9].annualsales = rows[i][4]
                self.companies[i % 9].web = rows[i][5]
                self.companies[i % 9].introduce = rows[i][9]
                self.companies[i % 9].major = rows[i][10]
                self.companies[i % 9].employees_num = rows[i][14]
            else:
                self.companies[i % 9].companyname = ''
                self.companies[i % 9].id =''
                self.companies[i % 9].address = ''
                self.companies[i % 9].annualsales = ''
                self.companies[i % 9].web =''
                self.companies[i % 9].introduce = ''
                self.companies[i % 9].major = ''
                self.companies[i % 9].employees_num =''

        self.pageCount = len(rows) // 9 + 1

        conn.close()

    def state(self):
        self.sr = student.Rate.sRate()
        self.sr.show()
        self.hide()

    def notice(self):
        self.nl = student.NoticeList.noticeList()
        self.nl.show()
        self.hide()

    def company(self):
        print('아직')

    def post(self):
        print('아직')

    def info(self):
        self.mp = student.MyPage.MyPage()
        self.mp.show()
        self.hide()

    def func(self, companyNum):
        try:
            self.cp = student.CompanyPost.CompanyPost(self.companies[companyNum])
            self.cp.show()
            self.hide()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CompanyList()
    ex.show()
    app.exec_()