# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:16:45 2020

@author: vishal
"""

from tkinter import *

#Click fuction

def click():
    output.delete(0.0,'end')#clearing o/p box
    iptext = Enter_text.get().lower()
    
    
    f = open("Dict.txt")
    for i in f.readlines():
        
        x = i.split(":")[0]
        y = i.split(":")[1]
        
        if iptext == x.lower():
            output.insert(0.0,y)#inserting meaning in o/p box
            break
    else:
         output.insert(0.0,"WORD NOT FOUND")
    f.close()


# Window
window = Tk()
window.title('Welcome to Dictionary App')
window.geometry('500x550')
window.configure(background = 'black')


# Search Box
Label(window, text = "Search Box", bg = "black", fg = "white",
      font = "courier 14 bold").grid(row = 1,column = 0, sticky = W)


# Enter text here
Enter_text = Entry(window, width = 40, bg = 'white')
Enter_text.grid(row = 1, column = 2, sticky = W)


# Search Button 
Button(window, text = "Search", width = 10, command = click).grid(row = 2, column = 2, sticky = W)


# Result 
Label(window, text = "Result", bg = "black", fg = "white",
      font = "courier 14 bold").grid(row = 4,column = 0, sticky = W)


# Actual Result Display
output = Text(window, width = 40, height = 10, wrap = "word", bg = "white")
output.grid(row = 4,column = 2, columnspan = 1, sticky = W)


window.mainloop()
