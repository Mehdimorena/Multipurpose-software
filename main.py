import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
import pyperclip as pc
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets ,QtCore , QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit ,QPushButton ,QSpinBox , QRadioButton , QLabel




class Opp_Project(QtWidgets.QMainWindow):
    def __init__(self):
        super(Opp_Project, self).__init__()

        # Set The UI
        self.initUI()
        # Set The GUI Position And Size
        self.setGeometry(1100, 500, 300, 250)
        # Set The GUI Title
        self.setWindowTitle("Opp Project")

    def initUI(self):
        Central = QtWidgets.QWidget(self)
        self.setCentralWidget(Central)

        # The main button
        self.deckButton = QtWidgets.QPushButton(self)
        self.deckButton.setText("Pasword Generator")
        self.deckButton.clicked.connect(self.open_passwordgenerator)
        self.deckButton.setGeometry(50, 50, 200, 30)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.deckButton, 0)

        Central.setLayout(hbox)

        #Second button
        self.deckButton2 = QtWidgets.QPushButton(self)
        self.deckButton2.setText("Toe")
        self.deckButton2.clicked.connect(self.open_Toe)
        self.deckButton2.setGeometry(10, 50,280, 30)

        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addWidget(self.deckButton2, 0)

        Central.setLayout(hbox2)




    def open_passwordgenerator(self):
        self.w = UI()
        self.w.show()

    def open_Toe(self):
        self.w = Toe()
        self.w.show()



class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load the ui file
        uic.loadUi("passwordgenerate.ui", self)

        # Definition of buttons
        self.spin = self.findChild(QSpinBox, "spinBox")
        self.spin.setRange(8,64)
        self.line = self.findChild(QLineEdit,"lineEdit")
        self.generate = self.findChild(QPushButton,"pushButton_generate")
        self.radioButton_normal = self.findChild(QRadioButton,"radioButton_normal")
        self.radioButton_medium = self.findChild(QRadioButton,"radioButton_medium")
        self.radioButton_hard = self.findChild(QRadioButton,"radioButton_hard")
        self.copy = self.findChild(QPushButton,"pushButton_copy")
        self.l_copy = self.findChild(QLabel,"label_copy")

        # connect to generator func
        self.generate.clicked.connect(self.generator)
        #connect to copy func
        self.copy.clicked.connect(self.copying)
        #lace holder
        self.line.setText("Your New Password")

        # set checkbox to medium  from defulte
        self.radioButton_medium.setChecked(True)

        # show the app
        self.show()


    def copying(self):
        a1 = self.line.text()
        pc.copy(a1)
        a2 = pc.paste()
        self.l_copy.setText("Password Copied")



    def generator(self):
        numbers = "0123456789"
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        symbol = "!@#$%^&*()>_+"
        Ambiguous = "[]{}|\/<>~"',:'

        if self.radioButton_normal.isChecked():
            string = numbers + lower + symbol + lower
            len = self.spin.value()
            password = "".join(random.sample(string,len))

            self.line.setText(str(password))

        if self.radioButton_medium.isChecked():
            string = numbers + lower + symbol + upper
            len = self.spin.value()
            password = "".join(random.sample(string,len))

            self.line.setText(str(password))

        if self.radioButton_hard.isChecked():
            string = numbers + lower + symbol + upper + Ambiguous
            len = self.spin.value()
            password = "".join(random.sample(string,len))

            self.line.setText(str(password))

        self.l_copy.setText("")



class Toe(QMainWindow):
    def __init__(self):
        super(Toe , self).__init__()

        #load the ui file
        uic.loadUi("Toe.ui",self)

        #Define A Counter to keep Track Of Who,s Turn it is
        self.counter = 0

        #define Our Widgets
        self.button1 = self.findChild(QPushButton , "pushButton_1")
        self.button2 = self.findChild(QPushButton , "pushButton_2")
        self.button3 = self.findChild(QPushButton , "pushButton_3")
        self.button4 = self.findChild(QPushButton , "pushButton_4")
        self.button5 = self.findChild(QPushButton , "pushButton_5")
        self.button6 = self.findChild(QPushButton , "pushButton_6")
        self.button7 = self.findChild(QPushButton , "pushButton_7")
        self.button8 = self.findChild(QPushButton , "pushButton_8")
        self.button9 = self.findChild(QPushButton , "pushButton_9")
        self.button10 = self.findChild(QPushButton , "pushButton_10")
        self.label = self.findChild(QLabel , "label")

        # Click the  Dropdown Box
        self.button1.clicked.connect(lambda : self.clicker(self.button1))
        self.button2.clicked.connect(lambda : self.clicker(self.button2))
        self.button3.clicked.connect(lambda : self.clicker(self.button3))
        self.button4.clicked.connect(lambda : self.clicker(self.button4))
        self.button5.clicked.connect(lambda : self.clicker(self.button5))
        self.button6.clicked.connect(lambda : self.clicker(self.button6))
        self.button7.clicked.connect(lambda : self.clicker(self.button7))
        self.button8.clicked.connect(lambda : self.clicker(self.button8))
        self.button9.clicked.connect(lambda : self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)

        #Show The App
        self.show()


    
    def checkwin(self):
        # across check row
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.win(self.button1,self.button2,self.button3)
        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.win(self.button4,self.button5,self.button6)
        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.win(self.button7,self.button8,self.button9)
        # Down
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.win(self.button1,self.button4,self.button7)
        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.win(self.button2,self.button5,self.button8)
        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9 .text():
            self.win(self.button3,self.button6,self.button9)
        # Diagonal مورب
        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.win(self.button1,self.button5,self.button9)
        if self.button7.text() != "" and self.button7.text() == self.button5.text() and self.button7.text() == self.button3.text():
            self.win(self.button7,self.button5,self.button3)









    def win(self,a,b,c):
        a.setStyleSheet('QPushButton {color:red;}') # Color change
        b.setStyleSheet('QPushButton {color:red;}')
        c.setStyleSheet('QPushButton {color:red;}')

        self.label.setText(f"{a.text()} Wins!") #Send the winning message


        # Disable the Board
        self.disable()

    # Disable the Board
    def disable(self):
        button_list =[
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9
        ]


    #clicker the buttons
    def clicker(self,b):
        if self.counter % 2 == 0:
            mark = "x"
            self.label.setText("O's Turn")
        else:
            mark = "O"
            self.label.setText("X's Turn")

        b.setText(mark)
        b.setEnabled(False) ## The button works only once

        #Increment The Counter
        self.counter += 1
        #check if won
        self.checkwin()

    #Start Over
    def reset(self):
        #creat a list of all our buttons
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9 ]
        # Rerset the buttons
        for b in button_list:
            b.setText("")
            b.setEnabled(True)
            #reset the button colors
            a.setStyleSheet('QPushButton {color:bule;}')

        # reset the Label
        self.label.setText("X Goes Firs! ")

        #reset the counter
        self.counter = 0











def window():
    app = QtWidgets.QApplication(sys.argv)
    win = Opp_Project()
    win.show()
    sys.exit(app.exec_())


window()