import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
from BasicInfo import BasicInfo, BasicDB
import company.NoneEmployementRequest
import company.Company
import company.CompanyEmploymentRequest
import company.EmployeeRequestDB as db
class Post(QWidget):

    def __init__(self):
        super().__init__()
        self.basicInfo = BasicInfo()
        self.w = QWidget(self)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, 1500)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/background.png")))
        self.w.setPalette(palette)

        self.w.setLayout(layout)

        title = QLabel("취업 의뢰", self.w)
        title.setFont(QFont(self.basicInfo.font1, 20))
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setGeometry(100, 10, 1000, 50)

        la1 = QLabel('모집 형태',self.w)
        la1.setFont(QFont(self.basicInfo.font1,15))
        la1.setGeometry(100,80,100,50)

        la2 = QLabel('기간', self.w)
        la2.setFont(QFont(self.basicInfo.font1, 12))
        la2.setGeometry(100, 150, 100, 40)

        l = QLabel(" ~ ", self.w)
        l.setFont(QFont(self.basicInfo.font1, 15))
        l.setGeometry(640, 150, 500, 40)

        self.year1 = QLineEdit(self.w)
        self.year1.setPlaceholderText('연도')
        self.year1.setFont(QFont(self.basicInfo.font1, 13))
        self.year1.setGeometry(250, 150, 100, 40)

        self.month1 = QComboBox(self.w)
        self.month1.setFont(QFont(self.basicInfo.font1, 13))
        self.month1.setGeometry(380, 150, 100, 40)
        for i in range(0, 12):
            self.month1.addItem(str(i + 1) + "월")

        self.day1 = QComboBox(self.w)
        self.day1.setFont(QFont(self.basicInfo.font1, 13))
        self.day1.setGeometry(510, 150, 100, 40)
        for i in range(0, 30):
            self.day1.addItem(str(i + 1) + "일")

        self.year2 = QLineEdit(self.w)
        self.year2.setPlaceholderText('연도')
        self.year2.setFont(QFont(self.basicInfo.font1, 13))
        self.year2.setGeometry(690, 150, 100, 40)

        self.month2 = QComboBox(self.w)
        self.month2.setFont(QFont(self.basicInfo.font1, 13))
        self.month2.setGeometry(820, 150, 100, 40)
        for i in range(0, 12):
            self.month2.addItem(str(i + 1) + "월")

        self.day2 = QComboBox(self.w)
        self.day2.setFont(QFont(self.basicInfo.font1, 13))
        self.day2.setGeometry(950, 150, 100, 40)
        for i in range(0, 30):
            self.day2.addItem(str(i + 1) + "일")



        la3 = QLabel('희망 인원', self.w)
        la3.setFont(QFont(self.basicInfo.font1, 12))
        la3.setGeometry(100, 210, 100, 40)

        self.hopePerson = QLineEdit(self.w)
        self.hopePerson.setFont(QFont(self.basicInfo.font1,13))
        self.hopePerson.setGeometry(250,210,800,40)
        self.hopePerson.setPlaceholderText('명')

        la4 = QLabel('지원 요건', self.w)
        la4.setFont(QFont(self.basicInfo.font1, 12))
        la4.setGeometry(100, 270, 100, 40)

        self.right = QLineEdit(self.w)
        self.right.setFont(QFont(self.basicInfo.font1, 13))
        self.right.setGeometry(250, 270, 800, 40)
        self.right.setPlaceholderText('ex) python 가능자')

        la5 = QLabel('우대 사항', self.w)
        la5.setFont(QFont(self.basicInfo.font1, 12))
        la5.setGeometry(100, 330, 100, 40)

        self.royalty = QLineEdit(self.w)
        self.royalty.setFont(QFont(self.basicInfo.font1, 13))
        self.royalty.setGeometry(250, 330, 800, 40)
        self.royalty.setPlaceholderText('ex) cospro 자격증')

        la6 = QLabel('제출 서류', self.w)
        la6.setFont(QFont(self.basicInfo.font1, 12))
        la6.setGeometry(100, 390, 100, 40)

        self.document = QLineEdit(self.w)
        self.document.setFont(QFont(self.basicInfo.font1, 13))
        self.document.setGeometry(250, 390, 800, 40)
        self.document.setPlaceholderText('ex) 이력서, 포트폴리오, 자기소개서')

        la7 = QLabel('근무 형태', self.w)
        la7.setFont(QFont(self.basicInfo.font1, 15))
        la7.setGeometry(100, 510, 100, 50)

        la8 = QLabel('사용 언어', self.w)
        la8.setFont(QFont(self.basicInfo.font1, 12))
        la8.setGeometry(100, 570, 100, 40)

        self.useLang = QLineEdit(self.w)
        self.useLang.setFont(QFont(self.basicInfo.font1, 13))
        self.useLang.setGeometry(250, 570, 800, 40)
        self.useLang.setPlaceholderText('ex) python, node.js ( , 로 구분 )')

        la9 = QLabel('고용 형태', self.w)
        la9.setFont(QFont(self.basicInfo.font1, 12))
        la9.setGeometry(100, 630, 100, 40)

        self.employment = QLineEdit(self.w)
        self.employment.setFont(QFont(self.basicInfo.font1, 13))
        self.employment.setGeometry(250, 630, 800, 40)
        self.employment.setPlaceholderText('ex) 현장실습 후 정규직 채용')

        la10 = QLabel('담당 업무', self.w)
        la10.setFont(QFont(self.basicInfo.font1, 12))
        la10 .setGeometry(100, 690, 100, 40)

        self.work = QLineEdit(self.w)
        self.work.setFont(QFont(self.basicInfo.font1, 13))
        self.work.setGeometry(250, 690, 800, 40)
        self.work.setPlaceholderText('ex) 백엔드 개발')

        la11 = QLabel('업무 시간', self.w)
        la11.setFont(QFont(self.basicInfo.font1, 12))
        la11.setGeometry(100, 750, 100, 40)

        self.workTime = QLineEdit(self.w)
        self.workTime.setFont(QFont(self.basicInfo.font1, 13))
        self.workTime.setGeometry(250, 750, 800, 40)
        self.workTime.setPlaceholderText('ex) 주 40시간 근무')

        la12 = QLabel('급여', self.w)
        la12.setFont(QFont(self.basicInfo.font1, 12))
        la12.setGeometry(100, 810, 100, 40)

        self.money = QLineEdit(self.w)
        self.money.setFont(QFont(self.basicInfo.font1, 13))
        self.money.setGeometry(250, 810, 800, 40)
        self.money.setPlaceholderText('ex) 연봉 2400만원')

        la13 = QLabel('복리후생', self.w)
        la13.setFont(QFont(self.basicInfo.font1, 12))
        la13.setGeometry(100, 870, 100, 40)

        self.benefit = QLineEdit(self.w)
        self.benefit.setFont(QFont(self.basicInfo.font1, 13))
        self.benefit.setGeometry(250, 870, 800, 40)
        self.benefit.setPlaceholderText('ex) 중식, 간식, 석식 제공')

        la14 = QLabel('현장 실습 정보', self.w)
        la14.setFont(QFont(self.basicInfo.font1, 15))
        la14.setGeometry(100, 990, 150, 50)

        la15 = QLabel('현장 실습 기간', self.w)
        la15.setFont(QFont(self.basicInfo.font1, 12))
        la15.setGeometry(100, 1050, 200, 40)

        self.period = QLineEdit(self.w)
        self.period.setFont(QFont(self.basicInfo.font1, 13))
        self.period.setGeometry(250, 1050, 800, 40)
        self.period.setPlaceholderText('ex) 2개월')

        la17 = QLabel('현장 실습 수당', self.w)
        la17.setFont(QFont(self.basicInfo.font1, 12))
        la17.setGeometry(100, 1110, 150, 40)

        self.pmoney = QLineEdit(self.w)
        self.pmoney.setFont(QFont(self.basicInfo.font1, 13))
        self.pmoney.setGeometry(250, 1110, 800, 40)
        self.pmoney.setPlaceholderText('ex) 월 150만원')

        la18 = QLabel('담당자 정보', self.w)
        la18.setFont(QFont(self.basicInfo.font1, 15))
        la18.setGeometry(100, 1230, 150, 50)

        la19 = QLabel('e-mail', self.w)
        la19.setFont(QFont(self.basicInfo.font1, 12))
        la19.setGeometry(100, 1290, 150, 40)

        self.email = QLineEdit(self.w)
        self.email.setFont(QFont(self.basicInfo.font1, 13))
        self.email.setGeometry(250, 1290, 800, 40)
        self.email.setPlaceholderText('ex) mirim@e-mirim.hs.kr')

        la20 = QLabel('전화번호', self.w)
        la20.setFont(QFont(self.basicInfo.font1, 12))
        la20.setGeometry(100, 1350, 150, 40)

        self.ph = QLineEdit(self.w)
        self.ph.setFont(QFont(self.basicInfo.font1, 13))
        self.ph.setGeometry(250, 1350, 800, 40)
        self.ph.setPlaceholderText('ex) 01012341234')

        requestBtn = QPushButton('확인', self.w)
        requestBtn.setFont(QFont(self.basicInfo.font1, 12))
        requestBtn.setGeometry(800, 1410, 120, 40)
        requestBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')
        requestBtn.clicked.connect(self.requestBtn)

        cancleBtn = QPushButton('취소', self.w)
        cancleBtn.setFont(QFont(self.basicInfo.font1, 12))
        cancleBtn.setGeometry(930, 1410, 120, 40)
        cancleBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')
        cancleBtn.clicked.connect(self.cancle)

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.w)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        vLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vLayout)

    def requestBtn(self):
        recruit = self.year1.text() + "년" + self.month1.currentText() + self.day1.currentText() + " ~ " + self.year2.text() + "년" + self.month2.currentText() + self.day2.currentText();
        db.insertRequest(company.Company.Company.ID, recruit,
                                        self.hopePerson.text(), self.right.text(), self.royalty.text(),self.document.text(),
                                        self.useLang.text(),self.employment.text(),self.work.text(),
                                        self.money.text(),self.workTime.text(),self.benefit.text(),self.period.text(),
                                        self.pmoney.text(),self.email.text(),self.ph.text())

        self.c=company.CompanyEmploymentRequest.CompanyEmploymentRequest()
        self.c.show()
        self.close()



        
    def cancle(self):
        self.none=company.NoneEmployementRequest.NoneEmployementRequest()
        self.none.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Post()
    ex.show()
    app.exec_()
'''
def insertPost(company_id, recruit, hopeperson, apply, royalty, document,
               uselang, employment, work, money, worktime, benefit,period,
               pmoney, manager_email, manager_ph):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "insert into employment_request ( company_id, recruit, hopeperson, apply, " \
          "royalty, document, uselang, employment, work, money, worktime, benefit, " \
          "period, pmoney, manager_email, manager_ph) values ( '"+company_id+"', '"+recruit+"', "+hopeperson+", '"+\
          apply+"','"+royalty+"', '"+document+"', '"+uselang+"', '"+employment+"', '"+work+"', '"+money+"', '"+\
          worktime+"', '"+benefit+"', '"+period+"','"+ pmoney+"', '"+manager_email+"', '"+manager_ph+"');"
    curs.execute(sql)
'''