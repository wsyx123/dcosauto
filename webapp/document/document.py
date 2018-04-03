#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月23日

@author: yangxu
'''
from django.shortcuts import render_to_response
from django.http import FileResponse

def document(request):
    return render_to_response("document/document.html",)

def documentdownload(request):
    filename = 'C:\\Users\\yangxu\\Desktop\\project\\dcosauto\\webapp\\download\\test.txt'
    files=open(filename,'r')
    response =FileResponse(files)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="test.txt"'  
    return response  