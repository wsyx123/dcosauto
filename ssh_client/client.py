#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月26日

@author: yangxu
'''
import paramiko
from interactive import interactive_shell


def connect(request):
    sshclient=paramiko.SSHClient()
    sshclient.load_system_host_keys()
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshclient.connect('192.168.10.3',22,'root','password')
    chan=sshclient.invoke_shell()
    interactive_shell(chan,request)
    

#################################################################
# 
# while True:
#     data=chan.recv(512)
#     if not data:
#         break
#     print(data)


