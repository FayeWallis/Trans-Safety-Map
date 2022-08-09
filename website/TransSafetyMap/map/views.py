from django.views.generic.base import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from .models import Incident
import json 

# Create your views here.
def index(request):
    return render(request, 'index.html')

class mapView(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context['incidents'] = json.loads(serialize("geojson", Incident.objects.all()))
        return context
