import datetime
from tkinter import *
import tkinter
from tkinter import ttk
import pandas as pd
from mpl_finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import talib

master = Tk()
subplot_number = 1
plotted_indicators = 0
added_indicators = []
company = pd.DataFrame()

'''
def matplotCanvas(n,ct,sym):
    figure = plt.Figure(figsize=(13,7), dpi=100)
    chart_type = FigureCanvasTkAgg(figure, master)
    ax = figure.add_subplot(111)
    NavigationToolbar2TkAgg(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 150, y = 40)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['MA'] = talib.MA(stock['CLOSE'], timeperiod = n)
    if(ct == "Candle-Stick"):
        axc = figure.add_subplot(111)
        candlestick_ohlc(axc, zip(mdates.date2num(stock.index.to_pydatetime()), stock['OPEN'], stock['HIGH'], stock['LOW'], stock['CLOSE']),width=0.5,colorup='g',colordown='r')
    elif(ct == "Line"):
        ax.plot(stock.index,stock['CLOSE'], label='CLOSE')
    ax.plot(stock.index,stock['MA'], label='MA')
    ax.set_title('ACC')
    ax.legend()
    ax.grid()
    #ax.show()
'''

figure = plt.Figure(figsize=(11,7), dpi=100, facecolor='lightsteelblue')

def initial_figure(ct):
    global change
    chart_type = FigureCanvasTkAgg(figure, master)
    NavigationToolbar2Tk(chart_type, master)
    #if(not(change)):
        #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = company
    stock = stock.iloc[::-1]
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    if(ct == "Candle-Stick"):
        axc = figure.add_subplot(subplot_number,1,1)
        axc.set_facecolor('aliceblue')
        candlestick_ohlc(axc, zip(mdates.date2num(stock.index.to_pydatetime()), stock['OPEN'], stock['HIGH'], stock['LOW'], stock['CLOSE']),width=0.5,colorup='g',colordown='r')
        axc.annotate(str(stock.CLOSE[-1]), (stock.index[-1], stock.CLOSE[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.CLOSE[-1]), bbox=bbox_props)
        loc = mdates.AutoDateLocator()
        axc.xaxis.set_major_locator(loc)
        axc.xaxis.set_major_formatter(mdates.AutoDateFormatter(loc))
        axc.grid()
        axc.tick_params(axis = 'x', labelrotation = 45)
    elif(ct == "Line"):
        ax = figure.add_subplot(subplot_number,1,1)
        ax.set_facecolor('aliceblue')
        ax.plot(stock.index,stock['CLOSE'], label='CLOSE')
        ax.annotate(str(stock.CLOSE[-1]), (stock.index[-1], stock.CLOSE[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.CLOSE[-1]), bbox=bbox_props)
        ax.legend()
        ax.grid(b=True)
        ax.tick_params(axis = 'x', labelrotation = 45)
  
def ma(n, sym):
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    ax = axs[0]
    ax.set_facecolor('aliceblue')
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['MA'] = talib.MA(stock['CLOSE'], timeperiod = n)
    lines = ax.plot(stock.index,stock['MA'], label = 'MA_' + str(n))
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.MA[-1],2)), (stock.index[-1], stock.MA[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.MA[-1]), bbox=bbox_props)
    ax.legend()
    ax.tick_params(axis = 'x', labelrotation = 45)
    
def bbands(n, sym):
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    ax = axs[0]
    ax.set_facecolor('aliceblue')
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 230, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['upperband'], stock['middleband'], stock['lowerband'] = talib.BBANDS(stock['CLOSE'], timeperiod = n)
    ax.fill_between(stock.index,stock['upperband'], stock['lowerband'],facecolor='blue', alpha=0.2, label = 'Bollinger Bands')
    ax.legend()
    ax.tick_params(axis = 'x', labelrotation = 45)

