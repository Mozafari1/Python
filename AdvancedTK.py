# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 23:47:22 2018

@author: m_rah
"""

import tkinter
import os
#
#print(tkinter.TkVersion)
#print(tkinter.TclVersion)
#tkinter._test()
# 

Window=tkinter.Tk()
Window.title("Grid Demo Window")
Window.geometry('640x480-8-200')
Window['padx']=8

label= tkinter.Label(Window, text='Tkinter Grid Demo Window')
label.grid(row=0, column=0, columnspan=3)
Window.columnconfigure(0, w=1)
Window.columnconfigure(1, w=1)
Window.columnconfigure(2, w=3)
Window.columnconfigure(3, w=3)
Window.columnconfigure(4, w=3)
Window.rowconfigure(0, w=1)
Window.rowconfigure(1, w=10)
Window.rowconfigure(2, w=1)
Window.rowconfigure(3, w=3)
Window.rowconfigure(4, w=3)

fileList=tkinter.Listbox(Window)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END,zone)

Scroll = tkinter.Scrollbar(Window, orient=tkinter.VERTICAL, command=fileList.yview)
Scroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand']=Scroll.set

optinFrame=tkinter.LabelFrame(Window, text="file detail")
optinFrame.grid(row=1, column=2, sticky='ne')
rbValue= tkinter.IntVar()
rbValue.set(3)
radio1=tkinter.Radiobutton(optinFrame, text="Filename", value=1, variable=rbValue)
radio2=tkinter.Radiobutton(optinFrame, text="Path", value=2, variable=rbValue)
radio3=tkinter.Radiobutton(optinFrame, text="Timers", value=3, variable=rbValue)

radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

result= tkinter.Label(Window, text="Result")
result.grid(row=2, column=2, sticky='nw')
result=tkinter.Entry(Window)
result.grid(row=2, column=2, sticky='sw')

timeFrame= tkinter.LabelFrame(Window, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
HS=tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
MS=tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
SS=tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
HS.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
MS.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
SS.grid(row=0, column=4)
timeFrame['padx']=36

DateFrame= tkinter.LabelFrame(Window)
DateFrame.grid(row=4, column=0, sticky='new')
DL=tkinter.Label(DateFrame, text="Day")
ML=tkinter.Label(DateFrame, text="Month")
YL=tkinter.Label(DateFrame, text="Year")

DL.grid(row=0, column=0, sticky='w')
ML.grid(row=0, column=1, sticky='w')
YL.grid(row=0, column=2, sticky='w')

DS=tkinter.Spinbox(DateFrame, width=5, values=tuple(range(1,32)))
MSS=tkinter.Spinbox(DateFrame, width=5, from_=1, to=12)

YS=tkinter.Spinbox(DateFrame, width=6, from_=0, to=10000)
DS.grid(row=1, column=0)
MSS.grid(row=1, column=1)
YS.grid(row=1, column=2)
DateFrame['padx']=36

okb = tkinter.Button(Window, text="OK")
cb= tkinter.Button(Window, text="Cancel", command=Window.destroy)
okb.grid(row=4, column=3, sticky='e')
cb.grid(row=4, column=4, sticky='w')

Window.mainloop()
print(rbValue.get())