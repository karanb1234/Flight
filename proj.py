from bs4 import BeautifulSoup as Bs
import time 
from selenium import webdriver
import urllib.request
import json
import calendar
import sqlite3
import datetime

import mapping as city

con=sqlite3.Connection('FL.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS FlightData(Date varchar(15),source varchar(4),destintion varchar(4),artime varchar(7),detime varchar(7),duration varchar(8),airline varchar(16),flightno varchar(10),stops varchar(8),fare number,vendor varchar(15))')
class User:
    

    def __init__(self,source,destination,Class,daty,daym,dayd):
        self.so=source
        self.des=destination
        self.cl=Class
        self.daY=daty
        self.daM=daym
        self.daD=dayd
        
    def goIbibo(self):         
         url="http://developer.goibibo.com/api/search/?app_id=91af2f79&app_key=c9db752e62aa6b81135cb2ad74c23fab&format=json&source="
         url1="&destination="
         url3="&dateofdeparture="
         url4="&seatingclass="
         url5="&adults=1&children=0&infants=0&counter=100"
         a=urllib.request.urlopen(url+self.so+url1+self.des+url3+self.daY+self.daM+self.daD+url4+self.cl+url5)
         f=json.loads(a.read())
         for data in f['data']['onwardflights']:

             da=str(str(self.daD)+"/"+str(self.daM)+"/"+str(self.daY))
             s=str(data['origin'])
             d=self.des
             art=str(data['deptime'])
             det=str(data['arrtime'])
             du=str(data['duration'])
             com=str(data['airline'])
             fno=str(data['carrierid']+" - "+data['flightno'])
             nos=str(data['stops']+" Stop")
             fare=int(data['fare']['grossamount'])
             vendor="goIbibo"

             C=(da,s,d,art,det,du,com,fno,nos,fare,vendor)
             '''
             print(data['duration'])
             print(data['airline'])
             
             print(data['deptime'])
             
             print(data['origin'])
             print(data['arrtime'])
             print(data['stops']+" Stop")
             
             print(data['carrierid']+" - "+data['flightno'])
             print(data['fare']['grossamount'])
             '''
             cur.execute("insert into FlightData values(?,?,?,?,?,?,?,?,?,?,?)",C)
             
             
             con.commit()
             del C
             
    def makeMyTrip(self):
        url='http://flights.makemytrip.com/makemytrip/splitRTDataService.json?classType=E&deptDate='
        
        url1='&fltMap=&fromCity='
        url2='&noOfAdlts=1&noOfChd=1&noOfInfnt=1&returnDate='
        
        url3='&toCity='
        url4='&tripType=R&tripTypeDup=R'
        a=urllib.request.urlopen(url+self.daD+'%2F'+self.daM+'%2F'+self.daY+url1+self.so+url2+self.daD+'%2F'+self.daM+'%2F'+self.daY+url3+self.des+url4)
        f=json.loads(a.read())
        f=json.loads(f['fd'])
        #file=open("make.txt","w")
        
        for x in range(len(f['departureFlights'])):
            revised_rate = f['departureFlights'][x]['raf'] if f['departureFlights'][x]['raf'] != 0.0 else f['departureFlights'][x]['af']

            l=len(f['departureFlights'][x]['le'])
            da=str(str(self.daD)+"/"+str(self.daM)+"/"+str(self.daY))
            s=str(f['departureFlights'][x]['le'][0]['o'])
            d=str(f['departureFlights'][x]['le'][l-1]['d'])
            art=str(f['departureFlights'][x]['le'][0]['fdt'])
            det=str(f['departureFlights'][x]['le'][l-1]['fat'])
            du=str(f['departureFlights'][x]['td'])
            com=str(f['departureFlights'][x]['le'][0]['an'])
            fno=str(f['departureFlights'][x]['le'][0]['cc']+" - "+f['departureFlights'][x]['le'][0]['fn'])
            nos=str(str(l-1)+" Stop")
            fare=int(revised_rate)
            vendor="makeMyTrip"

            C=(da,s,d,art,det,du,com,fno,nos,fare,vendor)

            cur.execute("insert into FlightData values(?,?,?,?,?,?,?,?,?,?,?)",C)
            con.commit()
            del C
    def close1(self):
        cur.close()
        con.close()
    def payTm(self):
        
        URL="https://paytm.com/flights/flightSearch/"
        url1=self.so+"-"+city.city_code[self.so]+"/"+self.des+"-"+city.city_code[self.des]
       # https://paytm.com/flights/flightSearch/DEL-Delhi/BOM-Mumbai//1/0/0/E/2018-06-26
        url2="/1/0/0/E/"
        url3=str(str(self.daY)+"-"+str(self.daM)+"-"+str(self.daD))
