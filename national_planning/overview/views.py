from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins

from .serializers import OverviewSerializer
from .models import Overview

class OverviewViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, retrives and delete Overview
    """
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer
    filter_fields = ('id', 'programs', 'subprojects', 'projects',
            'subprojects2','rec','sit',)
