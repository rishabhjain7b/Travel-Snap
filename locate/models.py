

from django.db import models
from geoposition.fields import GeopositionField

class Zone(models.Model):
    name = models.CharField(max_length = 50 )
    position = GeopositionField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return str(self.name)