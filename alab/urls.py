from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('services/', include('services.urls', namespace='services')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
