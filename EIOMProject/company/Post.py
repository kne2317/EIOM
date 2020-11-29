import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
from BasicInfo import BasicInfo


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
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
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

        year1 = QLineEdit(self.w)
        year1.setPlaceholderText('연도')
        year1.setFont(QFont(self.basicInfo.font1, 13))
        year1.setGeometry(250, 150, 100, 40)

        month1 = QComboBox(self.w)
        month1.setFont(QFont(self.basicInfo.font1, 13))
        month1.setGeometry(380, 150, 100, 40)
        for i in range(0, 12):
            month1.addItem(str(i + 1) + "월")

        day1 = QComboBox(self.w)
        day1.setFont(QFont(self.basicInfo.font1, 13))
        day1.setGeometry(510, 150, 100, 40)
        for i in range(0, 30):
            day1.addItem(str(i + 1) + "일")

        year2 = QLineEdit(self.w)
        year2.setPlaceholderText('연도')
        year2.setFont(QFont(self.basicInfo.font1, 13))
        year2.setGeometry(690, 150, 100, 40)

        month2 = QComboBox(self.w)
        month2.setFont(QFont(self.basicInfo.font1, 13))
        month2.setGeometry(820, 150, 100, 40)
        for i in range(0, 12):
            month2.addItem(str(i + 1) + "월")

        day2 = QComboBox(self.w)
        day2.setFont(QFont(self.basicInfo.font1, 13))
        day2.setGeometry(950, 150, 100, 40)
        for i in range(0, 30):
            day2.addItem(str(i + 1) + "일")

        la3 = QLabel('희망 인원', self.w)
        la3.setFont(QFont(self.basicInfo.font1, 12))
        la3.setGeometry(100, 210, 100, 40)

        hopePerson = QLineEdit(self.w)
        hopePerson.setFont(QFont(self.basicInfo.font1,13))
        hopePerson.setGeometry(250,210,800,40)
        hopePerson.setPlaceholderText('명')

        la4 = QLabel('지원 요건', self.w)
        la4.setFont(QFont(self.basicInfo.font1, 12))
        la4.setGeometry(100, 270, 100, 40)

        right = QLineEdit(self.w)
        right.setFont(QFont(self.basicInfo.font1, 13))
        right.setGeometry(250, 270, 800, 40)
        right.setPlaceholderText('ex) python 가능자')

        la5 = QLabel('우대 사항', self.w)
        la5.setFont(QFont(self.basicInfo.font1, 12))
        la5.setGeometry(100, 330, 100, 40)

        royalty = QLineEdit(self.w)
        royalty.setFont(QFont(self.basicInfo.font1, 13))
        royalty.setGeometry(250, 330, 800, 40)
        royalty.setPlaceholderText('ex) cospro 자격증')

        la6 = QLabel('제출 서류', self.w)
        la6.setFont(QFont(self.basicInfo.font1, 12))
        la6.setGeometry(100, 390, 100, 40)

        document = QLineEdit(self.w)
        document.setFont(QFont(self.basicInfo.font1, 13))
        document.setGeometry(250, 390, 800, 40)
        document.setPlaceholderText('ex) 이력서, 포트폴리오, 자기소개서')

        la7 = QLabel('근무 형태', self.w)
        la7.setFont(QFont(self.basicInfo.font1, 15))
        la7.setGeometry(100, 510, 100, 50)

        la8 = QLabel('사용 언어', self.w)
        la8.setFont(QFont(self.basicInfo.font1, 12))
        la8.setGeometry(100, 570, 100, 40)

        useLang = QLineEdit(self.w)
        useLang.setFont(QFont(self.basicInfo.font1, 13))
        useLang.setGeometry(250, 570, 800, 40)
        useLang.setPlaceholderText('ex) python, node.js')

        la9 = QLabel('고용 형태', self.w)
        la9.setFont(QFont(self.basicInfo.font1, 12))
        la9.setGeometry(100, 630, 100, 40)

        employment = QLineEdit(self.w)
        employment.setFont(QFont(self.basicInfo.font1, 13))
        employment.setGeometry(250, 630, 800, 40)
        employment.setPlaceholderText('ex) 현장실습 후 정규직 채용')

        la10 = QLabel('담당 업무', self.w)
        la10.setFont(QFont(self.basicInfo.font1, 12))
        la10 .setGeometry(100, 690, 100, 40)

        work = QLineEdit(self.w)
        work.setFont(QFont(self.basicInfo.font1, 13))
        work.setGeometry(250, 690, 800, 40)
        work.setPlaceholderText('ex) 백엔드 개발')

        la11 = QLabel('업무 시간', self.w)
        la11.setFont(QFont(self.basicInfo.font1, 12))
        la11.setGeometry(100, 750, 100, 40)

        workTime = QLineEdit(self.w)
        workTime.setFont(QFont(self.basicInfo.font1, 13))
        workTime.setGeometry(250, 750, 800, 40)
        workTime.setPlaceholderText('ex) 주 40시간 근무')

        la12 = QLabel('급여', self.w)
        la12.setFont(QFont(self.basicInfo.font1, 12))
        la12.setGeometry(100, 810, 100, 40)

        money = QLineEdit(self.w)
        money.setFont(QFont(self.basicInfo.font1, 13))
        money.setGeometry(250, 810, 800, 40)
        money.setPlaceholderText('ex) 연봉 2400만원')

        la13 = QLabel('복리후생', self.w)
        la13.setFont(QFont(self.basicInfo.font1, 12))
        la13.setGeometry(100, 870, 100, 40)

        benefit = QLineEdit(self.w)
        benefit.setFont(QFont(self.basicInfo.font1, 13))
        benefit.setGeometry(250, 870, 800, 40)
        benefit.setPlaceholderText('ex) 중식, 간식, 석식 제공')

        la14 = QLabel('현장 실습 정보', self.w)
        la14.setFont(QFont(self.basicInfo.font1, 15))
        la14.setGeometry(100, 990, 150, 50)

        la15 = QLabel('현장 실습 기간', self.w)
        la15.setFont(QFont(self.basicInfo.font1, 12))
        la15.setGeometry(100, 1050, 200, 40)

        period = QLineEdit(self.w)
        period.setFont(QFont(self.basicInfo.font1, 13))
        period.setGeometry(250, 810, 800, 40)
        period.setPlaceholderText('ex) 2개월')

        la16 = QLabel('현장 실습 기간', self.w)
        la16.setFont(QFont(self.basicInfo.font1, 12))
        la16.setGeometry(100, 1050, 150, 40)

        period = QLineEdit(self.w)
        period.setFont(QFont(self.basicInfo.font1, 13))
        period.setGeometry(250, 1050, 800, 40)
        period.setPlaceholderText('ex) 2개월')

        la17 = QLabel('현장 실습 수당', self.w)
        la17.setFont(QFont(self.basicInfo.font1, 12))
        la17.setGeometry(100, 1110, 150, 40)

        pmoney = QLineEdit(self.w)
        pmoney.setFont(QFont(self.basicInfo.font1, 13))
        pmoney.setGeometry(250, 1110, 800, 40)
        pmoney.setPlaceholderText('ex) 월 150만원')

        la18 = QLabel('담당자 정보', self.w)
        la18.setFont(QFont(self.basicInfo.font1, 15))
        la18.setGeometry(100, 1230, 150, 50)

        la19 = QLabel('e-mail', self.w)
        la19.setFont(QFont(self.basicInfo.font1, 12))
        la19.setGeometry(100, 1290, 150, 40)

        email = QLineEdit(self.w)
        email.setFont(QFont(self.basicInfo.font1, 13))
        email.setGeometry(250, 1290, 800, 40)
        email.setPlaceholderText('ex) mirim@e-mirim.hs.kr')

        la20 = QLabel('전화번호', self.w)
        la20.setFont(QFont(self.basicInfo.font1, 12))
        la20.setGeometry(100, 1350, 150, 40)

        ph = QLineEdit(self.w)
        ph.setFont(QFont(self.basicInfo.font1, 13))
        ph.setGeometry(250, 1350, 800, 40)
        ph.setPlaceholderText('ex) 01012341234')

        requestBtn = QPushButton('확인', self.w)
        requestBtn.setFont(QFont(self.basicInfo.font1, 12))
        requestBtn.setGeometry(930, 1410, 120, 40)
        requestBtn.setStyleSheet('background-color: white; border:1px solid lightgray;')


        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.w)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Post()
    sys.exit(app.exec_())
