# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import Executor


class ExecutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Executor
        fields = ('id', 'name', 'year', 'code', 'sector','overview',)


