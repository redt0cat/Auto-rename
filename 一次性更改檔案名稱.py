#!/usr/bin/env python
# coding: utf-8

import os,shutil

name = 'D:\\高考函授\函授_系統分析設計_張又中'
print(name)
list = os.listdir(''+name)

#更改range 確認 要改的檔案在範圍內
for i in range(40):
    print(list[i])
    start = list[i]
    print(start)

#開始名稱 為要命名之路徑檔案
startname = name+'\\'
#更改名稱 為所要添加之命名之路徑檔案
rename = '函授_系統分析設計_張又中 '      


for i in range(47):
    print(list[i])
    start = startname+list[i]
    fin = startname+rename+list[i]
    print(start)
    print(fin)
    shutil.move(''+start, ''+fin)
