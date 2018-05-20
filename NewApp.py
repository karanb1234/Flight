import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Search import *
from  proj import *

class Main2(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.home2()
    def home2(self):
        
        self.setWindowTitle("Flight Search")
        self.ls=QLabel("Source City")
        self.ld=QLabel("Destination City")
        self.dat=QLabel("Date of journey")
        self.clas=QLabel("Class")
        self.c1=QComboBox()
        self.c1.addItems(["E","B"])
        self.s1=QPushButton("Search")
        
        layout = QGridLayout()
        self.l1=QLineEdit()
        self.l2=QLineEdit()
        self.s1.clicked.connect(self.click)
        self.news=QLabel("***ALL FLIGHTS PRICES SHOWN HERE ARE PER PERSON***")
        self.cal=QCalendarWidget()
        self.lbl=QLabel()
        self.cal.clicked.connect(self.showDate)
        date=self.cal.selectedDate()
        self.lbl.setText(date.toString())
        self.l3=QLineEdit()
        self.l3.setPlaceholderText("Enter date")
        layout.addWidget(self.ls,0,0)
        layout.addWidget(self.l1,0,1)
        layout.addWidget(self.ld,0,3)
        layout.addWidget(self.l2,0,4)
        layout.addWidget(self.dat,4,0)
        layout.addWidget(self.cal,7,1)
        layout.addWidget(self.clas,4,3)
        layout.addWidget(self.c1,4,4)
        #layout.addWidget(self.lbl,7,2)
        layout.addWidget(self.l3,4,1)
        layout.addWidget(self.s1,8,4)
        layout.addWidget(self.news,8,1)
        self.setLayout(layout)
        self.showNormal()

    def click(self):
        
        str1=self.l1.text()
        str2=self.l2.text()
        str3=self.l3.text()
        dat=str3.split("/");
        str4=self.c1.currentText()
        print(str4)
        print(dat[0])
        
        if(str1==str2 and str1!="" and str2!=""):
            QMessageBox.about(self, "Error", "Source and destination should be different")
            self.l1.setText("")
            self.l2.setText("")
        elif(str1==""):
            QMessageBox.about(self, "Error", "Source missing")
        elif(str2==""):
            QMessageBox.about(self, "Error", "Destination missing")
        elif(str3==""):
            QMessageBox.about(self, "Date", "Date missing")
        
        else:
            self.obj2=User(str1,str2,str4,dat[2],dat[0],dat[1])
            self.obj2.goIbibo()
            self.obj2.makeMyTrip()
            self.obj2.payTm()
            self.obj2.close1()
            self.obj1=Main3()
            self.obj1.home3(str1,str2,str4,dat[2],dat[0],dat[1])
            self.showMinimized()
            self.close()
        
            
            
        
   



    def showDate(self,date):
        #self.lbl.setText(date.toString())
        self.d1=date.toString()
        self.d1=self.d1[8:]
        self.var1=self.cal.monthShown()
        self.a1=str(self.var1)
        if len(self.a1)==1:
            self.a1="0"+self.a1
        self.x=self.d1.split(" ")
        if len(self.x[0])==1:
            self.x[0]="0"+self.x[0]
        self.var3=self.a1+"/"+self.x[0]+"/"+self.x[1]
        self.l3.setText(self.var3)
        
        
    def ho(self):
        self.a2=QApplication(sys.argv)
        self.a3=Main2()
        sys.exit(self.a2.exec_())

    


        



 

