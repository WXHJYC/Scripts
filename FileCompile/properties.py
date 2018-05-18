#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @Time    : 2018/5/18
    @Author  : LiuXueWen
    @Site    : 
    @File    : properties.py
    @Software: PyCharm
    @Description: 定时合并文件配置文件
'''
# 上传服务器地址
host = "10.25.245.123"
# 上传服务器端口
port = 21
# 服务器登录用户名
username = "ftpuser"
# 服务器登录密码
passwd = "ftpuser"
# 需要上传的文件的本地路径
local_path = "/root/LXW/dat/"
# 需要上传的文件的远程地址路径
remote_path = "/home/ftpuser/dat"
# 需要删除的远程日志路径
ftp_log_path = "/home/ftpuser/log/log.txt"
# 需要上传的本地日志路径
local_log_path = "/root/LXW/log/log.txt"
# 需要上传的远程日志路径
remote_log_path = "/home/ftpuser/log/log.txt"
# 设置需要合并的本地文件路径
fileFullPath3 = "/root/LXW/new/"
# 设置本地文件合并后的输出路径
fileFullPath2 = "/root/LXW/dat/"
# 需要删除的已经完成合并的本地文件夹下所有文件的路径
has_merge_path = fileFullPath2
# 需要循环执行的周期时间段
delay_time = 2
