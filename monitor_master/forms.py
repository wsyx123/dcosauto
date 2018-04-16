#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月11日

@author: yangxu
'''
from elasticsearch import es_api
import datetime
from filter import threshold_filter
from models import SystemConfig
from common.get_es_connect_info import get_es_connect_info

    

class MonitorForms(object):
    def __init__(self,data,address):
        self.data = data
        self.host = self.data.get('host',address)
        es_api_info = get_es_connect_info('localhost', 9000, '/master/api/configs/ES%20API/')
        self.docops = es_api.DocumentApi(str(es_api_info[0]),int(es_api_info[1]))
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dispatch()
        
    
    def dispatch(self):
        for key,value in self.data.items():
            if key == 'cpu':
                self.cpu(value)
            elif key == 'memory':
                self.memory(value)
            elif key == 'disk':
                self.disk(value)
            elif key == 'network':
                self.network(value)
                
        
    def cpu(self,data):
        doc_body = {'host' : str(self.host),
            'timestamp' : self.date,
            'usage' : data['usage'],
            'iowait' : data['iowait']}
        threshold_filter.ThresholdFilter(self.host).cpu(data['usage'],self.date)
        self.docops.create(index_name='dcos', doc_type='cpu', doc_id=None, doc_body=doc_body)
    
    def memory(self,data):
        doc_body = {'host' : str(self.host),
            'timestamp' : self.date,
            'total' : data['total'],
            'free' : data['free']}
        self.docops.create(index_name='dcos', doc_type='memory', doc_id=None, doc_body=doc_body)
    
    def disk(self,data):
        for key,value in data.items():
            doc_body = {'host' : str(self.host),
                'timestamp' : self.date,
                'partition' : key,
                'total' : value['total'],
                'used' : value['used']}
            self.docops.create(index_name='dcos', doc_type='disk', doc_id=None, doc_body=doc_body)
    
    def network(self,data):
        for key,value in data.items():
            doc_body = {'host' : str(self.host),
                'timestamp' : self.date,
                'device' : key,
                'transmit' : value['transmit_total'],
                'receive' : value['receive_total'],
                'drop' : value['drop_total']}
            self.docops.create(index_name='dcos', doc_type='network', doc_id=None, doc_body=doc_body)