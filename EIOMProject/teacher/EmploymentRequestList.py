import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

import student.NoticeContent
from BasicInfo import BasicInfo, BasicDB
import student.Rate
import student.NoticeList
import student.MyPage
from teacher.EmploymentRequest import EmploymentRequest


class noticeList(QWidget):
    currentpage = 1
    pageCount = 0
    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.list_len = 9
        self.reque=[]
        for i in range(self.list_len):
            self.reque.append(EmploymentRequest())
        self.getNoticeData()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
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


        companyName_width = 200
        useLanquage_width = 200
        recruit_width = 400
        emplayment_width = 150
        address_width = 150
        hopePersonCount_width = 150

        listX = 100
        listY = 180
        blankHeigth = 40

        fontsize = 12

        i = -1


        title_header = QPushButton("회사명", self.w)
        title_header.setFont(QFont(self.basicInfo.font1, fontsize))
        title_header.setGeometry(listX, listY+blankHeigth*(i+1), companyName_width+1, blankHeigth+1)
        title_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        writer_header = QPushButton("사용언어", self.w)
        writer_header.setFont(QFont(self.basicInfo.font1, fontsize))
        writer_header.setGeometry(listX + companyName_width, listY+blankHeigth*(i+1), useLanquage_width+1, blankHeigth+1)
        writer_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        date_header = QPushButton("기간", self.w)
        date_header.setFont(QFont(self.basicInfo.font1, fontsize))
        date_header.setGeometry(listX + companyName_width + useLanquage_width, listY+blankHeigth*(i+1), recruit_width+1, blankHeigth+1)
        date_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        date_header = QPushButton("고용형태", self.w)
        date_header.setFont(QFont(self.basicInfo.font1, fontsize))
        date_header.setGeometry(listX + companyName_width + useLanquage_width + recruit_width, listY+blankHeigth*(i+1), emplayment_width+1, blankHeigth+1)
        date_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        date_header = QPushButton("위치", self.w)
        date_header.setFont(QFont(self.basicInfo.font1, fontsize))
        date_header.setGeometry(listX + companyName_width + useLanquage_width + recruit_width + emplayment_width, listY+blankHeigth*(i+1), address_width+1, blankHeigth+1)
        date_header.setStyleSheet('background-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        date_header = QPushButton("희망인원", self.w)
        date_header.setFont(QFont(self.basicInfo.font1, fontsize))
        date_header.setGeometry(listX + companyName_width + useLanquage_width + recruit_width+ emplayment_width + address_width, listY+blankHeigth*(i+1), hopePersonCount_width+1, blankHeigth+1)
        date_header.setStyleSheet('companyName_width-color: rgb(255,255,255); border-left: 0px; border-right: 0px; border-top: 2px solid #ababab; border-bottom: 2px solid #ababab; ')

        self.title = []
        self.writer = []
        self.date = []



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

        sql = "select * from employment_request;"
        curs.execute(sql)

        rows = curs.fetchall()


        for i in range((self.currentpage-1)*9, self.currentpage*9):
            if i < len(rows):
                self.reque[i%9].id = rows[i][0]
                self.reque[i%9].company_id = rows[i][1]
                self.reque[i%9].recruit = rows[i][2]
                self.reque[i%9].hopeperson = rows[i][3]
                self.reque[i%9].apply = rows[i][4]
                self.reque[i%9].royalty = rows[i][5]
                self.reque[i%9].document = rows[i][6]
                self.reque[i%9].uselang = rows[i][7]
                self.reque[i%9].employment = rows[i][8]
                self.reque[i%9].work = rows[i][9]
                self.reque[i%9].money = rows[i][10]
                self.reque[i%9].worktime = rows[i][11]
                self.reque[i%9].benefit = rows[i][12]
                self.reque[i%9].period = rows[i][13]
                self.reque[i%9].pmoney = rows[i][14]
                self.reque[i%9].manager_email = rows[i][15]
                self.reque[i%9].manager_ph = rows[i][16]
                curs2 = conn.cursor()
                sql2 = "select * from company Where id='"+ self.reque[i%9].company_id +"';"
                curs2.execute(sql2)
                rows2 = curs.fetchall()
                self.reque[i%9].company_name = rows2[0][0]
                self.reque[i%9].company_address = rows2[0][3]
                self.reque[i%9].company_annualsale = rows2[0][4]
                self.reque[i%9].company_web = rows2[0][5]
                self.reque[i%9].company_intro = rows2[0][9]
                self.reque[i%9].company_major = rows2[0][10]
                self.reque[i%9].company_employees_num = rows2[0][14]

            else:
                self.reque[i%9].id = ''
                self.reque[i%9].company_id = ''
                self.reque[i%9].recruit = ''
                self.reque[i%9].hopeperson = ''
                self.reque[i%9].apply = ''
                self.reque[i%9].royalty = ''
                self.reque[i%9].document = ''
                self.reque[i%9].uselang = ''
                self.reque[i%9].employment = ''
                self.reque[i%9].work = ''
                self.reque[i%9].money = ''
                self.reque[i%9].worktime = ''
                self.reque[i%9].benefit = ''
                self.reque[i%9].period = ''
                self.reque[i%9].pmoney = ''
                self.reque[i%9].manager_email = ''
                self.reque[i%9].manager_ph = ''
                self.reque[i%9].company_name = ''
                self.reque[i%9].company_address = ''
                self.reque[i%9].company_annualsale = ''
                self.reque[i%9].company_web = ''
                self.reque[i%9].company_intro = ''
                self.reque[i%9].company_major = ''
                self.reque[i%9].company_employees_num = ''

        self.pageCount = len(rows) // 9 + 1

        conn.close()

    def func(self, noticeNum):
        try:
            self.cp = student.NoticeContent.NoticeContent(self.notices[noticeNum])
            self.cp.show()
            self.hide()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = noticeList()
    sys.exit(app.exec_())
