import os, sys
import pandas as pd
import datetime
import requests
import requests, zipfile, io
article_read = pd.read_csv('ind_nifty200list.csv')
#article_read = pd.read_csv('EQUITY_L.csv')
#company = ['ACC']
x = datetime.datetime.now()
company = list(article_read['Symbol'])
print(company)
print(type(company))
n = 1
j = 0
k = 0

while n>0:
    day = x - datetime.timedelta(days=j)
    m = day.strftime("%b")
    y = day.strftime("%Y")
    d = day.strftime("%d")
    fnamer = 'cm' + d + m.upper() + y + 'bhav.csv'
    print(fnamer)
    #if(os.path.exists('/home/lokesh/ML/Download/' + fnamer)):
    #     j -= 1
    #     k = 1
    #     print('gasfgafg')
    #     break
    #surlid = 'https://www1.nseindia.com/content/historical/EQUITIES/' + y +'/' + m.upper() + '/' + fnamer + '.zip'
    #r = requests.get(surlid)
    #z = zipfile.ZipFile(io.BytesIO(r.content))
    #else:
    try:
         #surlid = 'https://www1.nseindia.com/content/historical/EQUITIES/' + y +'/' + m.upper() + '/' + fnamer + '.zip'
         #r = requests.get(surlid)
         #z = zipfile.ZipFile(io.BytesIO(r.content))
         #z.extractall('/home/lokesh/ML/Download')
         #print('DOWNLOADED')
         article_read = pd.read_csv('/home/lokesh/ML/Download/' + fnamer)
         n -=1
         #print('try')
         z = 0
         k = 0
         j -=1
         for i in company:
            try:
 	    #We read the existing text from file in READ mode
             article_read = article_read[article_read.SERIES == 'EQ'] 
             s = str(article_read[article_read.SYMBOL == i][['TIMESTAMP','OPEN','HIGH','LOW','CLOSE','TOTTRDQTY']])
             a = s.split(' ')
             #print(s)
             l = list(a)
             l = list(filter(None, l))
             print(i,l)
             if(l[0]!='Empty'):
              #zzz = float(l[-1]) 
              outs = l[-6] + "," + l[-5] + "," + l[-2] + "," + l[-4] + "," + l[-3] + "," + l[-1] + "\n"
              src=open(i + ".csv","r")
              fline=outs    #Prepending string
              oline=src.readlines()
              #print(type(oline[0]))
              #print(type(outs))
              s = str(oline[0])
              #Here, we prepend the string we want to on first line
              oline.insert(1,fline)
              src.close()
              src=open(i + ".csv","w")
              src.writelines(oline)
              src.close()
              print('sdrgtuu')
            except:
              pass
    except:
         n -=1
         print('except')
         j -= 1
         z = 0
         k = 1
      #l[11] = symbol
      #l[last] = close


'''
#if(n==0 and k==0):
for i in company:
  try:
     #We read the existing text from file in READ mode
     print(i)
     #s = str(article_read[article_read.SYMBOL == i][['TIMESTAMP','CLOSE']])
     #a = s.split(' ')
     #print(s)
     #l = list(a)
     #l = list(filter(None, l))
     #print(l)
     #zzz = float(l[-1]) 
     #outs = l[-2] + "," + l[-1] + "\n"
     src=open(i + ".csv","r")
     fline= "Date,Price\n"    #Prepending string
     oline=src.readlines()
     #print(type(oline[0]))
     #print(type(outs))
     s = str(oline[0])
     #Here, we prepend the string we want to on first line
     oline.insert(0,fline)
     src.close()
     #We again open the file in WRITE mode for deleting rows
     src=open(i + ".csv","w")
     src.writelines(oline)
     src.close()
     #readFile = open(i + ".csv")
     #lines = readFile.readlines()
     #readFile.close()
     #w = open(i + ".csv",'w')
     #w.writelines([item for item in lines[:-1]])
     #w.close()
     #print(outs)
  except:
     pass
'''
