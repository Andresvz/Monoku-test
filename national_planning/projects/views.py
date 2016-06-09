from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins

from .serializers import ProjectSerializer
from .models import Project

class ProjectViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, retrives and delete Project
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_fields = ('id', 'name', 'advance', 'residue', 'liabilities',
            'obligation','payments','source',)

