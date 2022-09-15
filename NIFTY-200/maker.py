'''import datetime
import pandas as pd
import numpy as np

article_read = pd.read_csv('ind_nifty200list.csv')
company = ['RNAM']
x = datetime.datetime.now()
eq = 'EQ'
for i in company:
  file1 = open(i+".csv","a")
  print(i)
  outs = 'DATE' + "," + 'OPEN' + "," + 'CLOSE' + "," + 'HIGH' + ','+ 'LOW' + ','+ 'VOLUME' + "\n"
  #print(outs)
  file1.write(outs)
  j = 136
  n = 1620 
  z = 0
  k = 0
  while n>0:
   try:
    day = x - datetime.timedelta(days=j)
    m = day.strftime("%b")
    y = day.strftime("%Y")
    d = day.strftime("%d")
    fnamer = 'cm' + d + m.upper() + y + 'bhav.csv'
    #surlid = 'https://www1.nseindia.com/content/historical/EQUITIES/' + y +'/' + m.upper() + '/' + fnamer + '.zip'
    #r = requests.get(surlid)
    #z = zipfile.ZipFile(io.BytesIO(r.content))
    #z.extractall('/home/lokesh/ML/Market')
    try:
     article_read = pd.read_csv('/home/lokesh/ML/Market/' + fnamer)
    except:
     article_read = pd.read_csv('/home/lokesh/ML/Download/' + fnamer)
    s = str(article_read[np.logical_and(article_read.SYMBOL == i,article_read.SERIES == eq)][['TIMESTAMP','OPEN','CLOSE','HIGH','LOW','TOTTRDQTY']])
    a = s.split(' ')
    #print(s)
    l = list(a)
    l = list(filter(None, l))
    print(l)
    #zzz = float(l[-1])
    if(l[-1]!='[]'): 
     outs = l[-6] + ',' + l[-5] + "," + l[-4] + "," + l[-3] + "," + l[-2] + "," + l[-1] + "\n"
     #print(outs)
     file1.write(outs)
     #costs.append(float(l[len(l)-1]))
     #mdate.append(day.strftime("%x"))
     n -=1
     k = 0
    else:
     k+=1
    if(k==10):
      break
    print(n)
    j +=1
    z = 0
    #l[11] = symbol
    #l[last] = close
    #print(i)
   except:
    j +=1  
    print(n)
    z+=1
    if(z==10):
      break 

  file1.close() 
'''
