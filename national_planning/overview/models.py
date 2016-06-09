from django.db import models
from common.models import TimeStampedModel, SoftDeleteManager


class Overview(TimeStampedModel):
    """
    informacion general de planeacion
    """
    programs = models.CharField(max_length=255)
    subprojects = models.CharField(max_length=255)
    projects = models.CharField(max_length=255)
    subprojects2 = models.CharField(max_length=255)
    rec = models.CharField(max_length=255)
    sit = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Informacion General'
        verbose_name_plural = 'Informacion General'

    def __str__(self):
        return '%s' % (self.programs)
