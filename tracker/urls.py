from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # This <int:pk> captures the ID from the URL
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]