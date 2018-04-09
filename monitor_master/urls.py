#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from django.conf.urls import url,include
from rest_framework import routers
from .views import HostViewSet,DetailViewSet,PolicyViewSet,ProblemViewSet,TemplateViewSet,ItemViewSet


router = routers.DefaultRouter()
router.register(r'hosts', HostViewSet)
router.register(r'details', DetailViewSet)
router.register(r'policys', PolicyViewSet)
router.register(r'problems', ProblemViewSet)
router.register(r'templates', TemplateViewSet)
router.register(r'Items', ItemViewSet)

urlpatterns = [
    url(r'/api/', include(router.urls)),
]
