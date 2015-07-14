# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:52:20 2015

@author: JackChen
"""
import os
from xlsx2csv import *# convert all xlsx files that filename strat with 紀錄 to file "info"
def convertxlsx2csv():
    dirs = os.listdir()
    for directory in dirs:
        if(directory[0]!="0"):
            continue
        os.chdir("./"+directory)
        filename = "./"+directory+"紀錄"+".xlsx"
        filename.encode('big5')
        Xlsx2csv(filename).convert("info")
        os.chdir("..")
