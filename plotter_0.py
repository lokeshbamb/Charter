import os, sys
import random
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from tkinter import *
import tkinter
from tkinter import ttk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

master = Tk()
figure = plt.Figure(figsize=(14.5,9))
E1 = ttk.Combobox()
change = False

def read_nse():
	df = pd.read_csv("^NSEI.csv",index_col=0,parse_dates=True,infer_datetime_format=True)
	return df
	
def read_company(sym):
	df = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
	return df
	
def normalize(df):
	mean = np.mean(df['prop'].tail(14))
	std = np.std(df['prop'].tail(14))
	c = (float(df.iloc[-1, -1])-mean)/std + 101
	return c

def company(sym, temp):
	temp.dropna(inplace = True)
	#temp["rs_ratio"] = 100 * ((temp['CLOSE'] - temp['OPEN'])/temp['OPEN']) / ((temp['Close'] - temp['Open'])/temp['Open'])
	temp["prop"] = temp['CLOSE']/temp['Close'] * 100
	l = []
	for i in range(0, -110, -1):
		if(i == 0):
			df = temp.iloc[:,:]
			#mean = np.mean(df['prop'].tail(14))
			#std = np.std(df['prop'].tail(14))
			#c = (float(df.iloc[-1, -1])-mean)/std + 101
			#print(float(df.iloc[-1, -1]), mean, std)
			c = normalize(df)
			l.append(c)
		else:
			df = temp.iloc[:i,:]
			#mean = np.mean(df['prop'].tail(14))
			#std = np.std(df['prop'].tail(14))
			#c = (float(df.iloc[-1, -1])-mean)/std + 101
			#print(float(df.iloc[-1, -1]), mean, std)
			c = normalize(df)
			l.append(c)
	#print(l)
	#print(float(df.iloc[-1, 0]))
	l.reverse()
	rs_ratio = pd.Series(l)
	l = list(rs_ratio.pct_change() * 100)
	#print(l)
	m = []
	for i in range(13, len(l), 1):
		mean = np.mean(l[i-13:i+1])
		std = np.std(l[i-13:i+1])
		c = (l[i]-mean)/std + 101
		m.append(c)
	#print(len(m))
	l = list(rs_ratio.iloc[13:])
	#print(len(l))
	#print(temp)
	temp.to_csv("temp.csv")
	chart_type = FigureCanvasTkAgg(figure, master)
	NavigationToolbar2Tk(chart_type, master)
	ax = figure.add_subplot(1,1,1)
	bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
	chart_type.get_tk_widget().place(x = 235, y = 45)
	ax.plot(l[-10:],m[-10:], marker='o')
	ax.plot(l[-1],m[-1], marker='o', color='gray')
	ax.axhline(y = 100, color = 'black', linestyle = '--')
	ax.axvline(x = 100, color = 'black', linestyle = '--')
	ax.axvspan(0,100, ymin=0, ymax=0.5, facecolor = 'red', alpha=0.2)
	ax.axvspan(100,200, ymin=0, ymax=0.5, facecolor = 'yellow', alpha=0.2)
	ax.axvspan(0,100, ymin=0.5, ymax=1, facecolor = 'blue', alpha=0.2)
	ax.axvspan(100,200, ymin=0.5, ymax=1, facecolor = 'green', alpha=0.2)
	y = max(int(max(m[-10:])) - 100, 100 - int(min(m[-10:]))) + 1
	x = max(int(max(m[-10:])) - 100, 100 - int(min(m[-10:]))) + 1
	#print(x, y)
	ax.text(100.05 - x, 100.1 - y, "Lagging", color = 'red', fontsize = 'x-large', fontweight = 500)
	ax.text(100.05 - x, 99.8 + y, "Improving", color = 'blue', fontsize = 'x-large', fontweight = 500)
	ax.text(100 + x - 0.6, 100.1 - y, "Weakening", color = 'orange', fontsize = 'x-large', fontweight = 500)
	ax.text(100 + x - 0.45, 99.8 + y, "Leading", color = 'green', fontsize = 'x-large', fontweight = 500)
	ax.text(l[-1], m[-1], "current", color = 'gray')
	ax.set_title(sym, fontsize = 'xx-large', fontweight = 1000)
	#ax.spines.left.set_position(('axes', 100))
	#ax.spines.right.set_color('none')
	#ax.spines.bottom.set_position(('axes', 100))
	#ax.spines.top.set_color('none')
	#ax.xaxis.set_ticks_position('bottom')
	#ax.yaxis.set_ticks_position('left')
	ax.set_ylim(ymin = 100 - y, ymax = 100 + y)
	ax.set_xlim(xmin = 100 - x, xmax = 100 + x)
	ax.set_ylabel("RS-Momentum", fontsize = 'xx-large')
	ax.set_xlabel("RS-Ratio", fontsize = 'xx-large')
	ax.grid()
	#plt.show()
	#print(temp["rs_ratio"].pct_change())

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def get_selected():
	global change
	sym = str(E1.get())
	#sym = "ACC"
	if(change):
		figure.clf()
		widget_list = all_children(master)
		#print(widget_list)
		widget_list[4].destroy() 
		widget_list[5].destroy()
		nse = read_nse()
		comp = read_company(sym)
		temp = pd.concat([nse, comp], axis=1)
		company(sym, temp)
	else:
		sym = str(E1.get())
		nse = read_nse()
		comp = read_company(sym)
		temp = pd.concat([nse, comp], axis=1)
		company(sym, temp)
		change = True

def main():
	global change
	global E1
	
	df = pd.read_csv('ind_nifty200list.csv')
	stocks = list(df['Symbol'])
	stocks.append('NSEI')
	
	L1 = Label(master, text="Script Symbol :")
	L1.place(x = 2,y = 10)
	#L1.pack(side = 'left')
	
	E1 = ttk.Combobox(master, values=stocks, state='readonly')
	E1.place(x = 110, y = 8)
	#E1.pack(side = 'left')
	E1.set('ACC')
	
	enter_button = Button(master, text="ENTER", command=get_selected)
	enter_button.place(x = 300, y = 4)
	master.geometry('1920x1080')

	mainloop()

if __name__ == "__main__":
	main()
