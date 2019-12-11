#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:14:16 2019

@author: wei
"""
import os
import re

def get_filelist(dir, Filelist): 
    newDir = dir 
    if os.path.isfile(dir): 
        Filelist.append(dir) 
        # # 若只是要返回文件文，使用这个 
        # Filelist.append(os.path.basename(dir))
    elif os.path.isdir(dir): 
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s) 
            get_filelist(newDir, Filelist)
    return Filelist

def print_log(word,control):
    if control == True:
        print(word)

dirnow = "/home/wei/文档/coq/AutoMaths"
keyword = "pymdownx"
filetype = ""
printcontent = False
Filelist = get_filelist(dirnow,[])
for file in Filelist:
    if file.endswith(filetype):
        f = open(file,'r',errors="ignore")
        content = f.read()
        f.close()
        keynum = len(re.findall(keyword,content))
        
        if keynum>0 :
            print(file)
            print_log(content,printcontent)
        
    