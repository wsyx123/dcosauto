# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets,filters
from .models import MonitorHost,MonitorNotifyDetail,MonitorNotifyPolicy,\
MonitorProblem,MonitorTemplate,MonitorItem,SystemConfig,MonitorNotifyConfig
from .serializers import HostSerializer,DetailSerializer,PolicySerializer,\
ProblemSerializer,TemplateSerializer,ItemSerializer,ConfigSerializer,NotifyConfigSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from forms import MonitorForms

# Create your views here.

class HostViewSet(viewsets.ModelViewSet):
    queryset = MonitorHost.objects.all()
    serializer_class = HostSerializer
    lookup_field = 'name'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','id')

class DetailViewSet(viewsets.ModelViewSet):
    queryset = MonitorNotifyDetail.objects.all()
    serializer_class = DetailSerializer

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = MonitorNotifyPolicy.objects.all()
    serializer_class = PolicySerializer
    
class NotifyConfigViewSet(viewsets.ModelViewSet):
    queryset = MonitorNotifyConfig.objects.all()
    serializer_class = NotifyConfigSerializer
    lookup_field = 'name'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','type')
    
class ProblemViewSet(viewsets.ModelViewSet):
    queryset = MonitorProblem.objects.all()
    serializer_class = ProblemSerializer
    lookup_field = 'id'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id','status','level')

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = MonitorTemplate.objects.all()
    serializer_class = TemplateSerializer
    lookup_field = 'name'

class ItemViewSet(viewsets.ModelViewSet):
    queryset = MonitorItem.objects.all()
    serializer_class = ItemSerializer

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = SystemConfig.objects.all()
    serializer_class = ConfigSerializer
    lookup_field = 'name'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    
class MonitorHandler(APIView):
    def post(self,request):
        MonitorForms(request.data,request.META['REMOTE_ADDR'])
        return Response('ok')