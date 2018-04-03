#!/usr/bin/env python
#coding:utf-8
import commands
import re
import redis
import platform
import socket
import fcntl  
import struct  
import os
import math
  
def getIp(ifname):  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    return socket.inet_ntoa(fcntl.ioctl(  
        s.fileno(),  
        0x8915,  
        struct.pack('256s', ifname[:15])  
    )[20:24])  
  


class RedisOps():
    def __init__(self,hostname,port):
        self.conn=redis.Redis(host=hostname,port=port)
        
    def hmset(self,name,keys):
        result=self.conn.hmset(name,keys)
        return result

def cpuCount():
    status,output=commands.getstatusoutput('sar 5 1|sed -n 1p')
    cpucount=output.split()[-2] 
    return cpucount.strip('(')

def cpuUsage():
    status,output=commands.getstatusoutput('sar 5 1|grep Average')
    cpuidle=output.split()[-1]
    cpuusage=100.00 - float(cpuidle)
    return cpuCount()+'核'+'/'+str(round(cpuusage,1))+'%'

def getHostname():
    hostname = platform.node()
    #hostname=socket.gethostname()
    return hostname

def getOs():
    version=platform.dist()
    return  version[0]+':'+version[1]

def getMem():
    mem={}
    with open('/proc/meminfo') as f:
	for line in f:
	    key=line.split(':')[0]
            value=line.split(':')[1].split()[0]
            mem[key]=float(value)
    mem['MemUsed']=mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    return str(round(mem['MemTotal']/1024/1024)) +'G'+'/'+ str(round(mem['MemUsed']/mem['MemTotal']*100,1))+'%'

def getDisk():
    disk=os.statvfs('/')
    diskUsed=(disk.f_blocks - disk.f_bfree) * disk.f_bsize
    diskTotal=disk.f_blocks * disk.f_bsize
    diskUsage=float(diskUsed)/float(diskTotal) * 100
    return str(diskTotal/1024/1024/1024+1)+'G'+'/'+str(round(diskUsage,1))+'%'

	    


if __name__== '__main__':
    info_dict={}
    hostname=getHostname()
    system=getOs()
    ip=getIp('eth0')
    cpu=cpuUsage()
    mem=getMem()
    disk=getDisk()
    info_dict={
               'hostname':hostname,
  	           'os':system,
	           'ip':ip,
               'cpu':cpu,
               'mem':mem,
               'disk':disk}
    redis_c=RedisOps('10.200.203.3',6379)
    redis_c.hmset(ip,info_dict)
