from django.contrib import admin

from projects.models import Project, ProjectPhoto

# Register your models here.
class InlinePhoto(admin.StackedInline):
    model = ProjectPhoto
    extra = 1
    show_change_link = True
    can_delete = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [InlinePhoto]

