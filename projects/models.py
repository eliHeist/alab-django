from django.db import models

from services.models import Service, Skill

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField()
    description = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    service = models.ForeignKey(Service, related_name='projects', on_delete=models.SET_NULL, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    
    def __str__(self):
        return self.name


class ProjectPhoto(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='images')
    photo = models.ImageField()

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'
    
    def __str__(self):
        return f'{self.project.name} photo'