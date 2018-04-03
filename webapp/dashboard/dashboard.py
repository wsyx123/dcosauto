#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月23日

@author: yangxu
'''
from webapp.models import platformcluster,platformcomponent,platformtemplate,platformhosts
from django.shortcuts import render_to_response
# Create your views here.
def dashboard(request):
    clusters = platformcluster.objects.all().count()
    hosts = platformhosts.objects.all().count()
    components = platformcomponent.objects.all().count()
    templates = platformtemplate.objects.all().count()
    return render_to_response("dashboard/dashboard.html",{'clusters':clusters,
                                                          'hosts':hosts,
                                                          'components':components,
                                                          'templates':templates})