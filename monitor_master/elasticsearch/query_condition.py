#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月10日

@author: yangxu
'''
import datetime

condition_data = {
    "query": {
        "bool": {
                 "must": [
                          { "term":  { "host": "keystone" }}, 
                          {"range" : {"timestamp" : {
                                    "gte": (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"), 
                                    "lte": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), }}},
                          ]
                 }
        
        }
    }       