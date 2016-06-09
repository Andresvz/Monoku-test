from django.db import models
from common.models import TimeStampedModel, SoftDeleteManager
from overview.models import Overview

class Executor(TimeStampedModel):
    """
    informacion de la entidad ejecutora
    """
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    overview = models.OneToOneField(Overview)

    class Meta:
        verbose_name = 'Unidad Ejecutora'
        verbose_name_plural = 'Unidades Ejecutoras'

    def __str__(self):
        return '%s' % (self.name)

