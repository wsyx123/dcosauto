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
from django.views.generic import RedirectView
from django.contrib import admin
from platformcenter.component import component,component_delete,component_status
from platformcenter.template import template,edit_template,del_platform_template
from platformcenter.install import auto_install, custom_install
from platformcenter.log import log
from dashboard.dashboard import dashboard
from system.system import system
from monitor.monitor import *
from document.document import document,documentdownload
from asset.asset import asset,asset_connect,asset_detail,asset_system_user,asset_system_user_detail,\
organization,organization_department_detail
from image.image import image
from task.cmd import cmd
from task.file_send import file_send
from task.cron_task import cron_task,cron_task_detail,cron_task_record
admin.autodiscover()

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$',dashboard),
    url(r'^dashboard/$',dashboard,name='dashboard'),
    url(r'^system/$',system),
    url(r'^asset/$',RedirectView.as_view(url='/asset/host/')),
    url(r'^asset/host/$',asset),
    url(r'^asset/host/detail/(?P<host>.+)$',asset_detail,name='asset_detail'),
    url(r'^asset/host/(?P<addr>.+)$',asset_connect),
    url(r'^asset/user/$',asset_system_user),
    url(r'^asset/user/detail/(?P<user>.+)$',asset_system_user_detail,name='user_detail'),
    url(r'^asset/organization/$',organization),
    url(r'^asset/organization/detail/(?P<deid>.+)$',organization_department_detail,name='organization_department_detail'),
    url(r'^task/cmd/$',cmd),
    url(r'^task/file/$',file_send),
    url(r'^task/cron/$',cron_task),
    url(r'^task/cron/detail/(?P<pk>.+)$',cron_task_detail,name='task_detail'),
    url(r'^task/cron/record/(?P<pk>.+)$',cron_task_record,name='task_record'),
    url(r'^image/$',image),
    url(r'^platform/manage/$',component),
    url(r'^platform/manage/delete/$',component_delete),
    url(r'^platform/manage/status/$',component_status),
    url(r'^platform/template/$',template),
    url(r'^platform/template/editTemplate/(?P<name>.+)$',edit_template),
    url(r'^platform/template/delTemplate/$',del_platform_template),
    url(r'^platform/autoinstall/$',auto_install),
    url(r'^platform/custominstall/$',custom_install),
    url(r'^platform/log/$',log),
    url(r'^document/$',document),
    url(r'^document/download/$',documentdownload),
    url(r'^monitor/configure/$',monitor_configure),
    url(r'^monitor/configure/addHost/$',add_host),
    url(r'^monitor/configure/delHost/$',del_host),
    url(r'^monitor/configure/editHost/(?P<name>.+)$',edit_host),
    url(r'^monitor/configure/addTemplate/$',add_template),
    url(r'^monitor/configure/delTemplate/$',del_template),
    url(r'^monitor/configure/editTemplate/(?P<name>.+)$',edit_tempate),
    url(r'^monitor/configure/addItem/$',add_item),
    url(r'^monitor/configure/delItem/$',del_item),
    url(r'^monitor/configure/editItem/(?P<name>.+)$',edit_item),
    url(r'^monitor/configure/addPolicy/$',add_policy),
    url(r'^monitor/configure/delPolicy/$',del_policy),
    url(r'^monitor/configure/editPolicy/(?P<name>.+)$',edit_policy),
    url(r'^monitor/notify/$',monitor_notify),
    url(r'^monitor/notify/addNotify/$',add_notify),
    url(r'^monitor/graph/$',monitor_graph),
]
