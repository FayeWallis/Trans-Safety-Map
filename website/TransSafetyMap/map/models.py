# from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Incident(models.Model):
    id              = models.UUIDField(null=False, primary_key=True)
    city            = models.CharField(max_length=128, blank=True, null=True)
    state           = models.CharField(max_length=2, blank=True, null=True)
    year            = models.IntegerField(blank=True, null=True)
    severity        = models.CharField(max_length=128, blank=True, null=True)
    geocode_output  = models.CharField(max_length=128, blank=True, null=True)
    geocoded_point  = models.PointField(srid=4326)

    class Meta:
        managed = False
        db_table = 'incidents'
        verbose_name_plural = 'Incidents'
    
    def __str__(self):
        return f'{self.year} {self.severity} in {self.city}, {self.state}'