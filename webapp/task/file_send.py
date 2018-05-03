#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月30日

@author: yangxu
'''
from django.shortcuts import render_to_response,HttpResponse
import os,sys
import json
root_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

def file_send(request):
    if request.method == 'POST':
#         print request.POST.get('remote_path')
#         print request.FILES['file-fr[]']
        handle_uploaded_file(request.FILES['file-fr[]'])
        return HttpResponse(json.dumps({'status':'success'}))
    return render_to_response('task/file.html', {})

def handle_uploaded_file(f):
    destination = open(root_dir+'/statics/upload/'+f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()