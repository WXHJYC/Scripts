#! /usr/bin/env python
#coding=utf-8
'''
    @Time    : 2018/5/17
    @Author  : LiuXueWen
    @Site    :
    @File    : Timer.py
    @Software: PyCharm
    @Description: 定时装置。用于控制脚本定时执行。设置每次扫描时间10分钟。
'''


import time
import os
import sys
def path_real():
    pwd = os.getcwd()
    # 当前文件的父路径
    father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    sys.path.append(father_path)

import FileOperating.FileFunction as FileFunction
import Ftp.FtpUpload as FtpUpload
import properties as properties
import FileOperating.MergeFor as MergeFor

def __init__():
    path_real()


# 总调度任务
def task_reload():
    # 调用合并模块执行合并文件功能
    for i in range(0,len(os.listdir(fileFullPath3))):
        MergeFor.main()

def ftp_upload():
    # 调用ftp上传功能，上传合并后的文件
    # 启动程序
    # 目标ftp地址
    my_ftp = FtpUpload.MyFTP(host, port)
    # ftp用户名和密码
    my_ftp.login(username, passwd)
    # 上传指定目录下所有文件到指定文件夹下
    my_ftp.upload_All_file(local_path, remote_path)
    # 删除ftp上的log日志文件
    my_ftp.remove_log(ftp_log_path)
    # 上传最新的日志文件
    my_ftp.upload_file(local_log_path, remote_log_path)

    my_ftp.close()


# 循环计划
def perform_command(delay_time):
    task_reload()
    ftp_upload()
    while True:
        if os.path.getsize(fileFullPath3) == 0:
            break
        else:
            time.sleep(delay_time)
            task_reload()
            ftp_upload()
            # 删除本地的dat文件
            FileFunction.removeFiles(local_path)


if __name__ == '__main__':
    fileFullPath3 = properties.fileFullPath3
    # 上传服务器地址
    host = properties.host
    # 上传服务器端口
    port = properties.port
    # 服务器登录用户名
    username = properties.username
    # 服务器登录密码
    passwd = properties.passwd
    # 需要上传的文件的本地路径
    local_path = properties.local_path
    # 需要上传的文件的远程地址路径
    remote_path = properties.remote_path
    # 需要删除的远程日志路径
    ftp_log_path = properties.ftp_log_path
    # 需要上传的本地日志路径
    local_log_path = properties.local_log_path
    # 需要上传的远程日志路径
    remote_log_path = properties.remote_log_path
    # 需要删除的已经完成合并的本地文件夹下所有文件的路径
    has_merge_path = properties.has_merge_path
    # 需要循环执行的周期时间段
    delay_time = properties.delay_time
    # 设置每过10分钟执行一次
    perform_command(delay_time)






