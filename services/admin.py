from django.contrib import admin

from services.models import Item, Package, PackageSet, Service

# Register your models here.
admin.site.register([Service, PackageSet])

class InlineItem(admin.StackedInline):
    model = Item
    extra = 1
    show_change_link = True
    can_delete = True


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    inlines = [InlineItem]