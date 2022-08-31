from django.urls import path
from . import views
# from django.contrib.auth.models import User

urlpatterns = [
    path('', views.home, name='home'),
    # library
    path('library/', views.library_index, name='library'),
    # games
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameCreate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameCreate.as_view(), name='games_delete'),

] 