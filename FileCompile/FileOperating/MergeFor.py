#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @Time    : 2018/5/18
    @Author  : LiuXueWen
    @Site    : 
    @File    : MergeFor.py
    @Software: PyCharm
    @Description: 循环所有合并，检查所有文件夹是否合并完成（避免同级多文件夹存在）
'''

import os

import FileMerge
import FileFunction
import properties

fileFullPath3 = properties.fileFullPath3
fileFullPath2 = properties.fileFullPath2

# # 设置需要合并的本地文件路径
# fileFullPath3 = "/root/LXW/new/"
# # 设置本地文件合并后的输出路径
# fileFullPath2 = "/root/LXW/dat/"

def MergeFor():
    sum = 0
    rebuild = FileMerge
    rebuildFile = rebuild.rebuildFile()
    MergeFile = rebuild.MergeFile()
    # 获取实际文件夹的路径
    fileFullPath = rebuildFile[2]
    # 获取filelist文件列表
    for fileRealName in os.listdir(fileFullPath2):
        print "f1:"+fileRealName
    fileName = MergeFile
    totleSize = os.path.getsize(fileFullPath2 + "/" + str(fileName))
    # 计算文件夹下每个文件的大小
    for files in os.listdir(fileFullPath):
        # 获取每个文件的大小
        size = os.path.getsize(fileFullPath + "/" + files)
        sum = sum+size
    return fileRealName,fileName,totleSize,sum

def con():
    Mer = MergeFor()
    fileRealName = Mer[0]
    fileName = Mer[1]
    totleSize = Mer[2]
    sum = Mer[3]
    filepath = FileMerge.rebuildFile()[2]
    print(filepath)
    # 判断生成的文件名是否和要求一致，判断生成的文件大小和合并前的总文件大小是否一致
    if fileName == fileRealName and sum == totleSize:
        FileFunction.removeAllFile(filepath)



def main():
        # if len(os.listdir(fileFullPath3)) == 0:
        #     return
        # else:
        FileMerge.ChoiseRes()
        con()

