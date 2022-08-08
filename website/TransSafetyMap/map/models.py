from django.db import models

# Create your models here.

class Incident(models.Model):
    id       = models.UUIDField(null=False, primary_key=True)
    city     = models.CharField(max_length=128, blank=True, null=True)
    state    = models.CharField(max_length=2, blank=True, null=True)
    year     = models.IntegerField(blank=True, null=True)
    severity = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidents'