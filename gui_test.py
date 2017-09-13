import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel,   QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QColor, QPixmap, QIcon,QPainter,QPen
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Crawlex'
        self.left = 100
        self.top = 100
        self.width = 770
        self.height = 475
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height)


        #BG IMAGE
        label = QLabel(self)
        pixmap = QPixmap('bg_2.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

        #GLAVNI CRAWLEX NATPIS
        self.main_title = QLabel(self)
        self.main_title.move(305,50)
        self.main_title.setText("Crawlex")
        #font_title = QFont('Serif', 37, QFont.Light)
        font_title = QFont("Times", 37)
        self.main_title.setFont(font_title)
        self.main_title.setStyleSheet("color: white")

        #u sto ide URL
        font_input = QFont('Serif',14,QFont.Light)
        self.url_input = QLineEdit(self)
        self.url_input.move(70,210)
        self.url_input.setFont(font_input)
        self.url_input.setFixedWidth(350)
        self.url_input.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.5); border: none; ")


        info_font = QFont('Serif',14,QFont.Light)
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
        self.paste_btn.setFixedHeight(25)
        self.paste_btn.setStyleSheet("color: rgba(255,255,255,1); background-color: rgba(255,255,255,0.5); border: none;")

        #iteration limit entryBox
        self.maxi_input = QLineEdit(self)
        self.maxi_input.move(70,250)
        self.maxi_input.setFont(font_input)
        self.maxi_input.setFixedWidth(77)
        self.maxi_input.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(255,255,255,0.3); border: none; ")
        self.maxi_input.setText("1000")

        # iteration limit label
        self.maxi_label = QLabel(self)
        self.maxi_label.move(170, 253)
        self.maxi_label.setText("Max. number of iterations")
        self.maxi_label.setFont(info_font)
        self.maxi_label.setStyleSheet("color: rgba(255,255,255,0.77)")

        #iteration default button
        self.itd_btn = QPushButton("Default",self)
        self.itd_btn.move(430,250)
        self.itd_btn.setFont(info_font)
        self.itd_btn.setFixedWidth(100)
        self.itd_btn.setFixedHeight(25)
        self.itd_btn.setStyleSheet("color: rgba(255,255,255,0.77); background-color:rgba(255,255,255,0.3); border: none; ")

        #time limit entryBox
        self.maxt_input = QLineEdit(self)
        self.maxt_input.move(70,284)
        self.maxt_input.setFont(font_input)
        self.maxt_input.setFixedWidth(77)
        self.maxt_input.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(255,255,255,0.3); border: none; ")
        self.maxt_input.setText("1000")

        # time limit label
        self.maxt_label = QLabel(self)
        self.maxt_label.move(170, 287)
        self.maxt_label.setText("Time limit (miliseconds)")
        self.maxt_label.setFont(info_font)
        self.maxt_label.setStyleSheet("color: rgba(255,255,255,0.77)")
       # self.maxt_label.setStyleSheet("color: rgba(255,255,255,0.7)")

        #time default button
        self.td_btn = QPushButton("Default",self)
        self.td_btn.move(430,284)
        self.td_btn.setFont(info_font)
        self.td_btn.setFixedWidth(100)
        self.td_btn.setFixedHeight(25)
        self.td_btn.setStyleSheet("color: rgba(255,255,255,0.77); background-color: rgba(255,255,255,0.3); border: none; ")

        middle_font = QFont('Serif',17,QFont.Light)

        #go button
        self.go_btn = QPushButton("Analyze",self)
        self.go_btn.move(587,250)
        self.go_btn.setFont(middle_font)
        self.go_btn.setFixedWidth(140)
        self.go_btn.setFixedHeight(59)
        self.go_btn.setStyleSheet("color: rgba(50,50,50); background-color: rgba(255,255,255,0.7); border: none; ")

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
        self.status_label.move(587, 210)
        self.status_label.setText("Waiting for input")
        self.status_label.setFont(info_font)
        self.status_label.setStyleSheet("color: rgba(255,255,255,0.5)")

        self.show()

    def paintEvet(self,event):
        #crte
        crte = QPainter()
        crte.begin(self)
        stil_crte = QPen(Qt.white,5,Qt.SolidLine)
        crte.setPen(stil_crte)
        crte.drawLine(1,1,500,140)
        crte.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())