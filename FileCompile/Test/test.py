#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
    @Time    : 2018/5/17
    @Author  : LiuXueWen
    @Site    :
    @File    : test.py
    @Software: PyCharm
    @Description: 测试使用
'''
# import time
#
# # todaytrim = time.time()
# # current_milli_time = int(round(time.time() * 1000))
# # print(type(current_milli_time))
#
# # for i in range(0,9):
# #     filepathname = "C:\Users\Carol\Desktop\\new\i_cpzx_clientuseperiod_20180516_00_."+str(i)
# #     file = open(filepathname,"wb")
# #     filepathname = file.write("test"+str(i))
#
# import os
# import time
#
#
# # 读取文件整体大小
# def getFileSize(file):
#     file.seek(0, os.SEEK_END)
#
#     fileLength = file.tell()
#
#     file.seek(0, 0)
#     print("文件总长度：" + str(fileLength))
#     # 返回文件总长度
#     return fileLength
#
#
# def rebuildFile():
#     '''
#         @files: fileFullPath3 下的所有文件和文件夹名称
#         @file2: files集合下遍历的每一个名称
#         @file3:
#         @file4: 当file2 是文件夹的情况下，遍历该文件夹下的所有文件
#         @fileFullPath: 遍历所有情况下得到的实际目标路径地址（\new\'realpath'）
#         @fileFullPath3: 设置需要合并的源目标路径
#         @fileFullPath2: 设置合并后的目标路径
#     '''
#     # 设置需要合并的文件路径
#     # 手动输入目标地址路径
#     # fileFullPath = r"%s" % raw_input("File base path: ").strip("\"")
#     # 指定读取输入和输出目标路径地址
#     fileFullPath3 = "/root/new2/"
#     fileFullPath2 = "/root/dat/"
#     # fileFullPath3 = "C:\Users\Carol\Desktop\\new2"
#     # fileFullPath2 = "C:\Users\Carol\Desktop\\dat"
#
#     # 当前时间节点的时间戳
#     todaytrim = time.time()
#     # 生成13位毫秒级的时间戳
#     current_milli_time = int(round(time.time() * 1000))
#
#     # 获取当前日期并格式化
#     todaydate = time.strftime("%Y%m%d", time.localtime())
#     # print len(os.listdir(fileFullPath3))
#     # 判断指定的\new文件夹下是否为空，为空则不处理
#     if len(os.listdir(fileFullPath3)) == 0:
#         print "null dirs"
#     else:
#         # 若文件夹不为空则执行以下操作
#         # 得到文件夹下的所有文件或文件夹的名称
#         files = os.listdir(fileFullPath3)
#         for file2 in files:  # 遍历文件夹
#             # 如果是文件夹则加上该地址成为实际路径
#             # 获取实际需要读取的目标路径
#             fileFullPath = fileFullPath3 + file2
#             # print "fileFullPath:" + fileFullPath
#             # 判断是否为文件夹，若为文件夹则执行下一步，否则跳过
#             if os.path.isdir(fileFullPath):
#                 # 循环读取所有文件夹下的文件
#                 print("fileFullPath----"+fileFullPath)
#                 for file4 in os.listdir(fileFullPath):
#                     print("file4----"+file4)
#                     # 获取文件的数量
#                     divideTotalPartsCount = len(os.listdir(fileFullPath))
#                     print(divideTotalPartsCount)
#                     # 设置读取的文件名称格式为utf-8
#                     # file = file.decode('utf-8')
#                     # 判断文件名是否符合要求，文件名一致的则执行合并功能
#                     # 以_下划线拆分成不同的字段，匹配字段值是否一致，根据匹配的字段值进行下一步操作
#                     filelist = file4.split("_")
#                     print "文件名称：" + str(file4)
#                     print("filelist:"+str(filelist))
#
# rebuildFile()
# import os
# import time
#
# # 设置需要合并的文件路径
# # 手动输入目标地址路径
# # fileFullPath = r"%s" % raw_input("File base path: ").strip("\"")
# # 指定读取输入和输出目标路径地址
# fileFullPath3 = "/root/LXW/new/"
# fileFullPath2 = "/root/LXW/dat/"
# # fileFullPath3 = "C:\Users\Carol\Desktop\\new2"
# # fileFullPath2 = "C:\Users\Carol\Desktop\\dat"
# # print len(os.listdir(fileFullPath3))
# # 当前时间节点的时间戳
# todaytrim = time.time()
# # 生成13位毫秒级的时间戳
# current_milli_time = int(round(time.time() * 1000))
#
# # 获取当前日期并格式化
# # todaydate = time.strftime("%Y%m%d", time.localtime())
# todaydate = "20180516"
#
# # 读取文件整体大小
# def getFileSize(file):
#     file.seek(0, os.SEEK_END)
#
#     fileLength = file.tell()
#
#     file.seek(0, 0)
#     print("文件总长度：" + str(fileLength))
#     # 返回文件总长度
#     return fileLength
#
#
# def rebuildFile():
#     '''
#         @files: fileFullPath3 下的所有文件和文件夹名称
#         @file2: files集合下遍历的每一个名称
#         @file3:
#         @file4: 当file2 是文件夹的情况下，遍历该文件夹下的所有文件
#         @fileFullPath: 遍历所有情况下得到的实际目标路径地址（\new\'realpath'）
#         @fileFullPath3: 设置需要合并的源目标路径
#         @fileFullPath2: 设置合并后的目标路径
#     '''
#     # 判断指定的\new文件夹下是否为空，为空则不处理
#     if len(os.listdir(fileFullPath3)) == 0:
#         print "null dirs"
#     else:
#         # 若文件夹不为空则执行以下操作
#         # 得到文件夹下的所有文件或文件夹的名称
#         files = os.listdir(fileFullPath3)
#         # print(files)
#         for file2 in files:  # 遍历文件夹
#             # 如果是文件夹则加上该地址成为实际路径
#             # 获取实际需要读取的目标路径
#             fileFullPath = fileFullPath3 + file2
#             # print "fileFullPath:" + fileFullPath
#             # 判断是否为文件夹，若为文件夹则执行下一步，否则跳过
#             if os.path.isdir(fileFullPath):
#                 # 循环读取所有文件夹下的文件
#                 print("fileFullPath----"+fileFullPath)
#                 #  获取文件的数量
#                 divideTotalPartsCount = len(os.listdir(fileFullPath))
#                 for file4 in os.listdir(fileFullPath):
#                     print("file4----"+file4)
#                     # 设置读取的文件名称格式为utf-8
#                     # file = file.decode('utf-8')
#                     # 判断文件名是否符合要求，文件名一致的则执行合并功能
#                     # 以_下划线拆分成不同的字段，匹配字段值是否一致，根据匹配的字段值进行下一步操作
#                     filelist = file4.split("_")
#                 # 将文件列表、文件数量、实际路径地址返回到外部
#                 return filelist,divideTotalPartsCount,fileFullPath
#
# def ChoiseRes():
#     res = rebuildFile()
#     filelist = res[0]
#     divideTotalPartsCount = res[1]
#     # 循环判断当前文件夹下所有的文件，判断结束  所有的文件后退出循环
#     # 根据指定的格式判断是否为同一个类型的文件，若为一致则执行合并操作，否则返回false
#     for i in range(0, divideTotalPartsCount):
#         # 系统中心
#         if (filelist[0] == "i" or filelist[0] == "a") and filelist[1] == "xtzx" and filelist[
#             3] == todaydate:
#             MergeFile()
#             print("xtzx Merge successed !")
#         # 渠道中心
#         elif (filelist[0] == "i" or filelist[0] == "a") and filelist[1] == "qdzx" and filelist[
#             3] == todaydate:
#             MergeFile()
#             print("qdzx Merge successed !")
#         # 产品中心
#         elif (filelist[0] == "i" or filelist[0] == "a") and filelist[1] == "cpzx" and filelist[
#             3] == todaydate:
#             MergeFile()
#             print("cpzx Merge successed !")
#         # 企业发展部
#         elif (filelist[0] == "i" or filelist[0] == "a") and filelist[1] == "qyfz" and filelist[
#             3] == todaydate:
#             MergeFile()
#             print("qyfz Merge successed !")
#         # 内容中心
#         elif (filelist[0] == "i" or filelist[0] == "a") and filelist[1] == "nrzx" and filelist[
#             3] == todaydate:
#             MergeFile()
#             print("nrzx Merge successed !")
#         # 运营中心
#         elif (filelist[0] == "i" or filelist[0] == "a") and filelist[1] == "yyzx" and filelist[
#             3] == todaydate:
#             MergeFile()
#             print("yyzx Merge successed !")
#         # 若全部不满足则执行下面的语句
#         else:
#             print "没有满足条件的文件"
#             return False
#
# # 合并功能操作代码
# def MergeFile():
#
#     res = rebuildFile()
#     filelist = res[0]
#     divideTotalPartsCount = res[1]
#     fileFullPath = res[2]
#
#     fileNewName = filelist[0] + "_" + filelist[1] + "_" + filelist[2] + "_" + todaydate + "_" + filelist[4] + "_" + str(current_milli_time) + ".dat"
#
#     # 读取文件操作
#     file = open(fileFullPath2 + fileNewName, "wb")
#
#     for i in range(0,divideTotalPartsCount):
#
#         # 控制合并文件的后缀名
#         filePartName = filelist[0] + "_" + filelist[1] + "_" + filelist[2] + "_" + todaydate + "_" + filelist[4] + "_." + str(i)
#
#         # 注意：linux系统下拼接该路径不需要加/，在Windows下需要加上\\
#         filePart = open(fileFullPath + "/" + filePartName, "rb")
#
#         filePartSize = getFileSize(filePart)
#
#         lengthWritten = 0
#
#         # 循环读取规定格式的.dat文件并执行写入操作
#         while lengthWritten < filePartSize:
#             # 每次读取1k
#             bufLen = 1024
#             buf = filePart.read(bufLen)
#             file.write(buf)
#             lengthWritten += len(buf)
#
#         # 判断文件是否存在，如果不存在则执行判断文件名的操作，否则继续合并
#         if os.path.exists(fileFullPath + filePartName):
#             continue
#
#         filePart.close()
#
#         # fileFunction.removeFile(fileFullPath)
#
#         # file.close()
import os
import sys
#当前文件的路径
import properties
print properties.delay_time