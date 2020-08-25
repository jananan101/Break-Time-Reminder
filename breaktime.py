from tkinter import *
import tkinter as tk
import datetime
import winsound

#secondary window
T = tk.Text(tk.Tk(), height=2, width=30)
T.pack()

#method used to compare time and sound alarm
def click():
    hour = int(hourentry.get())
    mini = int(minentry.get())
    sec = int(secentry.get())
    ampm = ampmentry.get()
    
    if(ampm == "pm" or ampm == "PM"):
        hour = hour + 12


    while(1):
        if(hour == datetime.datetime.now().hour and mini == datetime.datetime.now().minute and sec == int(datetime.datetime.now().second)):
            message = "Take a Break\n"
            
            T.insert(END,message)
            winsound.PlaySound("SystemAsterisk",winsound.SND_ALIAS)
            break

#main window
window = Tk()
window.title("Break Time")

Label (window, text="Set the time for break [hour,minute,seconds,AM/PM]",bg="white",fg="black",font="none 12 bold").grid(row=1,column=0,sticky=N)

hourentry = Entry(window,width=20,bg="white")
hourentry.grid(row=2,column=0,sticky=W)

minentry = Entry(window,width=20,bg="white")
minentry.grid(row=3,column=0,sticky=W)

secentry = Entry(window,width=20,bg="white")
secentry.grid(row=4,column=0,sticky=W)

ampmentry = Entry(window,width=20,bg="white")
ampmentry.grid(row=5,column=0,sticky=W)



Button(window, text="SET",width=3,command=click).grid(row=6,column=3,sticky=W)

