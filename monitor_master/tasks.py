#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月23日

@author: yangxu
'''
from __future__ import absolute_import
from celery import shared_task

@shared_task
def test_celery(x, y):
    print x + y
    return x + y