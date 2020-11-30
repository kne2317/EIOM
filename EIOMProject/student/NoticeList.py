import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

import student.NoticeContent
from BasicInfo import BasicInfo, BasicDB
from student.Notice import Notice


class noticeList(QWidget):
    currentpage = 1
    pageCount = 0
    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.list_len = 9
        self.notices=[]
        self.notices.append(Notice())
        self.notices.append(Notice())
        self.notices.append(Notice())
        self.notices.append(Notice())
        self.notices.append(Notice())
        self.notices.append(Notice())
        self.notices.append(Notice())
        self.notices.append(Notice())
        self.notices.append(Notice())
        self.getNoticeData()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
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

        title_width = 600
        writer_width = 200
        date_width = 200

        listX = 100
        listY = 180
        blankHeigth = 40

        fontsize = 12

        i = 0


        title_header = QPushButton("제목", self.w)
        title_header.setFont(QFont(self.basicInfo.font1, fontsize))
        title_header.setGeometry(listX, listY+blankHeigth*i, title_width+1, blankHeigth+1)
        title_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        writer_header = QPushButton("작성자", self.w)
        writer_header.setFont(QFont(self.basicInfo.font1, fontsize))
        writer_header.setGeometry(listX + title_width, listY+blankHeigth*i, writer_width+1, blankHeigth+1)
        writer_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        date_header = QPushButton("작성일", self.w)
        date_header.setFont(QFont(self.basicInfo.font1, fontsize))
        date_header.setGeometry(listX + title_width + writer_width, listY+blankHeigth*i, date_width, blankHeigth+1)
        date_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        self.title = []
        self.writer = []
        self.date = []

        #0
        i=0
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY+blankHeigth*(i+1), title_width+1, blankHeigth+1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(0))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY+blankHeigth*(i+1), writer_width+1, blankHeigth+1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(0))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY+blankHeigth*(i+1), date_width, blankHeigth+1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.date[i].clicked.connect(lambda v: self.func(0))

        #1
        i+=1
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY + blankHeigth * (i + 1), title_width + 1, blankHeigth + 1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(1))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY + blankHeigth * (i + 1), writer_width + 1, blankHeigth + 1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(1))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY + blankHeigth * (i + 1), date_width, blankHeigth + 1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.date[i].clicked.connect(lambda v: self.func(1))

        #2
        i+=1
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY + blankHeigth * (i + 1), title_width + 1, blankHeigth + 1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(2))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY + blankHeigth * (i + 1), writer_width + 1, blankHeigth + 1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(2))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY + blankHeigth * (i + 1), date_width, blankHeigth + 1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.date[i].clicked.connect(lambda v: self.func(2))

        #3
        i+=1
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY + blankHeigth * (i + 1), title_width + 1, blankHeigth + 1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(3))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY + blankHeigth * (i + 1), writer_width + 1, blankHeigth + 1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(3))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY + blankHeigth * (i + 1), date_width, blankHeigth + 1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.date[i].clicked.connect(lambda v: self.func(3))

        #4
        i+=1
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY + blankHeigth * (i + 1), title_width + 1, blankHeigth + 1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(4))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY + blankHeigth * (i + 1), writer_width + 1, blankHeigth + 1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(4))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY + blankHeigth * (i + 1), date_width, blankHeigth + 1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.date[i].clicked.connect(lambda v: self.func(4))

        #5
        i+=1
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY + blankHeigth * (i + 1), title_width + 1, blankHeigth + 1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(5))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY + blankHeigth * (i + 1), writer_width + 1, blankHeigth + 1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(5))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY + blankHeigth * (i + 1), date_width, blankHeigth + 1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.date[i].clicked.connect(lambda v: self.func(5))

        #6
        i+=1
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY + blankHeigth * (i + 1), title_width + 1, blankHeigth + 1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(6))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY + blankHeigth * (i + 1), writer_width + 1, blankHeigth + 1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(6))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY + blankHeigth * (i + 1), date_width, blankHeigth + 1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.date[i].clicked.connect(lambda v: self.func(6))

        #7
        i+=1
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY + blankHeigth * (i + 1), title_width + 1, blankHeigth + 1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(7))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY + blankHeigth * (i + 1), writer_width + 1, blankHeigth + 1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(7))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY + blankHeigth * (i + 1), date_width, blankHeigth + 1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.date[i].clicked.connect(lambda v: self.func(7))

        #8
        i+=1
        self.title.append('')
        self.title[i] = QPushButton(self.notices[i].title, self.w)
        self.title[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.title[i].setGeometry(listX, listY + blankHeigth * (i + 1), title_width + 1, blankHeigth + 1)
        self.title[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; text-align: left; padding-left: 30px;')
        self.title[i].clicked.connect(lambda v: self.func(8))

        self.writer.append('')
        self.writer[i] = QPushButton(self.notices[i].writer, self.w)
        self.writer[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.writer[i].setGeometry(listX + title_width, listY + blankHeigth * (i + 1), writer_width + 1, blankHeigth + 1)
        self.writer[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; ')
        self.writer[i].clicked.connect(lambda v: self.func(8))

        self.date.append('')
        self.date[i] = QPushButton(str(self.notices[i].date), self.w)
        self.date[i].setFont(QFont(self.basicInfo.font1, fontsize))
        self.date[i].setGeometry(listX + title_width + writer_width, listY + blankHeigth * (i + 1), date_width, blankHeigth + 1)
        self.date[i].setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; border-left: 0px;border-right: 0px; border-bottom:2px solid #ababab; ')
        self.date[i].clicked.connect(lambda v: self.func(8))



        prevPageBtn = QPushButton("<", self.w)
        prevPageBtn.setFont(QFont(self.basicInfo.font1, 14))
        prevPageBtn.setGeometry(430, 600, 15, 20)
        prevPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        prevPageBtn.clicked.connect(self.prevPage)

        self.pageBtn_1 = QPushButton(self.currentpage>2 and str(self.currentpage-2) or '', self.w)
        self.pageBtn_1.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_1.setGeometry(470, 600, 15, 20)
        self.pageBtn_1.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_1.clicked.connect(self.prev2Page)

        self.pageBtn_2 = QPushButton(self.currentpage>1 and str(self.currentpage-1) or '', self.w)
        self.pageBtn_2.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_2.setGeometry(510, 600, 15, 20)
        self.pageBtn_2.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_2.clicked.connect(self.prev1Page)

        self.currentPageBtn = QPushButton(str(self.currentpage), self.w)
        self.currentPageBtn.setFont(QFont(self.basicInfo.font1, fontsize))
        self.currentPageBtn.setGeometry(550, 600, 15, 20)
        self.currentPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); font-weight: bold;')
        self.currentPageBtn.clicked.connect(self.currentPage)

        self.pageBtn_3 = QPushButton(self.pageCount >= self.currentpage+1 and str(self.currentpage+1) or '', self.w)
        self.pageBtn_3.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_3.setGeometry(590, 600, 15, 20)
        self.pageBtn_3.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_3.clicked.connect(self.next1Page)

        self.pageBtn_4 = QPushButton(self.pageCount >= self.currentpage+2 and str(self.currentpage+2) or '', self.w)
        self.pageBtn_4.setFont(QFont(self.basicInfo.font1, fontsize))
        self.pageBtn_4.setGeometry(630, 600, 15, 20)
        self.pageBtn_4.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        self.pageBtn_4.clicked.connect(self.next2Page)

        nextPageBtn = QPushButton(">", self.w)
        nextPageBtn.setFont(QFont(self.basicInfo.font1, 14))
        nextPageBtn.setGeometry(670, 600, 15, 20)
        nextPageBtn.setStyleSheet('background-color: rgba(255,255,255, 0); ')
        nextPageBtn.clicked.connect(self.nextPage)


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

    def setPageText(self):
        self.close()
        self.show()
        self.pageBtn_1.setText(self.currentpage>2 and str(self.currentpage-2) or '')
        self.pageBtn_2.setText(self.currentpage>1 and str(self.currentpage-1) or '')
        self.currentPageBtn.setText(str(self.currentpage))
        self.pageBtn_3.setText(self.pageCount >= self.currentpage+1 and str(self.currentpage+1) or '')
        self.pageBtn_4.setText(self.pageCount >= self.currentpage+2 and str(self.currentpage+2) or '')

        for i in range(self.list_len):
            self.title[i].setText(self.notices[i].title)
            self.writer[i].setText(self.notices[i].writer)
            self.date[i].setText(str(self.notices[i].date))


    def getNoticeData(self):
        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()

        sql = "select * from notice order by date desc;"
        curs.execute(sql)

        rows = curs.fetchall()

        for i in range((self.currentpage-1)*9, self.currentpage*9):
            if i < len(rows):
                self.notices[i%9].id = rows[i][0]
                self.notices[i%9].writer = rows[i][1]
                self.notices[i%9].date = rows[i][2]
                self.notices[i%9].title = rows[i][3]
                self.notices[i%9].content = rows[i][4]
            else:
                self.notices[i%9].id = ''
                self.notices[i%9].writer = ''
                self.notices[i%9].date = ''
                self.notices[i%9].title = ''
                self.notices[i%9].content = ''

        self.pageCount = len(rows) % 9 + 1

        conn.close()

    def func(self, noticeNum):
        self.contentPage = student.NoticeContent.NoticeContent(self.notices[noticeNum])
        self.contentPage.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = noticeList()
    sys.exit(app.exec_())
