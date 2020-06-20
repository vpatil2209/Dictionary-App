# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:58:38 2020

@author: vishal
"""

from tkinter import *

base = Tk()
base.geometry('200x200')

def find_meaning():
    print("")
#search = Entry(root, font("Times New Roman", 14, "Bold"))
#search.grid(row = 2, column = 2)
stud = Button(base, text = 'Tutorialspoint', font =('Courier',14, 'bold'))
stud.grid(row = 4, column = 2)

root.mainloop()