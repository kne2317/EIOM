import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
from BasicInfo import BasicInfo
from company.Company import Request
from company.Company import Company
import company.NoneEmployementRequest
import company.CompanyEmploymentRequest
import company.CompanyInfo
import company.NonePofol
import company.PofolList
class CompanyEmploymentRequest(QWidget):

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, 1300)
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

        stateBtn = QPushButton('취업의뢰', self.w)
        stateBtn.setFont(QFont(self.basicInfo.font1, 13))
        stateBtn.setGeometry(0, 70, self.basicInfo.WindowWidth / 3, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        pfBtn = QPushButton('포트폴리오', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(self.basicInfo.WindowWidth / 3 * 1, 70, self.basicInfo.WindowWidth / 3, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내 정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(self.basicInfo.WindowWidth / 3 * 2, 70, self.basicInfo.WindowWidth / 3, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        contTitle = QLabel('@@@ soft \n', self.w)
        contTitle.setFont(QFont(self.basicInfo.font1, 13))
        contTitle.setGeometry(100, 150, 1000, 90)
        contTitle.setStyleSheet('border-top:1px solid black; border-bottom:1px solid black; ')
        contTitle.setAlignment(QtCore.Qt.AlignCenter)
        contTitle.setText(Company.companyname)

        writer = QLabel('@@@ soft', contTitle)
        writer.setFont(QFont(self.basicInfo.font1, 10))
        writer.setGeometry(0, 60, 1000, 20)
        writer.setStyleSheet('color:gray; border:0px;')
        writer.setAlignment(QtCore.Qt.AlignCenter)
        writer.setText(Company.ID)

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

        cNameL2 = QLabel("연지 소프트", self.w)
        cNameL2.setFont(QFont(self.basicInfo.font1, 13))
        cNameL2.setGeometry(230, 320, 500, 40)
        cNameL2.setText(Company.companyname)

        cintroL = QLabel("기업 소개", self.w)
        cintroL.setFont(QFont(self.basicInfo.font1, 13))
        cintroL.setGeometry(130, 370, 500, 40)

        cintro = QTextBrowser(self.w)
        cintro.setFont(QFont(self.basicInfo.font1, 12))
        cintro.setGeometry(130, 420, 400, 200)
        cintro.setText(Company.introduce)

        majorL1 = QLabel("분야", self.w)
        majorL1.setFont(QFont(self.basicInfo.font1, 13))
        majorL1.setGeometry(130, 630, 500, 40)

        majorL2 = QLabel("개발", self.w)
        majorL2.setFont(QFont(self.basicInfo.font1, 13))
        majorL2.setGeometry(230, 630, 500, 40)
        majorL2.setText(Company.major)

        salesL1 = QLabel("연 매출", self.w)
        salesL1.setFont(QFont(self.basicInfo.font1, 13))
        salesL1.setGeometry(130, 680, 500, 40)

        salesL2 = QLabel("10억", self.w)
        salesL2.setFont(QFont(self.basicInfo.font1, 13))
        salesL2.setGeometry(230, 680, 500, 40)
        salesL2.setText(Company.annualsale)

        employeeL1 = QLabel("사원수", self.w)
        employeeL1.setFont(QFont(self.basicInfo.font1, 13))
        employeeL1.setGeometry(130, 720, 500, 40)

        employeeL2 = QLabel("10", self.w)
        employeeL2.setFont(QFont(self.basicInfo.font1, 13))
        employeeL2.setGeometry(230, 720, 500, 40)
        employeeL2.setText(str(Company.employees_num))

        addressL1 = QLabel("위치", self.w)
        addressL1.setFont(QFont(self.basicInfo.font1, 13))
        addressL1.setGeometry(130, 770, 500, 40)

        addressL2 = QLabel("남양주시 화도읍", self.w)
        addressL2.setFont(QFont(self.basicInfo.font1, 13))
        addressL2.setGeometry(230, 770, 500, 40)
        addressL2.setText(Company.address)

        webL1 = QLabel("웹사이트", self.w)
        webL1.setFont(QFont(self.basicInfo.font1, 13))
        webL1.setGeometry(130, 830, 500, 40)

        webL2 = QLabel("www.yj310.com", self.w)
        webL2.setFont(QFont(self.basicInfo.font1, 13))
        webL2.setGeometry(230, 830, 500, 40)
        webL2.setText(Company.web)

        personEL1 = QLabel("e-mail", self.w)
        personEL1.setFont(QFont(self.basicInfo.font1, 13))
        personEL1.setGeometry(630, 320, 500, 40)

        personEL2 = QLabel("s2019s17@e-mirim.hs.kr", self.w)
        personEL2.setFont(QFont(self.basicInfo.font1, 13))
        personEL2.setGeometry(750, 320, 500, 40)
        personEL2.setText(Request.manager_email)

        personPL1 = QLabel("전화번호", self.w)
        personPL1.setFont(QFont(self.basicInfo.font1, 13))
        personPL1.setGeometry(630, 370, 500, 40)

        personPL2 = QLabel("010-5037-2292", self.w)
        personPL2.setFont(QFont(self.basicInfo.font1, 13))
        personPL2.setGeometry(750, 370, 500, 40)
        personPL2.setText(Request.manager_ph)

        periodL1 = QLabel("현장 실습 기간", self.w)
        periodL1.setFont(QFont(self.basicInfo.font1, 13))
        periodL1.setGeometry(630, 520, 500, 40)

        periodL2 = QLabel("2개월", self.w)
        periodL2.setFont(QFont(self.basicInfo.font1, 13))
        periodL2.setGeometry(780, 520, 500, 40)
        periodL2.setText(Request.period)

        pmoneyL1 = QLabel("현장 실습 수당", self.w)
        pmoneyL1.setFont(QFont(self.basicInfo.font1, 13))
        pmoneyL1.setGeometry(630, 570, 500, 40)

        pmoneyL2 = QLabel("1500000", self.w)
        pmoneyL2.setFont(QFont(self.basicInfo.font1, 13))
        pmoneyL2.setGeometry(780, 570, 500, 40)
        pmoneyL2.setText(Request.pmoney)

        receiptL1 = QLabel("모집 기간", self.w)
        receiptL1.setFont(QFont(self.basicInfo.font1, 13))
        receiptL1.setGeometry(130, 950, 500, 40)

        receiptL2 = QLabel("2020.11.10~2020.11.30", self.w)
        receiptL2.setFont(QFont(self.basicInfo.font1, 13))
        receiptL2.setGeometry(230, 950, 500, 40)
        receiptL2.setText(Request.recruit)

        hopeCountL1 = QLabel("희망 인원", self.w)
        hopeCountL1.setFont(QFont(self.basicInfo.font1, 13))
        hopeCountL1.setGeometry(130, 1000, 500, 40)

        hopeCountL2 = QLabel("2", self.w)
        hopeCountL2.setFont(QFont(self.basicInfo.font1, 13))
        hopeCountL2.setGeometry(230, 1000, 500, 40)
        hopeCountL2.setText(str(Request.hopeperson))

        rightL1 = QLabel("지원 자격", self.w)
        rightL1.setFont(QFont(self.basicInfo.font1, 13))
        rightL1.setGeometry(130, 1100, 500, 40)

        rightL2 = QLabel("c++ 가능", self.w)
        rightL2.setFont(QFont(self.basicInfo.font1, 13))
        rightL2.setGeometry(230, 1100, 500, 40)
        rightL2.setText(Request.apply)

        royaltyL1 = QLabel("우대 사항", self.w)
        royaltyL1.setFont(QFont(self.basicInfo.font1, 13))
        royaltyL1.setGeometry(130, 1050, 500, 40)

        royaltyL2 = QLabel("cospro c++ 자격증 보유", self.w)
        royaltyL2.setFont(QFont(self.basicInfo.font1, 13))
        royaltyL2.setGeometry(230, 1050, 500, 40)
        royaltyL2.setText(Request.royalty)

        postL1 = QLabel("제출서류", self.w)
        postL1.setFont(QFont(self.basicInfo.font1, 13))
        postL1.setGeometry(130, 1150, 500, 40)

        postL2 = QLabel("이력서, 포트폴리오, 자기소개서", self.w)
        postL2.setFont(QFont(self.basicInfo.font1, 13))
        postL2.setGeometry(230, 1150, 500, 40)
        postL2.setText(Request.document)

        useLangL1 = QLabel("사용 언어", self.w)
        useLangL1.setFont(QFont(self.basicInfo.font1, 13))
        useLangL1.setGeometry(630, 700, 500, 40)

        useLangL2 = QLabel("c / c++", self.w)
        useLangL2.setFont(QFont(self.basicInfo.font1, 13))
        useLangL2.setGeometry(730, 700, 500, 40)
        useLangL2.setText(Request.uselang)

        employmentL1 = QLabel("고용 형태", self.w)
        employmentL1.setFont(QFont(self.basicInfo.font1, 13))
        employmentL1.setGeometry(630, 750, 500, 40)

        employmentL2 = QLabel("정규직", self.w)
        employmentL2.setFont(QFont(self.basicInfo.font1, 13))
        employmentL2.setGeometry(730, 750, 500, 40)
        employmentL2.setText(Request.employment)

        workL1 = QLabel("담당 업무", self.w)
        workL1.setFont(QFont(self.basicInfo.font1, 13))
        workL1.setGeometry(630, 800, 500, 40)

        workL2 = QLabel("c++을 이용한 개발", self.w)
        workL2.setFont(QFont(self.basicInfo.font1, 13))
        workL2.setGeometry(730, 800, 500, 40)
        workL2.setText(Request.work)

        workTimeL1 = QLabel("업무 시간", self.w)
        workTimeL1.setFont(QFont(self.basicInfo.font1, 13))
        workTimeL1.setGeometry(630, 850, 500, 40)

        workTimeL2 = QLabel("일 주 40시간 근무", self.w)
        workTimeL2.setFont(QFont(self.basicInfo.font1, 13))
        workTimeL2.setGeometry(730, 850, 500, 40)
        workTimeL2.setText(Request.worktime)

        moneyL1 = QLabel("급여", self.w)
        moneyL1.setFont(QFont(self.basicInfo.font1, 13))
        moneyL1.setGeometry(630, 900, 500, 40)

        moneyL2 = QLabel("연 2400", self.w)
        moneyL2.setFont(QFont(self.basicInfo.font1, 13))
        moneyL2.setGeometry(730, 900, 500, 40)
        moneyL2.setText(Request.money)

        benefitL1 = QLabel("복리후생", self.w)
        benefitL1.setFont(QFont(self.basicInfo.font1, 13))
        benefitL1.setGeometry(630, 950, 500, 40)

        benefitL2 = QTextBrowser(self.w)
        benefitL2.setFont(QFont(self.basicInfo.font1, 12))
        benefitL2.setGeometry(630, 1000, 400, 200)
        benefitL2.setText(Request.benefit)

        modifyBtn = QPushButton('수정', self.w)
        modifyBtn.setFont(QFont(self.basicInfo.font1, 12))
        modifyBtn.setGeometry(900, 1250, 130, 30)
        modifyBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.w)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        vLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vLayout)

        stateBtn.clicked.connect(self.state)
        pfBtn.clicked.connect(self.pf)
        infoBtn.clicked.connect(self.info)

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
            self.p = company.PofolList.pofolList()
            self.p.show()
            self.hide()

    def info(self):
        self.ci = company.CompanyInfo.CompanyInfo()
        self.ci.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CompanyEmploymentRequest()
    ex.show()
    app.exec_()
