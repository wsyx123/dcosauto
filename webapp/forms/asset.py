#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月24日

@author: yangxu
'''
'''
DriverStatus : [
    [u'Pool Name', u'docker-8:2-407767-pool'], 
    [u'Pool Blocksize', u'65.54kB'], 
    [u'Base Device Size', u'10.74GB'], 
    [u'Backing Filesystem', u'xfs'], 
    [u'Udev Sync Supported', u'true'], 
    [u'Data file', u'/dev/loop0'], 
    [u'Metadata file', u'/dev/loop1'], 
    [u'Data loop file', u'/data/docker/devicemapper/devicemapper/data'], 
    [u'Metadata loop file', u'/data/docker/devicemapper/devicemapper/metadata'], 
    [u'Data Space Used', u'11.8MB'], 
    [u'Data Space Total', u'107.4GB'], 
    [u'Data Space Available', u'11.41GB'], 
    [u'Metadata Space Used', u'581.6kB'], 
    [u'Metadata Space Total', u'2.147GB'], 
    [u'Metadata Space Available', u'2.147GB'], 
    [u'Thin Pool Minimum Free Space', u'10.74GB'], 
    [u'Deferred Removal Enabled', u'true'], 
    [u'Deferred Deletion Enabled', u'true'], 
    [u'Deferred Deleted Device Count', u'0'], 
    [u'Library Version', u'1.02.140-RHEL7 (2017-05-03)']]
'''

import json
class AssetForm(object):
    def __init__(self,data,modelname,address):
        self.data = json.loads(data)
        self.modelname = modelname
        self.data_key = ['Name','OperatingSystem','NCPU','MemTotal','DriverStatus',
                          'ServerVersion','Driver','DockerRootDir']
        self.hostname = self.data['Name']
        self.address = address
        self.sversion = self.data['OperatingSystem']
        self.dversion = self.data['ServerVersion']
        self.ddriver = self.data['Driver']
        self.ddata = self.data['DockerRootDir']
        self.cpu = str(self.data['NCPU'])
        self.mem = str(self.data['MemTotal']/1000/1000/1000)+'GB'
        self.disk = self.get_disk_value()
        self.save()
        
    def get_disk_value(self):
        disk_value_list = self.data['DriverStatus']
        for item in disk_value_list:
            if 'Data Space Available' in item:
                return item[1]
        return None    
            
    def save(self):
        self.modelname.objects.create(hostname=self.hostname,address=self.address,
                                      sversion=self.sversion,cpu=self.cpu,
                                      mem=self.mem,disk=self.disk,
                                      dversion=self.dversion,ddriver=self.ddriver,
                                      ddata=self.ddata,status='up')