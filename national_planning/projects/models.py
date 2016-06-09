from django.db import models
from common.models import TimeStampedModel, SoftDeleteManager
from executors.models import Executor

class Project(TimeStampedModel):
    """
    informacion del proyecto
    """
    name = models.CharField(max_length=255)
    advance = models.CharField(max_length=255)
    residue = models.CharField(max_length=255)
    liabilities = models.CharField(max_length=255)
    obligation = models.CharField(max_length=255)
    payments = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    executor = models.OneToOneField(Executor)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return '%s' % (self.name)
