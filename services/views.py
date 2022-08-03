from django.views.generic import ListView, DetailView

from services.models import Service

# Create your views here.

class ServiceListView(ListView):
    model = Service
    template_name = "services/service-list.djhtml"
    context_object_name = 'services'



class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/service-detail.djhtml"
    context_object_name = 'service'
