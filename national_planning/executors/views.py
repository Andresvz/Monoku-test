from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import filters

from .serializers import ExecutorSerializer
from .models import Executor

class ExecutorViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, retrives and delete Executor
    """
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    filter_backends = (filters.DjangoFilterBackend,)

