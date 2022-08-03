from unicodedata import name
from django.db import models

from projects.models import Project

# Create your models here.

# clients, featured work
class Client(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name or 'client'


class FeaturedWork(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='featured')

    def __str__(self):
        return self.project.name
