from django.urls import path

from projects.views import ProjectDetailView, ProjectListView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]