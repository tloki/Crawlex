import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel,   QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QColor, QPixmap, QIcon, QFontDatabase
from PyQt5.QtCore import *
from Crawl import *
from Page import *



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = ' '
        self.left = 100
        self.top = 100
        self.width = 770
        self.height = 475

        self.url_ok = False
        self.text_changed = False
        self.iteration_ok = True
        self.time_ok = True

        self.all_ok = False

        self.MAXT = "1000"
        self.MAXI = "1000"

        self.analyze = Crawl("www.python.org",self.MAXT,self.MAXI)

        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height)
        self.setWindowIcon(QIcon("ikona.png"))

        self.temp_page = Page(0,"-")

        font_db = QFontDatabase()
        Montserrat = font_db.addApplicationFont("Montserrat-Regular.otf")

        #BG IMAGE
        label = QLabel(self)
        pixmap = QPixmap('bg_2.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

        #GLAVNI CRAWLEX NATPIS
        self.main_title = QLabel(self)
        self.main_title.move(300,17)
        self.main_title.setText("Crawlex")
        #font_title = QFont('Serif', 37, QFont.Light)
        font_title = QFont("Montserrat", 37)
        self.main_title.setFont(font_title)
        self.main_title.setStyleSheet("color: white")

        #u sto ide URL
        font_input = QFont("Montserrat",14,QFont.Light)
        self.url_input = QLineEdit(self)
        self.url_input.move(70,210)
        self.url_input.setFont(font_input)
        self.url_input.setFixedWidth(350)
        self.url_input.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.5); border: none; ")

        self.url_input.textChanged[str].connect(self.urlChange)


        info_font = QFont("Montserrat",14,QFont.Light)
        #url label
        self.url_label = QLabel(self)
        self.url_label.move(70, 177)
        self.url_label.setText("URL")
        self.url_label.setFont(info_font)
        self.url_label.setStyleSheet("color: white")

        #url paste button
        self.paste_btn = QPushButton("Paste",self)
        self.paste_btn.move(430,210)
        self.paste_btn.setFont(info_font)
        self.paste_btn.setFixedWidth(100)
        self.paste_btn.setFixedHeight(31)
        self.paste_btn.setStyleSheet("color: rgba(255,255,255,1); background-color: rgba(255,255,255,0.5); border: none;")
        self.paste_btn.clicked.connect(self.paste_btn_click)

        #iteration limit entryBox
        self.maxi_input = QLineEdit(self)
        self.maxi_input.move(70,250)
        self.maxi_input.setFont(font_input)
        self.maxi_input.setFixedWidth(77)
        self.maxi_input.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(255,255,255,0.3); border: none; ")
        self.maxi_input.setText(self.MAXI)
        self.maxi_input.textChanged[str].connect(self.maxiChange)

        # iteration limit label
        self.maxi_label = QLabel(self)
        self.maxi_label.move(170, 250)
        self.maxi_label.setText("Max. number of iterations")
        self.maxi_label.setFont(info_font)
        self.maxi_label.setStyleSheet("color: rgba(255,255,255,0.77)")

        #iteration default button
        self.itd_btn = QPushButton("Default",self)
        self.itd_btn.move(430,250)
        self.itd_btn.setFont(info_font)
        self.itd_btn.setFixedWidth(100)
        self.itd_btn.setFixedHeight(30)
        self.itd_btn.setStyleSheet("color: rgba(255,255,255,0.77); background-color:rgba(255,255,255,0.3); border: none; ")
        self.itd_btn.clicked.connect(self.itd_btn_click)

        #time limit entryBox
        self.maxt_input = QLineEdit(self)
        self.maxt_input.move(70,284)
        self.maxt_input.setFont(font_input)
        self.maxt_input.setFixedWidth(77)
        self.maxt_input.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(255,255,255,0.3); border: none; ")
        self.maxt_input.setText(self.MAXT)
        self.maxt_input.textChanged[str].connect(self.maxtChange)

        # time limit label
        self.maxt_label = QLabel(self)
        self.maxt_label.move(170, 285)
        self.maxt_label.setText("Time limit (miliseconds)")
        self.maxt_label.setFont(info_font)
        self.maxt_label.setStyleSheet("color: rgba(255,255,255,0.77)")
       # self.maxt_label.setStyleSheet("color: rgba(255,255,255,0.7)")

        #time default button
        self.td_btn = QPushButton("Default",self)
        self.td_btn.move(430,284)
        self.td_btn.setFont(info_font)
        self.td_btn.setFixedWidth(100)
        self.td_btn.setFixedHeight(30)
        self.td_btn.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(255,255,255,0.3); border: none; ")
        self.td_btn.clicked.connect(self.td_btn_click)

        middle_font = QFont("Montserrat",17)

        #go button
        self.go_btn = QPushButton("Analyze",self)
        self.go_btn.move(587,255)
        self.go_btn.setFont(middle_font)
        self.go_btn.setFixedWidth(140)
        self.go_btn.setFixedHeight(59)
        self.go_btn.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.7); border: none; ")
        self.go_btn.clicked.connect(self.go_btn_click)

        #mail list button
        self.mail_list_btn = QPushButton("Mail list",self)
        self.mail_list_btn.move(170,400)
        self.mail_list_btn.setFont(info_font)
        self.mail_list_btn.setFixedWidth(140)
        self.mail_list_btn.setFixedHeight(37)
        self.mail_list_btn.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.7); border: none; ")

        #graph photo button
        self.graph_photo_btn = QPushButton("Graph",self)
        self.graph_photo_btn.move(321,400)
        self.graph_photo_btn.setFont(info_font)
        self.graph_photo_btn.setFixedWidth(140)
        self.graph_photo_btn.setFixedHeight(37)
        self.graph_photo_btn.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.7); border: none; ")

        #more info button
        self.more_info_btn = QPushButton("More info",self)
        self.more_info_btn.move(473,400)
        self.more_info_btn.setFont(info_font)
        self.more_info_btn.setFixedWidth(140)
        self.more_info_btn.setFixedHeight(37)
        self.more_info_btn.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.7); border: none; ")

        #waiting label
        self.status_label = QLabel(self)
        self.status_label.move(577, 210)
        self.status_label.setText("Waiting for input")
        self.status_label.setFont(info_font)
        self.status_label.setStyleSheet("color: rgba(255,255,255,0.5)")

        self.show()

    #funkcija za paste gumb
    def paste_btn_click(self):
        self.clipboard = QApplication.clipboard()
        if self.clipboard.text() != "":
            self.url_input.setText(self.clipboard.text())
        return

    #funkcije za default gumbe
    def td_btn_click(self):
        self.maxt_input.setText(self.MAXT)
        return

    def itd_btn_click(self):
        self.maxi_input.setText(self.MAXI)
        return

    #funkcije pri promijeni teksta
    def urlChange(self):
        self.temp_string = self.url_input.text()
        ##self.temp_Page.url = self.temp_string
        if  True: #self.temp_Page.check_url():
                self.url_ok = True;
        else:
                self.url_ok = False;
        self.changeCheck()
        return

    def maxiChange(self):
        self.temp_string = self.maxi_input.text()

        try:
            int(self.temp_string)
            self.iteration_ok = True
        except ValueError:
            self.iteration_ok = False

        self.changeCheck()
        return

    def maxtChange(self):
        self.temp_string = self.maxt_input.text()

        try:
            int(self.temp_string)
            self.time_ok = True
        except ValueError:
            self.time_ok = False

        self.changeCheck()
        return


    def changeCheck(self):
        if self.url_ok and self.iteration_ok and self.time_ok:
            self.status_label.setText("Ready to analyze")
            self.all_ok = True
        else:
            self.status_label.setText("  Invalid input...")
            self.all_ok = False
        return

    def go_btn_click(self):
        if self.all_ok:
            self.status_label.setText("       Working")
            self.analyze.start_url = self.url_input.text()
            self.analyze.max_iter = int(self.maxi_input.text())
            self.analyze.max_time = int(self.maxt_input.text())
            #self.analyze = Crawl(self.url_input.text(),int(self.maxi_input.text()),int(self.maxt_label.text()))
            self.analyze.crawl()
            self.status_label.setText("         Done")
        else:
            self.status_label.setText("  Invalid input!!!")
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())