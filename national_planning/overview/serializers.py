# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import Overview


class OverviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Overview
        fields = ('id', 'programs', 'subprojects', 'projects',
            'subprojects2','rec','sit',)
