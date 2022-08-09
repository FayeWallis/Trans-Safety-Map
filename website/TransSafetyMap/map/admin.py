from django.contrib.gis import admin as geo_admin
from django.contrib import admin
from .models import Incident

# Register your models here.
class IncidentAdmin(geo_admin.ModelAdmin):
    readonly_fields = ('id',)
    # list_display = ('year',  'severity', 'city', 'state')

geo_admin.site.register(Incident, IncidentAdmin)