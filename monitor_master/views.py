# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import MonitorHost,MonitorNotifyDetail,MonitorNotifyPolicy,MonitorProblem,MonitorTemplate,MonitorItem
from .serializers import HostSerializer,DetailSerializer,PolicySerializer,ProblemSerializer,TemplateSerializer,ItemSerializer

# Create your views here.

class HostViewSet(viewsets.ModelViewSet):
    queryset = MonitorHost.objects.all()
    serializer_class = HostSerializer

class DetailViewSet(viewsets.ModelViewSet):
    queryset = MonitorNotifyDetail.objects.all()
    serializer_class = DetailSerializer

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = MonitorNotifyPolicy.objects.all()
    serializer_class = PolicySerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = MonitorProblem.objects.all()
    serializer_class = ProblemSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = MonitorTemplate.objects.all()
    serializer_class = TemplateSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = MonitorItem.objects.all()
    serializer_class = ItemSerializer
    