def rsi(n, sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    #print(subplot_number)
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['rsi'] = talib.RSI(stock['CLOSE'], timeperiod = n)
    ax.plot(stock.index, stock['rsi'], label = 'RSI')
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.rsi[-1],2)), (stock.index[-1], stock.rsi[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.rsi[-1]), bbox=bbox_props)
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def macd(sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    macd, macdsignal, macdhist = talib.MACD(stock['CLOSE'])
    stock['macd'] = macd
    stock['macdsignal'] = macdsignal
    ax.plot(stock.index, stock['macd'], label = 'MACD')
    ax.plot(stock.index, stock['macdsignal'], label = 'MACD Signal')
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.macd[-1],2)), (stock.index[-1], stock.macd[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.macd[-1]), bbox=bbox_props)
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.macdsignal[-1],2)), (stock.index[-1], stock.macdsignal[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.macdsignal[-1]), bbox=bbox_props)
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def vol(sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['volume'] = stock['VOLUME']/100000
    ax.bar(stock.index, stock['volume'], label = 'Volumes')
    ax.set_ylabel('Value in lakhs')
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def adx(n, sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['adx'] = talib.ADX(stock['HIGH'], stock['LOW'], stock['CLOSE'], timeperiod = n)
    stock['plusadx'] = talib.PLUS_DI(stock['HIGH'], stock['LOW'], stock['CLOSE'], timeperiod = n)
    stock['minusadx'] = talib.MINUS_DI(stock['HIGH'], stock['LOW'], stock['CLOSE'], timeperiod = n)
    ax.plot(stock.index, stock['adx'], label = 'ADX')
    ax.plot(stock.index, stock['plusadx'], label = '+ DM')
    ax.plot(stock.index, stock['minusadx'], label = '- DM')
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.adx[-1],2)), (stock.index[-1], stock.adx[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.adx[-1]), bbox=bbox_props)
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def apo(fn, sn, sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['apo'] = talib.APO(stock['CLOSE'], fastperiod = fn, slowperiod = sn)
    ax.plot(stock.index, stock['apo'], label = 'APO')
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.apo[-1],2)), (stock.index[-1], stock.apo[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.apo[-1]), bbox=bbox_props)
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def aroon(n, sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['aroondown'], stock['aroonup'] = talib.AROON(stock['HIGH'], stock['LOW'], timeperiod = n)
    ax.plot(stock.index, stock['aroondown'], label = 'AROONDOWN')
    ax.plot(stock.index, stock['aroonup'], label = 'AROONUP')
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.aroonup[-1],2)), (stock.index[-1], stock.aroonup[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.aroonup[-1]), bbox=bbox_props)
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.aroondown[-1],2)), (stock.index[-1], stock.aroondown[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.aroondown[-1]), bbox=bbox_props)
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def aroono(n, sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['aroonoscillator'] = talib.AROONOSC(stock['HIGH'], stock['LOW'], timeperiod = n)
    ax.plot(stock.index, stock['aroonoscillator'], label = 'AROON_OSCILLATOR')
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.aroonoscillator[-1],2)), (stock.index[-1], stock.aroonoscillator[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.aroonoscillator[-1]), bbox=bbox_props)
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def bop(sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['bop'] = talib.BOP(stock['OPEN'], stock['HIGH'], stock['LOW'], stock['CLOSE'])
    stock['pos'] = stock['bop'] > 0
    ax.bar(stock.index, stock['bop'], color=stock.pos.map({True: 'g', False: 'r'}))
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.bop[-1],2)), (stock.index[-1], stock.bop[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.bop[-1]), bbox=bbox_props)
    ax.set_ylabel('BOP')    
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def obv(sym):
    global subplot_number
    subplot_number += 1
    chart_type = FigureCanvasTkAgg(figure, master)
    axs = figure.get_axes()
    c = 1
    for ax1 in axs:
       ax1.change_geometry(subplot_number,1,c)
       ax1.axes.xaxis.set_visible(False)
       c += 1
    ax = figure.add_subplot(subplot_number,1,c,sharex = ax1)
    ax.set_facecolor('aliceblue')
    figure.subplots_adjust(hspace = 0.01)
    NavigationToolbar2Tk(chart_type, master)
    #chart_type.get_tk_widget().pack(side = 'bottom')
    chart_type.get_tk_widget().place(x = 235, y = 45)
    stock = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    stock = stock.iloc[::-1]
    stock['obv'] = talib.OBV(stock['CLOSE'],stock['VOLUME'])
    ax.plot(stock.index, stock['obv'], label = 'OBV')
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    ax.annotate(str(round(stock.obv[-1],2)), (stock.index[-1], stock.obv[-1]), xytext = (mdates.date2num(stock.index[-1].to_pydatetime()) +42, stock.obv[-1]), bbox=bbox_props)
    ax.legend()
    ax.grid()
    ax.get_shared_x_axes().join(ax, ax1)
    ax.tick_params(axis = 'x', labelrotation = 45)

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