#https://AGX-Agatti%20Island/DEL-Delhi/1/0/0/E/2018-05-23

        
                 
        abc=webdriver.Chrome()
        abc.get(URL+url1+url2+url3)
        #abc.get("https://paytm.com/flights/flightSearch/DEL-Delhi/BOM-Mumbai/1/0/0/E/2018-05-26")
        time.sleep(10)
        html=abc.page_source

        #f=open("paytm.txt","w")
        #f.write(html)

        abc.quit()


        soup=Bs(html,"lxml")
        container=soup.findAll("div", class_ = "_3215 row")
        #soup.findAll('td', valign='top')
        for div1 in container:
                  
            ac=div1.find_all("div", class_ = "AY8t _1OV0")
            for actual in ac:
                ab=div1.findAll("div", class_ = "_3H-S")
                al=div1.findAll("div", class_ = "NqXj")
                aj=div1.findAll("div",class_ = "vY4t")
       
        
                a=[]
                del a[:]
                b=[]
                del b[:]
                c=[]
                del c[:]
            for (i,j)  in zip(ab,al):
                a.append(str(i.getText()))
                a.append(str(j.getText()))
            
        
            am=div1.findAll("div" , class_ = "_7BOG")
            ak=div1.findAll("div" , class_ = "_2gMo")
            for (i,j) in zip(am,ak):
                b.append(str(i.getText()))
                c.append(str(j.getText()))
            for i in (aj):
                du=(str(i.getText()))
            v=""
            v=str(c[0])
            z=v.strip()
            z=z.replace(",","")
            da=str(str(self.daD)+"/"+str(self.daM)+"/"+str(self.daY))
            s=str(a[3])
            d=str(a[5])
            art=str(a[2])
            det=str(a[4])
            
            com=str(a[0])
            fno=str(a[1])
            nos=str(b[0])
            fare=int(z)
            vendor="Paytm"
            
            C=(da,s,d,art,det,du,com,fno,nos,fare,vendor)

            cur.execute("insert into FlightData values(?,?,?,?,?,?,?,?,?,?,?)",C)
            con.commit()
            del C
            
            '''
            print(a[0])
            print(a[1]) 
            print(a[2])
            print(a[3])
            print(a[4])
            print(a[5])                   
            print(b[0])
            print(c[0])
            print("\n")
            '''
            
       
                            
        #file.close()    
                   #print(data)

'''
now = datetime.datetime.now()

print('='*10+'Welcome to flight searchong system'+'='*10)
cal=calendar.month(now.year, now.month)
print('Here is the calendar:')
print (cal)


origin=input('Enter your origin City')
dest=input('Enter your destination city')
Cl=input('Enter the class you want to travel')
dateY=input('Enter Year  of travel in')
dateM=input('Enter month of travel')
dateD=input('Enter date of travel')


us = User(origin,dest,Cl,dateY,dateM,dateD)



#us.makeMyTrip()
#us.payTm()

'''

        





  


'''cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal
'''



'''import datetime

now = datetime.datetime.now()

print
print "Current date and time using str method of datetime object:"
print str(now)

print
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond
'''

'''
http://flights.makemytrip.com/makemytrip/splitRTDataService.json?classType=E&
deptDate=25%2F06%2F2018&fltMap=&fromCity=DEL&noOfAdlts=1&noOfChd=0&noOfInfnt=0
&returnDate=06%2F11%2F2018&toCity=JAI&tripType=R&tripTypeDup=R
'''

#o9W-795_9W-617    

        
    
        
