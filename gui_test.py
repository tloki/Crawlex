import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel,   QLineEdit, QPushButton, QMessageBox, QPlainTextEdit
from PyQt5.QtGui import QFont, QColor, QPixmap, QIcon, QFontDatabase, QTextCursor
from PyQt5.QtCore import *
from Crawl import *
import re, multiprocessing, threading,time
import os



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = ' '
        self.left = 100
        self.top = 100
        self.width = 770
        self.height = 475

        self.alternate = [(770,475,"v"),(770,730,"^")]
        self.alternate_bool = False

        self.url_ok = False
        self.text_changed = False
        self.iteration_ok = True
        self.time_ok = True
        self.depth_ok = True

        self.printQ = multiprocessing.Queue()
        self.my_thread = threading.Thread(target=self.input_handler, args=(self.printQ,))


        #self.mythreadpool = QThreadPool()

        self.all_ok = False

        #self.parsed_url = ""

        self.MAXT = "1000"
        self.MAXI = "1000"
        self.MAXD = "10"

        self.analyze = Crawl("www.python.org",self.MAXT,self.MAXI,self.MAXD,self.console_print)
        self.t = multiprocessing.Process(target=self.do_nothing)
        self.t.run()



        self.initUI()

        self.my_thread.start()


    def do_nothing(self):
        return

    def input_handler(self,Q_arg:multiprocessing.Queue):
        while True:
            temp_var = Q_arg.get(True)
            time.sleep(0.3)

            dump_list = str(temp_var) + "\n"
            for i in range(Q_arg.qsize()):
                try:
                    dump_list += Q_arg.get(True) + "\n"
                except:
                    break

            self.console_print(dump_list)
            pass



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height)
        self.setWindowIcon(QIcon("ikona.png"))



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

        #depth limit entry box
        self.maxd_input = QLineEdit(self)
        self.maxd_input.move(70, 318)
        self.maxd_input.setFont(font_input)
        self.maxd_input.setFixedWidth(77)
        self.maxd_input.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(255,255,255,0.3); border: none; ")
        self.maxd_input.setText(self.MAXD)
        self.maxd_input.textChanged[str].connect(self.maxdChange)

        #depth limit label
        self.maxd_label = QLabel(self)
        self.maxd_label.move(170, 319)
        self.maxd_label.setText("Depth iteration limit")
        self.maxd_label.setFont(info_font)
        self.maxd_label.setStyleSheet("color: rgba(255,255,255,0.77)")

        #depth default button
        self.dd_btn = QPushButton("Default",self)
        self.dd_btn.move(430,318)
        self.dd_btn.setFont(info_font)
        self.dd_btn.setFixedWidth(100)
        self.dd_btn.setFixedHeight(30)
        self.dd_btn.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(255,255,255,0.3); border: none; ")
        self.dd_btn.clicked.connect(self.dd_btn_click)

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
        self.mail_list_btn.clicked.connect(self.mail_list_click)

        #graph photo button
        self.graph_photo_btn = QPushButton("Graph",self)
        self.graph_photo_btn.move(321,400)
        self.graph_photo_btn.setFont(info_font)
        self.graph_photo_btn.setFixedWidth(140)
        self.graph_photo_btn.setFixedHeight(37)
        self.graph_photo_btn.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.7); border: none; ")
        self.graph_photo_btn.clicked.connect(self.graph_click)

        #more info button
        self.more_info_btn = QPushButton("More info",self)
        self.more_info_btn.move(473,400)
        self.more_info_btn.setFont(info_font)
        self.more_info_btn.setFixedWidth(140)
        self.more_info_btn.setFixedHeight(37)
        self.more_info_btn.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.7); border: none; ")
        self.more_info_btn.clicked.connect(self.more_info_click)

        #waiting label
        self.status_label = QLabel(self)
        self.status_label.move(577, 210)
        self.status_label.setText("Waiting for input")
        self.status_label.setFont(info_font)
        self.status_label.setStyleSheet("color: rgba(255,255,255,0.5)")


        about_font = QFont("Sans-Serif",14)
        #about gumcmb
        self.about_btn = QPushButton("i",self)
        self.about_btn.move(750,455)
        self.about_btn.setFixedSize(20,20)
        self.about_btn.setFont(about_font)
        self.about_btn.setStyleSheet("background-color:rgba(255,255,255,0.5); border:none; color: rgba(50,50,50,0.7)")
        self.about_btn.clicked.connect(self.about_btn_click)

        #expand gumb
        self.expand_btn = QPushButton("v", self)
        self.expand_btn.move(0, 455)
        self.expand_btn.setFixedSize(20, 20)
        self.expand_btn.setFont(about_font)
        self.expand_btn.setStyleSheet("background-color:rgba(255,255,255,0.5); border:none; color: rgba(50,50,50,0.7)")
        self.expand_btn.clicked.connect(self.expand_click)

        #expanded textbox
        self.maxd_label = QLabel(self)
        self.maxd_label.move(170, 319)
        self.maxd_label.setText("Depth iteration limit")
        self.maxd_label.setFont(info_font)
        self.maxd_label.setStyleSheet("color: rgba(255,255,255,0.77)")

        #text box
        console_font = QFont("Courier", 12)
        self.text_box = QPlainTextEdit(self)
        self.text_box.move(0, 475)
        self.text_box.setFont(console_font)
        self.text_box.setFixedWidth(770)
        self.text_box.setFixedHeight(275)
        self.text_box.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(0,0,0,1); border: none; border-top: 3px solid white;")
        self.text_box.insertPlainText("console waiting for output...")
        # self.text_box.setReadOnly(True)



        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.go_btn_click()

    # expand funkcija
    def expand_click(self):

        self.alternate_bool = not self.alternate_bool

        temp_switch = int(self.alternate_bool)

        temp_width = self.alternate[temp_switch][0]
        temp_height = self.alternate[temp_switch][1]

        self.expand_btn.setText(self.alternate[temp_switch][2])

        self.setFixedSize(temp_width, temp_height)
        #self.console_print("dodao tekst")
        return

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

    def dd_btn_click(self):
        self.maxd_input.setText(self.MAXD)
        return

    def about_btn_click(self):
        QMessageBox.about(self, "About Crawlex", "\nWeb crawling application developed for ICM Summer of Code 2017 \n\n\n >Students:\n Abramović Hrvoje\n Krišto Zvonimir\n Tišljar Antun\n Štracak Jakov\n\n >Supervisor:\n Tomislav Lokotar\n\n\nZagreb, 2017.")
        return

    #funkcije pri promijeni teksta
    def urlChange(self):
        self.temp_string = self.url_input.text()

        if not self.temp_string.startswith('http'):
            self.temp_string = 'http://' + self.temp_string

        self.regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if  bool(self.regex.match(self.temp_string)):
                self.url_ok = True

        else:
                self.url_ok = False
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

    def maxdChange(self):
        self.temp_string = self.maxd_input.text()

        try:
            int(self.temp_string)
            self.depth_ok = True
        except ValueError:
            self.depth_ok = False

        self.changeCheck()
        return

    def changeCheck(self):
        if self.url_ok and self.iteration_ok and self.time_ok and self.depth_ok:
            self.status_label.setText("Ready to analyze")
            self.all_ok = True
        else:
            self.status_label.setText("  Invalid input...")
            self.all_ok = False
        return

    def go_btn_click(self):
        if self.all_ok:
            self.status_label.setText("       Working")
            self.analyze = Crawl(self.url_input.text(), int(self.maxi_input.text()), int(self.maxt_input.text()),int(self.maxd_input.text()),queue=self.printQ)
            #self.analyze.start_url = self.url_input.text()
            #self.analyze.max_iter = int(self.maxi_input.text())
            #self.analyze.max_time = int(self.maxt_input.text())
            #self.analyze = Crawl(self.url_input.text(),int(self.maxi_input.text()),int(self.maxt_label.text()))
            #self.mythreadpool.start(self.analyze)
            if self.t.is_alive():
                self.t.terminate()
            self.t = multiprocessing.Process(target=self.analyze.crawl)
            #threads.append(self.t)
            self.t.start()
            #self.analyze.crawl()
            self.status_label.setText("         Done")
            self.text_box.clear()
        else:
            self.status_label.setText("  Invalid input!!!")
        return

    def console_print(self, text_arg):
        self.text_box.setReadOnly(False)
        self.text_box.insertPlainText("\n"+str(text_arg))
        self.text_box.setReadOnly(True)
        # self.text_box.moveCursor(QTextCursor.End)
        return

    def graph_click(self):
        if os.path.isfile("graph.png"):
            os.startfile("graph.png")
        else:
            self.status_label.setText("  Analyze first!")
        return

    def more_info_click(self):
        if os.path.isfile("more_info.txt"):
            os.startfile("more_info.txt")
        else:
            self.status_label.setText("  Analyze first!")
        return


    def mail_list_click(self):
        if os.path.isfile("mail_list.txt"):
            os.startfile("mail_list.txt")
        else:
            self.status_label.setText("  Analyze first!")

        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())