'''
def moving_average():
    global change
    if(change):
         widget_list = all_children(master)
         #for item in widget_list:
         #    print(item)
         widget_list[5].pack_forget()
         widget_list[6].pack_forget()
    chart_type = str(option.get())
    print "value is", option.get()
    print "sym is ", E1.get()
    sym = str(E1.get())
    s = tkSimpleDialog.askstring('Inputs required','Number of Periods')
    n = int(s)
    print(n)
    matplotCanvas(n,chart_type,sym)
    change = True
    #master.quit()
'''

def moving_average():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    s = tkinter.simpledialog.askstring('Inputs required','Number of Periods')
    n = int(s)
    print(n)
    widget_list = all_children(master)
    #for item in widget_list:
    #    print(item)
    #print(widget_list)
    #for i in range(0,plotted_indicators + 1,1):
    #    widget_list[11+i*2].pack_forget()
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    ma(n, sym)
    added_indicators.append('MA_' + str(n))
    plotted_indicators += 1

def bollinger_bands():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    s = tkinter.simpledialog.askstring('Inputs required','Number of Periods')
    n = int(s)
    print(n)
    widget_list = all_children(master)
    #print(widget_list)
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    bbands(n, sym)
    added_indicators.append('bbands_' + str(n))
    plotted_indicators += 1

def relative_strength_index():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    s = tkinter.simpledialog.askstring('Inputs required','Number of Periods')
    n = int(s)
    print(n)
    widget_list = all_children(master)
    #print(widget_list)
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    rsi(n, sym)
    added_indicators.append('rsi_' + str(n))
    plotted_indicators += 1

def MACD():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    widget_list = all_children(master)
    #print(widget_list)
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    macd(sym)
    added_indicators.append('macd')
    plotted_indicators += 1

def volume():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    widget_list = all_children(master)
    #print(widget_list)
    #for i in range(0,plotted_indicators + 1,1):
    #    widget_list[11+i*2].pack_forget()
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    vol(sym)
    added_indicators.append('volume')
    plotted_indicators += 1

def ADX():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    s = tkinter.simpledialog.askstring('Inputs required','Number of Periods')
    n = int(s)
    print(n)
    widget_list = all_children(master)
    #print(widget_list)
    #for i in range(0,plotted_indicators + 1,1):
    #    widget_list[11+i*2].pack_forget()
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    adx(n, sym)
    added_indicators.append('ADX_' + str(n))
    plotted_indicators += 1

def APO():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    s = tkinter.simpledialog.askstring('Inputs Required','Fast-Period')
    fn = int(s)
    s = tkinter.simpledialog.askstring('Inputs Required','Slow-Period')
    sn = int(s)
    widget_list = all_children(master)
    #print(widget_list)
    #for i in range(0,plotted_indicators + 1,1):
    #    widget_list[11+i*2].pack_forget()
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    apo(fn, sn, sym)
    added_indicators.append('APO_' + str(fn) + '_' + str(sn))
    plotted_indicators += 1

def AROON():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    s = tkinter.simpledialog.askstring('Inputs required','Number of Periods')
    n = int(s)
    print(n)
    widget_list = all_children(master)
    #print(widget_list)
    #for i in range(0,plotted_indicators + 1,1):
    #    widget_list[11+i*2].pack_forget()
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    aroon(n, sym)
    added_indicators.append('AROON_' + str(n))
    plotted_indicators += 1

def AROONO():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    s = tkinter.simpledialog.askstring('Inputs required','Number of Periods')
    n = int(s)
    print(n)
    widget_list = all_children(master)
    #print(widget_list)
    #for i in range(0,plotted_indicators + 1,1):
    #    widget_list[11+i*2].pack_forget()
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    aroono(n, sym)
    added_indicators.append('Aroono_' + str(n))
    plotted_indicators += 1

def BOP():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    widget_list = all_children(master)
    #print(widget_list)
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    bop(sym)
    added_indicators.append('bop')
    plotted_indicators += 1

def OBV():
    global plotted_indicators
    global added_indicators
    sym = str(E1.get())
    widget_list = all_children(master)
    #print(widget_list)
    widget_list[button_number].destroy()    
    widget_list[button_number + 1].destroy()
    obv(sym)
    added_indicators.append('obv')
    plotted_indicators += 1

