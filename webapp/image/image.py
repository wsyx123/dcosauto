#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年3月27日

@author: yangxu
'''
from webapp.models import ImageRegistry
from django.shortcuts import render_to_response,HttpResponse
from webapp.common.dockerhubv2api import dockerhubv2
from webapp.forms.image import ImageForm
import urllib
import json

def image(request):
    if request.method == "POST":
        ImageForm(request.POST)
    try:
        images = get_images()
    except Exception as e:
        print e
        images = []
    if request.method == 'DELETE':
        address = urllib.unquote(request.body.split('=')[1])
        ImageRegistry.objects.get(address=address).delete()
        
    if request.method == 'UPDATE':
        address = urllib.unquote(request.body.split('=')[1])
        count = set_one_host_status(address)
        return HttpResponse(json.dumps({'count':count}))
    
    set_all_host_status()
    hosts = ImageRegistry.objects.all()    
    return render_to_response("image/image.html",{'hosts':hosts,'images':images})

def get_images():
    image_hosts = ImageRegistry.objects.all()
    imageinfolist = []
    for hostobj in image_hosts:
        if hostobj.status == 'up':
            host = str(hostobj.address.split(":")[0])
            port = str(hostobj.address.split(":")[1])
            dockerinstance = dockerhubv2(host,port)
            image_tag_list = dockerinstance.getImageTagList()
            for i in range(len(image_tag_list)):
                for repository,tag in image_tag_list[i].items():
                    one_image_info_dict = {'address':hostobj.address}
                    size_id_time_version = dockerinstance.countImageSizeAndId(repository,tag)
                    if size_id_time_version:
                        one_image_info_dict["imagename"] = repository+":"+tag
                        one_image_info_dict["imagesize"] = size_id_time_version["imagesize"]
                        one_image_info_dict["imageid"] = size_id_time_version["imageid"]
                        one_image_info_dict["imagetime"] = size_id_time_version["imagetime"]
                        one_image_info_dict["imagedockerversion"] = size_id_time_version["imagedockerversion"]
                        imageinfolist.append(one_image_info_dict)
    return imageinfolist

def set_one_host_status(address):        
    host = str(address.split(":")[0])
    port = str(address.split(":")[1])
    try:
        instancev2 = dockerhubv2(host,port)
        imagecount = instancev2.countImageAmount()
        imageobj = ImageRegistry.objects.get(address=address)
        imageobj.count = imagecount
        imageobj.status = 'up'
        imageobj.save()
        return imagecount
    except Exception as e:
        print e
        imageobj = ImageRegistry.objects.get(address=address)
        imageobj.count = 0
        imageobj.status = 'down'
        imageobj.save()
        return 0
    
def set_all_host_status():        
    rImages = ImageRegistry.objects.all()
    if rImages:
        for image in rImages:
            address = image.address
            host = str(address.split(":")[0])
            port = str(address.split(":")[1])
            try:
                instancev2 = dockerhubv2(host,port)
                imagecount = instancev2.countImageAmount()
                imageobj = ImageRegistry.objects.get(address=address)
                imageobj.count = imagecount
                imageobj.status = 'up'
                imageobj.save()
            except Exception as e:
                imageobj = ImageRegistry.objects.get(address=address)
                imageobj.count = 0
                imageobj.status = 'down'
                imageobj.save()
