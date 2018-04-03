"""devops_ci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from platformcenter.component import component,component_delete
from platformcenter.template import template
from platformcenter.install import auto_install, custom_install
from platformcenter.log import log
from dashboard.dashboard import dashboard
from system.system import system
from monitor.monitor import monitor_configure,add_host,del_host,\
monitor_graph,monitor_notify,add_template,del_template
from document.document import document,documentdownload
from asset.asset import asset
from image.image import image
admin.autodiscover()

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$',dashboard),
    url(r'^dashboard/$',dashboard,name='dashboard'),
    url(r'^system/$',system),
    url(r'^asset/$',asset),
    url(r'^image/$',image),
    url(r'^platform/manage/$',component),
    url(r'^platform/manage/delete/$',component_delete),
    url(r'^platform/template/$',template),
    url(r'^platform/autoinstall/$',auto_install),
    url(r'^platform/custominstall/$',custom_install),
    url(r'^platform/log/$',log),
    url(r'^document/$',document),
    url(r'^document/download/$',documentdownload),
    url(r'^monitor/configure/$',monitor_configure),
    url(r'^monitor/configure/addHost/$',add_host),
    url(r'^monitor/configure/delHost/$',del_host),
    url(r'^monitor/configure/addTemplate/$',add_template),
    url(r'^monitor/configure/delTemplate/$',del_template),
    url(r'^monitor/notify/$',monitor_notify),
    url(r'^monitor/graph/$',monitor_graph),
]
