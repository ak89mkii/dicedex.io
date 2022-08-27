from django.urls import path
from . import views
# from django.contrib.auth.models import User

urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.library_index, name='library'),
]