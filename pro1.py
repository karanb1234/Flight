import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from NewApp import *
class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.home()
    def home(self):
        self.b=QPushButton("Continue")
        self.l=QLabel("Optimize your Flight Booking with FLYSCANNER!")
        self.lab=QLabel()
        self.pix=QPixmap('image.jpg')
        self.lab.setPixmap(self.pix)
        self.resize(800,400)
        self.b.move(10,5)
                


        
        hbox=QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.l)
        hbox.addStretch()
        vbox=QVBoxLayout()
        vbox.addWidget(self.b)
        vbox.addWidget(self.lab)
        
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.setWindowTitle("Flights")
        self.b.clicked.connect(self.on_click)
        #self.b1.clicked.connect(self.on_click2)
        self.setGeometry(100,100,626,300)
        self.showMaximized()
      
    def on_click(self):
        self.obj=Main2()
        self.showMinimized()
        self.close()
app=QApplication(sys.argv)
a1=App()#Instance of class
sys.exit(app.exec_())
    
     
 
