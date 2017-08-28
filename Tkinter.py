# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:06:40 2017

@author: yangjinyue
"""

from Tkinter import *
import difflib

root = Tk()
root.title('begger\'s calculator')
root.geometry()
Label_root = Label(root, text='规则运算（根框架）', font = ('宋体',15))

def Plus(a,b):
    return round(a+b,2)
    
