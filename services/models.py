from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    short_description = models.TextField(max_length=1000)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    

class Package(models.Model):
    set = models.ForeignKey('PackageSet', on_delete=models.CASCADE, related_name='packages')
    name = models.CharField(max_length=50, default='__package__', blank=True)
    price = models.IntegerField()
    best_choice = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class PackageSet(models.Model):
    name = models.CharField(max_length=60)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='sets')

    class Meta:
        verbose_name = 'Package Set'
        verbose_name_plural = 'Package Sets'

    def __str__(self):
        return self.name or f'{self.service.name} set'



class Item(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name