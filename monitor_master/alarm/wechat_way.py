#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月12日

@author: yangxu
'''

import itchat, time
def lc():
    print("Finash Login!")
def ec():
    print("exit")

itchat.auto_login(loginCallback=lc, exitCallback=ec)
