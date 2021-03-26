# Converrt elevator floors
# inp = input('Which Europe Floor ')
# try:
#     n=int(inp)
# except:
#     n= -1
# if n > 0 :
#     usf = n+1
#     print('US Floor' , usf)
# else :
#      print('Enter Number')
#FUNCTION##
# def thing():
#     print('JUST CHECKING')
# thing()
# print('Is it Done?')
# thing()
# print('yeah it is')
# big = max('Hello world')
# print(big)
###HOURS&RATE######################################################
# hour = input('Enter Hours')
# rate = input('Enter Rate')
# h = float(hour)
# r = float(rate)
# def computepay(h,r):
# 	if h>40  :
# 		part1 = ((h-40)*1.5)*10.5
# 		part2 = 40*10.5
# 		pay = part1+part2
# 		return pay
# 	else :
# 		pay = h*r
# 		return pay
# p = computepay(h,r)
# # print('Pay',p)
######################################
# fruit = 'banana'
# index = 0
# while index < len(fruit) : 
#     letter = fruit[index]
#     print(index , letter)
    # index = index + 1
#####FILES####################################
# fname = input('enter File name :  ')
# fh = open(fname)
# inp = fh.read()
# print(inp.upper())
#####FILES 2#######################################
# fname = input("Enter file name:  ")
# fo = open(fname)
# total = 0
# total=float(total)
# count = 0
# for line in fo :
#     if not line.startswith('X-DSPAM-Confidence:') :
#         continue
#     count=count+1
#     val = line.find('0')
#     value = line[val:]
#     number = float(value)
#     total=total+number
# avg=total/count
# print('Average spam confidence:',avg)
# friends = [Dave , Marques , Lew]
# for friend in friends :
#     print('Hey', friend)

###################EXERCISE 8.4###############################################

# fname = input('Enter File Name : ')
# fh = open(fname)
# lst = list()
# flst1 = list()
# for line in fh :
#     line = line.rstrip()
#     line = line.split()       
#     if not line in lst :
#         lst=line+lst
#         for word in lst :
#             if word not in flst1 :
#                 flst1.append(word)
# flst = list()
# flst = flst1.sort()                
# print(flst1)

####################EXERCISE 8.5###################

# fname = input('Enter File name: ')
# fo = open(fname)
# # count = 0
# counts = dict()

# for line in fo :
#     if not line.startswith('From ') :
#         continue
#     # count=count+1
#     words = line.split()
#     words=words[1]
#     words.append(words)
#     print(words)
#     for word in words :
#         counts[word] = counts.get(word,0) + 1
    
# bigcount = None
# bigword = None
# for word,count in counts.items() :
#     if bigcount is None or count > bigcount :
#         bigword = word
#         bigcount = count

# print(bigword , bigcount)

###############EXERCISE 9.4###############

# fname = input('Enter File name: ')
# fo = open(fname)
# # # count = 0
# counts = dict()
# lst = list()

# for line in fo :
#     if not line.startswith('From ') :
#          continue
#     words = line.split()
#     words = words[1]
#     lst.append(words)
# # print(lst)

# for word in lst :
#     # print(word)
#     counts[word] = counts.get(word,0) +1
# print(counts)

# bigcount = None
# bigword = None
# for word,count in counts.items() :
#     if bigcount is None or count > bigcount :
#         bigword = word
#         bigcount = count

# print(bigword , bigcount)

###############EXERCISE 10.2###############

# fname = input('Enter File name: ')
# fo = open(fname)
# counts = dict()
# lst = list()
# lst2 = list()

# for line in fo :
#     if not line.startswith('From ') :
#          continue
#     words = line.split()
#     words = words[5]
#     words = words[0:2]
#     lst.append(words)
# for hrs in lst :
#     counts[hrs] = counts.get(hrs , 0) + 1 
# # print(counts)

# for hrs , times in counts.items() :
#     newtup = (hrs,times)
#     lst2.append(newtup)
# lst2 = sorted(lst2)

# for hrs,times in lst2 :
#     print(hrs,times)

###########################Assignment Course 3 WEEK2###########################################
# import re

# if __name__ == '__main__':
#     file = open('Assignmentfile.txt')
#     sm = 0
#     wd = 0
#     for line in file:
#         temp = line.rstrip()
#         temp = re.findall('[0-9]+', temp)
#         #print(temp)
#         #print('\n')
#         if len(temp) > 0:
#             for w in temp:
#                 wd += 1
#                 sm += int(w)

#     print('The sum for the sample text above is %d\n' % sm)
###########################Assignment Course 3 WEEK4###########################################
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# #Get SSL Certification Error handeling
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# #Data Collect From the Website
# link = input('Enter - ')
# html = urllib.request.urlopen(link, context = ctx).read()
# soup = BeautifulSoup(html, 'html.parser')


