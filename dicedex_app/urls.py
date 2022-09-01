from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.home, name='home'),
    # library
    path('library/', views.library_index, name='library'),
    # signup
    path('accounts/signup/', views.signup, name='signup'),

    # games
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),

] 