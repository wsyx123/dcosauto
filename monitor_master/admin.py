# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import MonitorTemplate,MonitorHost,MonitorNotifyDetail,\
MonitorProblem,MonitorNotifyPolicy,MonitorItem,SystemConfig

    

    
class MonitorTemplateAdmin(admin.ModelAdmin):
    list_display = ('name','get_items','get_policy','interval')

    
class MonitorHostAdmin(admin.ModelAdmin):
    list_display = ('name','address','port','template','status','monitor_agent')  
    
class MonitorNotifyPolicyAdmin(admin.ModelAdmin):
    list_display = ('name','warning_threshold','danger_threshold','promote')
    
class MonitorProblemAdmin(admin.ModelAdmin):
    list_display = ('name','type','time','host','level','status')
    
class MonitorNotifyDetailAdmin(admin.ModelAdmin):
    list_display = ('mode','theme','content','send_to','status')
    
class MonitorItemAdmin(admin.ModelAdmin):
    list_display = ('name','value')

class SystemConfigAdmin(admin.ModelAdmin):
    list_display = ('name','value')

admin.site.register(MonitorTemplate,MonitorTemplateAdmin)
admin.site.register(MonitorHost,MonitorHostAdmin)
admin.site.register(MonitorNotifyPolicy,MonitorNotifyPolicyAdmin)
admin.site.register(MonitorProblem,MonitorProblemAdmin)
admin.site.register(MonitorNotifyDetail,MonitorNotifyDetailAdmin)
admin.site.register(MonitorItem,MonitorItemAdmin)
admin.site.register(SystemConfig,SystemConfigAdmin)