# #Data Scraping
# tags = soup('span')
# sm = 0
# cn = 0
# for tag in tags:
#     cn += 1
#     sm += int(tag.contents[0])

# print('Count %d' % cn)
# print('Sum %d' % sm)
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# #SSL Certification Error Handle
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# #Data Collection
# link = input('Enter URL: ')
# cont = int(input('Enter count: '))
# line = int(input('Enter position: '))



# print('Retrieving: %s' % link)
# for i in range(0, cont):
#     html = urllib.request.urlopen(link, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
    
#     tags = soup('a')
#     cn = 0
#     ps = 0
#     for tag in tags:
#         ps += 1
#         if ps == line:
#             print('Retrieving: %s' % str(tag.get('href', None)))
#             link = str(tag.get('href', None))
#             ps = 0
#             break
###########################Assignment Course 3 WEEK5###########################################
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET

# link = input('Enter location: ')
# html = urllib.request.urlopen(link).read().decode()
# print('Retrieving', link)
# print('Retrieved', len(html), 'characters')


# #data calculation
# cn = 0
# sm = 0
# data = ET.fromstring(html)
# tags = data.findall('comments/comment')

# for tag in tags:
#     cn += 1
#     sm += int(tag.find('count').text)

# print('Count:', cn)
# print('Sum:', sm)
###########################Assignment Course 3 WEEK6###########################################
# import urllib.request, urllib.parse, urllib.error
# import json

# link = input('Enter location: ')
# print('Retrieving', link)

# html = urllib.request.urlopen(link).read().decode()
# print('Retrieved', len(html), 'characters')

# try:
#     js = json.loads(html)
# except:
#     js = None

# cn = 0
# sm = 0
# for item in js['comments']:
#     cn += 1
#     sm += int(item['count'])

# print('Count:', cn)
# print('Sum:', sm)
###########################Assignment2 Course 3 WEEK6###########################################
  
# import urllib.request, urllib.parse, urllib.error
# import json


# target = 'http://py4e-data.dr-chuck.net/json?'
# local = input('enter location:')
# url = target + urllib.parse.urlencode({'address': local, 'key' : 42})

# print('Retrieving', url)
# data = urllib.request.urlopen(url).read()
# print('Retrieved', len(data), 'characters')
# js = json.loads(data)
# print(json.dumps(js, indent=4))
# print('place id',js['results'][0]['place_id'])
###########################Assignment2 Course 4 WEEK2###########################################

# import sqlite3
# import re

# class MyDB:
#     def __init__(self):
#         self.db_name = 'emaildb.sqlite'
#         self.con = ''
#         self.cur = ''
#         self.fl = ''

#     def db_connect(self):
#         self.con = sqlite3.connect(self.db_name)
#         self.cur = self.con.cursor()
    
#     def create_db(self):
#         try:
#             self.cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')
#             self.con.commit()
#         except:
#             None
#             #self.cur.execute('Drop Before Database')

#     def add_db(self, a):
#         self.cur.execute('INSERT INTO Counts(org, count) VALUES(?, 1)', (a,))

#     def update_db(self, a):
#         self.cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (a,))
    
#     def show_db(self):
#         self.sql = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
#         for self.row in self.cur.execute(self.sql):
#             print(str(self.row[0]), self.row[1])

#         self.cur.close()

#     def open_file(self):
#         self.fname = input('Enter file name: ')
#         if len(self.fname) < 1:
#             self.fname = 'mbox.txt'
        
#         self.fl = open(self.fname)
        
#         for self.line in self.fl:
#             if not self.line.startswith('From: '):
#                 continue
#             self.line = self.line.strip()
#             self.temp = re.findall('@([\w.]+)', self.line)
            
#             if len(self.temp) > 0:
#                 self.domain = self.temp[0]
#                 self.cur.execute('SELECT count FROM Counts WHERE org = ? ', (self.domain,))
#                 self.row = self.cur.fetchone()

#                 if self.row is None:
#                     self.add_db(self.domain)
#                 else:
#                     self.update_db(self.domain)

#                 self.con.commit()

# if __name__ == '__main__':
#     obj = MyDB()
#     obj.db_connect()
#     obj.create_db()
#     obj.open_file()
#     obj.show_db()
###########################Assignment1 Course 4 WEEK3###########################################
##new one
# b=-20
# def slope(b):
#     return 2* (b-4)
# while(b<=4.00):
#     b= b-0.1*slope(b)
#     b=round(b,2)
# print(b)

##12.2 HTTP

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if ( len(data)<1):
        break
    print(data.decode())

mysock.close()