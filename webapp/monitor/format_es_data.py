#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月15日

@author: yangxu
'''
from monitor_master.elasticsearch.es_api import DocumentApi
import json
from common.get_es_connect_info import get_es_connect_info

class FormatData(object):
    def __init__(self,query_data):
        self.return_data = {'cpu':{'timestamp':[],'usage':[],'iowait':[]},
                       'memory':{'timestamp':[],'free':[],'total':[]},
                       'disk':{'partition':[],'used':[],'total':[]},
                       'network':{'device':"",'timestamp':[],'transmit':[],'receive':[],'drop':[]}
                       }
        es_api_info = get_es_connect_info('192.168.10.1', 9000, '/master/api/config/ES%20API/')
        self.doc_api_obj = DocumentApi(str(es_api_info[0]),int(es_api_info[1]))
        self.query_data = query_data
    
    def cpu(self):
        monitor_data = self.doc_api_obj.search('dcos', 'cpu', self.query_data['host'], int(self.query_data['time_value']))
        for one in (json.loads(monitor_data['result']))['hits']['hits']:
            self.return_data['cpu']['timestamp'].append(one['_source']['timestamp'].split()[1][0:5])
            self.return_data['cpu']['usage'].append(one['_source']['usage']*100)
            self.return_data['cpu']['iowait'].append(one['_source']['iowait']*100)
            
    def memory(self):
        monitor_data = self.doc_api_obj.search('dcos', 'memory', self.query_data['host'], int(self.query_data['time_value']))
        for one in (json.loads(monitor_data['result']))['hits']['hits']:
            self.return_data['memory']['timestamp'].append(one['_source']['timestamp'].split()[1][0:5])
            self.return_data['memory']['free'].append(one['_source']['free'])
            self.return_data['memory']['total'].append(one['_source']['total'])
        
    def disk(self):
        partition_temp_list = []
        free_temp_dict = {}
        total_temp_dict = {}
        monitor_data = self.doc_api_obj.search('dcos', 'disk', self.query_data['host'], int(self.query_data['time_value']))
        monitor_data_list = (json.loads(monitor_data['result']))['hits']['hits']
        for one in monitor_data_list:
            partition_temp_list.append(one['_source']['partition'])
        partition_temp_list = list(set(partition_temp_list))
        
        for partition in partition_temp_list:
            for one in monitor_data_list:
                if one['_source']['partition'] == partition:
                    free_temp_dict[partition] = one['_source']['used']
                    total_temp_dict[partition] = one['_source']['total']
        
        for partition in partition_temp_list:
            self.return_data['disk']['partition'].append(partition)
            self.return_data['disk']['used'].append(free_temp_dict[partition])
            self.return_data['disk']['total'].append(total_temp_dict[partition])
            
    def network(self):
        monitor_data = self.doc_api_obj.search('dcos', 'network', self.query_data['host'], int(self.query_data['time_value']))
        for one in (json.loads(monitor_data['result']))['hits']['hits']:
            self.return_data['network']['device'] = one['_source']['device']
            self.return_data['network']['timestamp'].append(one['_source']['timestamp'].split()[1][0:5])
            self.return_data['network']['transmit'].append(one['_source']['transmit'])
            self.return_data['network']['receive'].append(one['_source']['receive'])
            self.return_data['network']['drop'].append(one['_source']['drop'])
        
    
    def dispatch(self):
        if self.query_data['graph_item'] == 'all':
            self.cpu()
            self.disk()
            self.memory()
            self.network()
        else:
            getattr(self, self.query_data['graph_item'])()
        return self.return_data