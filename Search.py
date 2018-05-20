import mapping as city
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
import webbrowser
class Main3(QWidget):
    def __init__(self):

        QWidget.__init__(self)
        
        #self.home3()
    def home3(self,str1,str2,str3,dy,dm,dd):
        self.s1=str1
        self.s2=str2
        self.s3=str3
        self.dDy=dy
        self.dDm=dm
        self.dDd=dd
        '''
        cur.execute('CREATE TABLE IF NOT EXISTS FlightData(Date varchar(15),source varchar(4),destintion varchar(4),artime varchar(7),detime varchar(7),duration varchar(8),airline varchar(16),flightno varchar(10),stops varchar(8),fare number,vendor varchar(15))')
        con=sqlite3.Connection('FL.db')
        cur=con.cursor()
        cur.execute('select * from FlightData order by fare , flightno asc')
        a=cur.fetchall()
        '''
        
        
        self.setWindowTitle("Search Results")
        self.l=QLabel()
        self.l.setText("Search results for the requested flight is")
        '''
        self.scroll=QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        '''
        self.table=QTableWidget()
        layout=QVBoxLayout()
        self.button=QPushButton("Load Data")
        self.button1=QPushButton("Book via paytm")
        self.button2=QPushButton("Book via GoIbibo")
        self.button3=QPushButton("Book via makeMytrip")
        self.button.setGeometry(QRect(150,50,50,50))
        self.button.clicked.connect(self.loaddata)
        self.button1.clicked.connect(self.book1)
        self.button2.clicked.connect(self.book2)
        self.button3.clicked.connect(self.book3)
        self.table.setRowCount(200)
        self.table.setColumnCount(11)
        #self.table.setShowGrid(show_grid)
        layout.addWidget(self.l)
        layout.addWidget(self.table)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        
       
        
        
        
        
        
        
        self.setLayout(layout)
        self.resize(800,400)
        self.show()
    def loaddata(self):
        con=sqlite3.Connection("FL.db")
        cur=con.cursor()
        query="select * from Flightdata ORDER BY fare,flightno ASC"
        res=cur.execute(query)
        self.table.setRowCount(0)
        for row_no, row_data in enumerate(res):
            self.table.insertRow(row_no)
            for col_no, data in enumerate(row_data):
                self.table.setItem(row_no, col_no, QTableWidgetItem(str(data)))
        cur.execute("DELETE from FlightData")
        con.commit()
        cur.close()
        con.close()
                
        
    def book1(self):
        '''
        url='http://docs.python.org/lib/module-webbrowser.html'
        url="https://paytm.com/flights/flightSearch/"
        url1=self.str1
        url2=self.str2
        payt=url+url1+"-"+
        '''



        URL="https://paytm.com/flights/flightSearch/"
        url1=self.s1+"-"+city.city_code[self.s1]+"/"+self.s2+"-"+city.city_code[self.s2]
        # https://paytm.com/flights/flightSearch/DEL-Delhi/BOM-Mumbai//1/0/0/E/2018-06-26
        url2="/1/0/0/E/"
        url3=str(str(self.dDy)+"-"+str(self.dDm)+"-"+str(self.dDd))
        #DEL-Delhi/BOM-Mumbai/1/0/0/E/2018-05-29
        #self,str1,str2,str3,dy,dm,dd
        webbrowser.open(URL+url1+url2+url3)
    def book2(self):
        url="https://www.goibibo.com/flights/air-"
        url1=self.s1
        url2=self.s2
        url3=str(self.dDy+self.dDm+self.dDd)
        URL=str(url+url1+"-"+url2+"-"+url3+"--1-0-0-E-D/")
        #https://www.goibibo.com/flights/air-DEL-BOM-20180529--1-0-0-E-D/
        webbrowser.open(URL)
    def book3(self):
        url="https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/"
        url1=self.s1
        url2=self.s2
        URL=str(url+url1+"_"+url2+"_"+self.dDd+"-"+self.dDm+"-"+self.dDy)
        #https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_29-05-2018
        #https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_29-05-2018
        webbrowser.open(URL)

    def ho(self):
        self.a2=QApplication(sys.argv)
        self.a3=Main3()
        sys.exit(self.a2.exec_())

            

 


        
