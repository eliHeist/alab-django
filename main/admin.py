from django.contrib import admin

from main.models import Client, FeaturedWork

# Register your models here.
admin.site.register([Client, FeaturedWork])