from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('upload/', views.upload_csv, name='upload_csv'),
]
