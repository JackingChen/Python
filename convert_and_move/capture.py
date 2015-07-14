# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:57:45 2015

@author: JackChen
"""
import os
def changeFormat():# process csv file transformed last time to more desired one
    f = open("info","r+")
    string =[]
    laughter=[]
    clap=[]
    for line in f:
        string.append(line.split(","))
    for i in range(len(string)):
        if any("laugh" in s for s in string[i]):# find any item in list "string" that matches "laugh" in the string
            s= [a for a in string[i] if "s" in a]# collect the 
            s1=s[0]
            laughter.append(s1[1:])
        if any("clap" in s for s in string[i]):
            s= [a for a in string[i] if "s" in a]
            s1=s[0]
            clap.append(s1[1:])
    lauStr=""
    claStr=""
    for i in laughter:
        lauStr = lauStr+","+i
    for i in clap:
        claStr = claStr+","+i
    f1=open("info_collect","w")
    f1.writelines("laughter"+lauStr+"\n")
    f1.writelines("clap"+claStr+"\n")
    f.close()
    f1.close()
def do_changeFormat():#sneak in all the directories and change the format
    dirs = os.listdir()
    savedpath=os.getcwd()
    for directory in dirs:
        if(directory[0]=="0"):        
            os.chdir("./"+directory)
            changeFormat()
            os.chdir(savedpath)