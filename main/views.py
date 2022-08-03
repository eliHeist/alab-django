from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import Client, FeaturedWork

# Create your views here.
class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = FeaturedWork.objects.all()
        context['clients'] = Client.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

