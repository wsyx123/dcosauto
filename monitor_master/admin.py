# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import MonitorTemplate,MonitorHost,MonitorNotifyDetail,\
MonitorProblem,MonitorNotifyPolicy,MonitorItem

    

    
class MonitorTemplateAdmin(admin.ModelAdmin):
    list_display = ('name','get_items','get_policy','interval')
    def get_policy(self, MonitorNotifyPolicy):
        return "\n".join([p.name for p in MonitorNotifyPolicy.objects.all()]) 
    def get_items(self, MonitorItem):
        return "\n".join([p.name for p in MonitorItem.objects.all()]) 
    
class MonitorHostAdmin(admin.ModelAdmin):
    list_display = ('name','address','port','template','status','agent')  
    
class MonitorNotifyPolicyAdmin(admin.ModelAdmin):
    list_display = ('name','warning_threshold','danger_threshold','promote')
    
class MonitorProblemAdmin(admin.ModelAdmin):
    list_display = ('name','time','address','level','status')
    
class MonitorNotifyDetailAdmin(admin.ModelAdmin):
    list_display = ('mode','theme','content','send_to','status')
    
class MonitorItemAdmin(admin.ModelAdmin):
    list_display = ('name','value')

admin.site.register(MonitorTemplate,MonitorTemplateAdmin)
admin.site.register(MonitorHost,MonitorHostAdmin)
admin.site.register(MonitorNotifyPolicy,MonitorNotifyPolicyAdmin)
admin.site.register(MonitorProblem,MonitorProblemAdmin)
admin.site.register(MonitorNotifyDetail,MonitorNotifyDetailAdmin)
admin.site.register(MonitorItem,MonitorItemAdmin)