# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import shutil

class Chdir:         
      def enter(self,Path):
        self.savedPath = os.getcwd()
        os.chdir(Path)
      def __del__( self ):
        os.chdir( self.savedPath )
      def write(self):
        object = open("test.txt","w")
        object.write("test complete 2")
        object.close()
"""
mainP = os.getcwd()
try:    
    mover = Chdir()
    mover.enter(mainP+"/test")
    mover.write()
    del mover
except OSError:
    print("cannot go to the directory")"""
"""
savedPath = os.getcwd()    
os.chdir(savedPath+"/test")
print("we are now in "+os.getcwd())
print("savePath ="+savedPath)
for i in range(20):    
    try:
        os.mkdir(savedPath+"/test/test"+str(i),755)
    except FileExistsError:
        continue
os.chdir("..") """
"""
savedPath = os.getcwd()    
os.chdir(savedPath+"/test")
"""

# define the function blocks
def laugh(string,directory):#accumulate the audio file with laughter
    print ("in laugh")
    string = string[1:]
    if not string:
        Path = os.getcwd()
        print(Path+"no laughter return")
        
        return
    else:
        Path = os.getcwd()
        print(Path)
        for file in string:
            filename = "split_wav"+file+".wav"
            try:                
                p = os.path.join(Path, filename)
                t = os.path.join(Path, directory+ filename)
                os.rename(p,t)
                #filename=directory+ filename
                shutil.move(t, "../laughter")
                print(t+" move complete")
            except FileExistsError:
                print("file not exist")
            except OSError:
                print("OS error")
def clap(string,directory):#accumulate the audio file with clap
    print ("in clap")
    string = string[1:]
    if not string:
        return
    else:
        print(string)
        Path = os.getcwd()
        print(Path)
        for file in string:
            filename = "split_wav"+file+".wav"
            try:                
                p = os.path.join(Path, filename)
                t = os.path.join(Path, directory+ filename)
                os.rename(p,t)
                #filename=directory+ filename
                shutil.move(t, "../clap")
                print(t+" move complete")
            except FileExistsError:
                print("file not exist")
            except OSError:
                print("OS error")

# map the inputs to the function blocks
options = {"laughter" : laugh,
           "clap" : clap,
}

def collect():#find the chosen file information in file "info_collect" and throw them in laughter and clap directory
    dirs = os.listdir()
    savedPath = os.getcwd() 
    try:
        os.mkdir("./clap")
        os.mkdir("./laughter")
    except FileExistsError:
        for directory in dirs:#search every sub directory    
            if(directory[0]=="0"):#skip the files that are non-directory
                try:
                    os.chdir(savedPath+"/"+directory)
                    try:
                        f = open("info_collect","r+")
                        for line in f:
                            line=line[0:-1]
                            string=line.split(",")
                            options[string[0]](string,directory)
                            #os.chdir("..")
                        f.close()
                    except IOError:
                        print("info file not exist")
                except PermissionError:
                    continue
            else:
                continue

"""
dirs = os.listdir()
for directory in dirs:
    try:
        if(directory[0]=="0"):
            shutil.copy("./info", os.getcwd()+"/"+directory)
    except PermissionError:
        continue
"""