def initial_plot():
    global change
    global added_indicators
    global company
    sym = str(E1.get())
    company = pd.read_csv('/home/lokesh/ML/NIFTY-200/' + sym + '.csv',index_col=0,parse_dates=True,infer_datetime_format=True)
    if(change):
       figure.clf()
       chart_type = str(option.get())
       widget_list = all_children(master)
       #print(widget_list)
       #for i in range(0,plotted_indicators + 1,1):
       #    widget_list[11+i*2].pack_forget()
       widget_list[button_number].destroy()    
       widget_list[button_number + 1].destroy()
       global subplot_number
       subplot_number = 1
       initial_figure(chart_type)
       widget_list = all_children(master)
       #widget_list[button_number].destroy()    
       #widget_list[button_number + 1].destroy()
       global plotted_indicators
       plotted_indicators += 1
       for i in added_indicators:
           widget_list = all_children(master)
           if(i[:2] == 'MA'):
              ma(int(i[3:]),sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i[:6] == 'bbands'):
              bbands(int(i[7:]),sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i[:3] == 'rsi'):
              rsi(int(i[4:]),sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i == 'macd'):
              macd(sym)
              print(widget_list)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i == 'volume'):
              vol(sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i[:3] == 'ADX'):
              adx(int(i[4:]),sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i[:3] == 'APO'):
              l = i.split('_')
              apo(int(l[1]),int(l[2]),sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i[:5] == 'AROON'):
              aroon(int(i[6:]),sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i[:6] == 'Aroono'):
              aroono(int(i[7:]),sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i == 'bop'):
              bop(sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           elif(i == 'obv'):
              obv(sym)
              widget_list[button_number].destroy()    
              widget_list[button_number + 1].destroy()
              plotted_indicators += 1
           else:
              pass
    else:
        sym = str(E1.get())
        chart_type = str(option.get())
        initial_figure(chart_type)
        change = True
    #if(change):
    #   widget_list = all_children(master)
    #   widget_list[7].pack_forget()

def candlestick():
    cs = tkinter.Toplevel(master)
    #cs.geometry('1000x650')
    comp = company.iloc[::-1]
    stock = comp[-10:]
    available = {}
    stock['cs'] = talib.CDL2CROWS(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Two Crows'] = 'Bullish'
        elif i < 0:
           available['Two Crows'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDL3BLACKCROWS(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Three Black Crows'] = 'Bullish'
        elif i < 0:
           available['Three Black Crows'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDL3INSIDE(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Three Inside Up/Down'] = 'Bullish'
        elif i < 0:
           available['Three Inside Up/Down'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDL3LINESTRIKE(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Three-Line Strike'] = 'Bullish'
        elif i < 0:
           available['Three-Line Strike'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDL3OUTSIDE(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Three Outside Up/Down'] = 'Bullish'
        elif i < 0:
           available['Three Outside Up/Down'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDL3STARSINSOUTH (stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Three Stars In The South'] = 'Bullish'
        elif i < 0:
           available['Three Stars In The South'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDL3WHITESOLDIERS(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Three Advancing White Soldiers'] = 'Bullish'
        elif i < 0:
           available['Three Advancing White Soldiers'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLABANDONEDBABY(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Abandoned Baby'] = 'Bullish'
        elif i < 0:
           available['Abandoned Baby'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLADVANCEBLOCK(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Advance Block'] = 'Bullish'
        elif i < 0:
           available['Advance Block'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLBELTHOLD(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Belt-hold'] = 'Bullish'
        elif i < 0:
           available['Belt-hold'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLBREAKAWAY(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Breakaway'] = 'Bullish'
        elif i < 0:
           available['Breakaway'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLCLOSINGMARUBOZU(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Closing Marubozu'] = 'Bullish'
        elif i < 0:
           available['Closing Marubozu'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLCONCEALBABYSWALL(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Concealing Baby Swallow'] = 'Bullish'
        elif i < 0:
           available['Concealing Baby Swallow'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLCOUNTERATTACK(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Counter Attack'] = 'Bullish'
        elif i < 0:
           available['Counter Attack'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLDARKCLOUDCOVER(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Dark Cloud Cover'] = 'Bullish'
        elif i < 0:
           available['Dark Cloud Cover'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLDOJI(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Belt-hold'] = 'Bullish'
        elif i < 0:
           available['Belt-hold'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLDOJI(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Doji'] = 'Bullish'
        elif i < 0:
           available['Doji'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLDOJISTAR(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Doji Star'] = 'Bullish'
        elif i < 0:
           available['Doji Star'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLDRAGONFLYDOJI(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Dragonfly Doji'] = 'Bullish'
        elif i < 0:
           available['Dragonfly Doji'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLENGULFING(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Engulfing Pattern'] = 'Bullish'
        elif i < 0:
           available['Engulfing Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLEVENINGDOJISTAR(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Evening Doji Star'] = 'Bullish'
        elif i < 0:
           available['Evening Doji Star'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLEVENINGSTAR(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Evening Star'] = 'Bullish'
        elif i < 0:
           available['Evening Star'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLGAPSIDESIDEWHITE(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Up/Down-gap side-by-side white lines'] = 'Bullish'
        elif i < 0:
           available['Up/Down-gap side-by-side white lines'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLGRAVESTONEDOJI(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Gravestone Doji'] = 'Bullish'
        elif i < 0:
           available['Gravestone Doji'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLHAMMER(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Hammer'] = 'Bullish'
        elif i < 0:
           available['Hammer'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLHANGINGMAN(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Hanging Man'] = 'Bullish'
        elif i < 0:
           available['Hanging Man'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLHARAMI(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Harami Pattern'] = 'Bullish'
        elif i < 0:
           available['Harami Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLHARAMICROSS(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Harami Cross Pattern'] = 'Bullish'
        elif i < 0:
           available['Harami Cross Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLHIGHWAVE(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['High-Wave Candle'] = 'Bullish'
        elif i < 0:
           available['High-Wave Candle'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLHIKKAKE(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Hikkake Pattern'] = 'Bullish'
        elif i < 0:
           available['Hikkake Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLHIKKAKEMOD(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Modified Hikkake Pattern'] = 'Bullish'
        elif i < 0:
           available['Modified Hikkake Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLHOMINGPIGEON(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Homing Pigeon'] = 'Bullish'
        elif i < 0:
           available['Homing Pigeon'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLIDENTICAL3CROWS(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Identical Three Crows'] = 'Bullish'
        elif i < 0:
           available['Identical Three Crows'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLINNECK(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['In-Neck Pattern'] = 'Bullish'
        elif i < 0:
           available['In-Neck Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLINVERTEDHAMMER(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Inverted Hammer'] = 'Bullish'
        elif i < 0:
           available['Inverted Hammer'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLKICKING(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Kicking'] = 'Bullish'
        elif i < 0:
           available['Kicking'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLKICKINGBYLENGTH(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Kicking - bull/bear determined by the longer marubozu'] = 'Bullish'
        elif i < 0:
           available['Kicking - bull/bear determined by the longer marubozu'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLLADDERBOTTOM(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Ladder Bottom'] = 'Bullish'
        elif i < 0:
           available['Ladder Bottom'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLLONGLEGGEDDOJI(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Long Legged Doji'] = 'Bullish'
        elif i < 0:
           available['Long Legged Doji'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLLONGLINE(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Long Line Candle'] = 'Bullish'
        elif i < 0:
           available['Long Line Candle'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLMARUBOZU(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Marubozu'] = 'Bullish'
        elif i < 0:
           available['Marubozu'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLMATCHINGLOW(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Matching Low'] = 'Bullish'
        elif i < 0:
           available['Matching Low'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLMATHOLD(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Mat Hold'] = 'Bullish'
        elif i < 0:
           available['Mat Hold'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLMORNINGDOJISTAR(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Morning Doji Star'] = 'Bullish'
        elif i < 0:
           available['Morning Doji Star'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLMORNINGSTAR(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Morning Star'] = 'Bullish'
        elif i < 0:
           available['Morning Star'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLONNECK(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['On-Neck Pattern'] = 'Bullish'
        elif i < 0:
           available['On-Neck Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLPIERCING(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Piercing Pattern'] = 'Bullish'
        elif i < 0:
           available['Piercing Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLRICKSHAWMAN(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Rickshaw Man'] = 'Bullish'
        elif i < 0:
           available['Rickshaw Man'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLRISEFALL3METHODS(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Rising/Falling Three Methods'] = 'Bullish'
        elif i < 0:
           available['Rising/Falling Three Methods'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLSEPARATINGLINES(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Separating Lines'] = 'Bullish'
        elif i < 0:
           available['Separating Lines'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLSHOOTINGSTAR(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Shooting Star'] = 'Bullish'
        elif i < 0:
           available['Shooting Star'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLSHORTLINE(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Short Line Candle'] = 'Bullish'
        elif i < 0:
           available['Short Line Candle'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLSPINNINGTOP(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Spinning Top'] = 'Bullish'
        elif i < 0:
           available['Spinning Top'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLSTALLEDPATTERN(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Stalled Pattern'] = 'Bullish'
        elif i < 0:
           available['Stalled Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLSTICKSANDWICH(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Stick Sandwich'] = 'Bullish'
        elif i < 0:
           available['Stick Sandwich'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLTAKURI(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Takuri'] = 'Bullish'
        elif i < 0:
           available['Takuri'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLTASUKIGAP(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Tasuki Gap'] = 'Bullish'
        elif i < 0:
           available['Tasuki Gap'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLTHRUSTING(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Thrusting Pattern'] = 'Bullish'
        elif i < 0:
           available['Thrusting Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLTRISTAR(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Tristar Pattern'] = 'Bullish'
        elif i < 0:
           available['Tristar Pattern'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLUNIQUE3RIVER(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Unique 3 River'] = 'Bullish'
        elif i < 0:
           available['Unique 3 River'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLUPSIDEGAP2CROWS(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Upside Gap Two Crows'] = 'Bullish'
        elif i < 0:
           available['Upside Gap Two Crows'] = 'Bearish'
        else:
           pass
    stock['cs'] = talib.CDLXSIDEGAP3METHODS(stock['OPEN'],stock['HIGH'],stock['LOW'],stock['CLOSE'])
    for i in stock.cs:
        if i > 0:
           available['Upside/Downside Gap Three Methods'] = 'Bullish'
        elif i < 0:
           available['Upside/Downside Gap Three Methods'] = 'Bearish'
        else:
           pass
    #print(available)
    r = 0
    for c in available.keys():
     Label(cs, text=c, relief=RIDGE,  width=50).grid(row=r, column=0)
     if(available[c] == 'Bearish'):
        color = 'red'
     else:
        color = 'green'
     Label(cs, text=available[c], bg=color, relief=RIDGE,  width=25).grid(row=r, column=1)
     r = r+1
    if(available == {}):
       Label(cs, text='No Patterns Can Be Identified Currently', relief=RIDGE,  width=50).grid(row=r, column=0)
#header = Frame(master)
#header.pack(side = 'top')
#header.place(x = 0, y =4)

change = False
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

enter_button = Button(master, text="ENTER", command=initial_plot)
enter_button.place(x = 300, y = 4)

#chart_option = Frame(master)
#chart_option.pack(side = 'right')
option = ttk.Combobox(master, values=['Candle-Stick','Line'], state='readonly')
option.place(x = 1400, y = 10)
option.set('Candle-Stick')
ct = option.get()

#indicators = Frame(master)
#indicators.pack(side = 'left')
button_number = 17
L1 = Label(master, text="Chart Indicators :")
L1.place(x = 2,y = 40)

button_ma = Button(master, text="Moving Average", command=moving_average)
button_ma.place(x = 5, y = 70)
button_bbands = Button(master, text="Bollinger Bands", command=bollinger_bands)
button_bbands.place(x = 5, y = 100)
button_rsi = Button(master, text="Relative Strength Index", command=relative_strength_index)
button_rsi.place(x = 5, y = 130)
button_macd = Button(master, text="Macd", command=MACD)
button_macd.place(x = 5, y = 160)
button_vol = Button(master, text="Volume", command=volume)
button_vol.place(x = 5, y = 190)
button_adx = Button(master, text="Average Directional Movement", command=ADX)
button_adx.place(x = 5, y = 220)
button_apo = Button(master, text="Absolute Price Oscillator", command=APO)
button_apo.place(x = 5, y = 250)
button_aroon = Button(master, text="Aroon", command=AROON)
button_aroon.place(x = 5, y = 280)
button_aroono = Button(master, text="Aroon Oscillator", command=AROONO)
button_aroono.place(x = 5, y = 310)
button_bop = Button(master, text="Balance Of Power", command=BOP)
button_bop.place(x = 5, y = 340)
button_obv = Button(master, text="On Balance Volume", command=OBV)
button_obv.place(x = 5, y = 370)

#candlestick optipon
button_bop = Button(master, text="Identify the Candlestick Patterns", command=candlestick)
button_bop.place(x = 1350, y = 50)

master.geometry('1520x750')
mainloop()
