
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo
import student.Rate
import student.NoticeList
import student.MyPage
from student.Company import Company
from student.EmploymentRequest import EmploymentRequest


class EmploymentRequestPost(QWidget):

    def __init__(self, reque=EmploymentRequest()):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)
        self.reque = reque
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, 1200)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/background.png")))
        self.w.setPalette(palette)

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

        contTitle = QLabel(self.reque.company_name+'\n', self.w)
        contTitle.setFont(QFont(self.basicInfo.font1, 13))
        contTitle.setGeometry(100, 150, 1000, 90)
        contTitle.setStyleSheet('border-top:1px solid black; border-bottom:1px solid black; ')
        contTitle.setAlignment(QtCore.Qt.AlignCenter)

        writer = QLabel(self.reque.company_id, contTitle)
        writer.setFont(QFont(self.basicInfo.font1, 10))
        writer.setGeometry(0, 60, 1000, 20)
        writer.setStyleSheet('color:gray; border:0px;')
        writer.setAlignment(QtCore.Qt.AlignCenter)

        t1 = QLabel('회사 정보', self.w)
        t1.setFont(QFont(self.basicInfo.font1, 15))
        t1.setGeometry(100, 260, 500, 40)

        t2 = QLabel('담당자 정보', self.w)
        t2.setFont(QFont(self.basicInfo.font1, 15))
        t2.setGeometry(600, 260, 500, 40)

        t3 = QLabel('현장 실습 정보', self.w)
        t3.setFont(QFont(self.basicInfo.font1, 15))
        t3.setGeometry(600, 450, 500, 40)

        t4 = QLabel('모집 형태', self.w)
        t4.setFont(QFont(self.basicInfo.font1, 15))
        t4.setGeometry(100, 900, 500, 40)

        t5 = QLabel('근무 형태', self.w)
        t5.setFont(QFont(self.basicInfo.font1, 15))
        t5.setGeometry(600, 650, 500, 40)

        cNameL1 = QLabel("기업명", self.w)
        cNameL1.setFont(QFont(self.basicInfo.font1, 13))
        cNameL1.setGeometry(130, 320, 500, 40)

        cNameL2 = QLabel(self.reque.company_name, self.w)
        cNameL2.setFont(QFont(self.basicInfo.font1, 13))
        cNameL2.setGeometry(230, 320, 500, 40)

        cintroL = QLabel("기업 소개", self.w)
        cintroL.setFont(QFont(self.basicInfo.font1, 13))
        cintroL.setGeometry(130, 370, 500, 40)

        cintro = QTextBrowser(self.w)
        st = self.reque.company_intro.split("\\n")
        for i in st:
            cintro.append(i)
        cintro.setFont(QFont(self.basicInfo.font1, 12))
        cintro.setGeometry(130, 420, 400, 200)

        majorL1 = QLabel("분야", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 13))
        majorL1.setGeometry(130, 630, 500, 40)

        majorL2 = QLabel(self.reque.company_major, self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 13))
        majorL2.setGeometry(230, 630, 500, 40)

        salesL1 = QLabel("연 매출", self.w)
        salesL1.setFont(QFont(self.basicInfo.font1, 13))
        salesL1.setGeometry(130, 680, 500, 40)

        salesL2 = QLabel(self.reque.company_annualsale, self.w)
        salesL2.setFont(QFont(self.basicInfo.font1, 13))
        salesL2.setGeometry(230, 680, 500, 40)

        employeeL1 = QLabel("사원수", self.w)
        employeeL1.setFont(QFont(self.basicInfo.font1, 13))
        employeeL1.setGeometry(130, 720, 500, 40)

        employeeL2 = QLabel(str(self.reque.company_employees_num), self.w)
        employeeL2.setFont(QFont(self.basicInfo.font1, 13))
        employeeL2.setGeometry(230, 720, 500, 40)

        addressL1 = QLabel("위치", self.w)
        addressL1.setFont(QFont(self.basicInfo.font1, 13))
        addressL1.setGeometry(130, 770, 500, 40)

        addressL2 = QLabel(self.reque.company_address, self.w)
        addressL2.setFont(QFont(self.basicInfo.font1, 13))
        addressL2.setGeometry(230, 770, 500, 40)

        webL1 = QLabel("웹사이트", self.w)
        webL1.setFont(QFont(self.basicInfo.font1, 13))
        webL1.setGeometry(130, 830, 500, 40)

        webL2 = QLabel(self.reque.company_web, self.w)
        webL2.setFont(QFont(self.basicInfo.font1, 13))
        webL2.setGeometry(230, 830, 500, 40)

        personEL1 = QLabel("e-mail", self.w)
        personEL1.setFont(QFont(self.basicInfo.font1, 13))
        personEL1.setGeometry(630, 320, 500, 40)

        personEL2 = QLabel(self.reque.manager_email, self.w)
        personEL2.setFont(QFont(self.basicInfo.font1, 13))
        personEL2.setGeometry(750, 320, 500, 40)

        personPL1 = QLabel("전화번호", self.w)
        personPL1.setFont(QFont(self.basicInfo.font1, 13))
        personPL1.setGeometry(630, 370, 500, 40)

        personPL2 = QLabel(self.reque.manager_ph, self.w)
        personPL2.setFont(QFont(self.basicInfo.font1, 13))
        personPL2.setGeometry(750, 370, 500, 40)

        periodL1 = QLabel("현장 실습 기간", self.w)
        periodL1.setFont(QFont(self.basicInfo.font1, 13))
        periodL1.setGeometry(630, 520, 500, 40)

        periodL2 = QLabel(self.reque.period, self.w)
        periodL2.setFont(QFont(self.basicInfo.font1, 13))
        periodL2.setGeometry(780, 520, 500, 40)

        pmoneyL1 = QLabel("현장 실습 수당", self.w)
        pmoneyL1.setFont(QFont(self.basicInfo.font1, 13))
        pmoneyL1.setGeometry(630, 570, 500, 40)

        pmoneyL2 = QLabel(self.reque.pmoney, self.w)
        pmoneyL2.setFont(QFont(self.basicInfo.font1, 13))
        pmoneyL2.setGeometry(780, 570, 500, 40)

        receiptL1 = QLabel("모집 기간", self.w)
        receiptL1.setFont(QFont(self.basicInfo.font1, 13))
        receiptL1.setGeometry(130, 950, 500, 40)

        receiptL2 = QLabel(self.reque.recruit, self.w)
        receiptL2.setFont(QFont(self.basicInfo.font1, 13))
        receiptL2.setGeometry(230, 950, 500, 40)

        hopeCountL1 = QLabel("희망 인원", self.w)
        hopeCountL1.setFont(QFont(self.basicInfo.font1, 13))
        hopeCountL1.setGeometry(130, 1000, 500, 40)

        hopeCountL2 = QLabel(str(self.reque.hopeperson), self.w)
        hopeCountL2.setFont(QFont(self.basicInfo.font1, 13))
        hopeCountL2.setGeometry(230, 1000, 500, 40)

        rightL1 = QLabel("지원 자격", self.w)
        rightL1.setFont(QFont(self.basicInfo.font1, 13))
        rightL1.setGeometry(130, 1100, 500, 40)

        rightL2 = QLabel(self.reque.apply, self.w)
        rightL2.setFont(QFont(self.basicInfo.font1, 13))
        rightL2.setGeometry(230, 1100, 500, 40)

        royaltyL1 = QLabel("우대 사항", self.w)
        royaltyL1.setFont(QFont(self.basicInfo.font1, 13))
        royaltyL1.setGeometry(130, 1050, 500, 40)

        royaltyL2 = QLabel(self.reque.royalty, self.w)
        royaltyL2.setFont(QFont(self.basicInfo.font1, 13))
        royaltyL2.setGeometry(230, 1050, 500, 40)

        postL1 = QLabel("제출서류", self.w)
        postL1.setFont(QFont(self.basicInfo.font1, 13))
        postL1.setGeometry(130, 1150, 500, 40)

        postL2 = QLabel(self.reque.document, self.w)
        postL2.setFont(QFont(self.basicInfo.font1, 13))
        postL2.setGeometry(230, 1150, 500, 40)

        useLangL1 = QLabel("사용 언어", self.w)
        useLangL1.setFont(QFont(self.basicInfo.font1, 13))
        useLangL1.setGeometry(630, 700, 500, 40)

        useLangL2 = QLabel(self.reque.uselang, self.w)
        useLangL2.setFont(QFont(self.basicInfo.font1, 13))
        useLangL2.setGeometry(730, 700, 500, 40)

        employmentL1 = QLabel("고용 형태", self.w)
        employmentL1.setFont(QFont(self.basicInfo.font1, 13))
        employmentL1.setGeometry(630, 750, 500, 40)

        employmentL2 = QLabel(self.reque.employment, self.w)
        employmentL2.setFont(QFont(self.basicInfo.font1, 13))
        employmentL2.setGeometry(730, 750, 500, 40)

        workL1 = QLabel("담당 업무", self.w)
        workL1.setFont(QFont(self.basicInfo.font1, 13))
        workL1.setGeometry(630, 800, 500, 40)

        workL2 = QLabel(self.reque.work, self.w)
        workL2.setFont(QFont(self.basicInfo.font1, 13))
        workL2.setGeometry(730, 800, 500, 40)

        workTimeL1 = QLabel("업무 시간", self.w)
        workTimeL1.setFont(QFont(self.basicInfo.font1, 13))
        workTimeL1.setGeometry(630, 850, 500, 40)

        workTimeL2 = QLabel(self.reque.worktime, self.w)
        workTimeL2.setFont(QFont(self.basicInfo.font1, 13))
        workTimeL2.setGeometry(730, 850, 500, 40)

        moneyL1 = QLabel("급여", self.w)
        moneyL1.setFont(QFont(self.basicInfo.font1, 13))
        moneyL1.setGeometry(630, 900, 500, 40)

        moneyL2 = QLabel(self.reque.money, self.w)
        moneyL2.setFont(QFont(self.basicInfo.font1, 13))
        moneyL2.setGeometry(730, 900, 500, 40)

        benefitL1 = QLabel("복리후생", self.w)
        benefitL1.setFont(QFont(self.basicInfo.font1, 13))
        benefitL1.setGeometry(630, 950, 500, 40)

        benefitL2 = QTextBrowser(self.w)
        st = self.reque.benefit.split("\\n")
        for i in st:
            benefitL2.append(i)
        benefitL2.setFont(QFont(self.basicInfo.font1, 12))
        benefitL2.setGeometry(630, 1000, 400, 200)


        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.w)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        vLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vLayout)

        self.show()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = EmploymentRequestPost()
    ex.show()
    sys.exit(app.exec_())
