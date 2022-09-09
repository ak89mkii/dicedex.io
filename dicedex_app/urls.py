from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.home, name='home'),
    path('home_logged_in', views.home_logged_in, name='home_logged_in'),

    path('groups/', views.groups, name='groups'),
    # library
    path('library/', views.library_index, name='library'),
    path('library_01/', views.library_index_01, name='library_01'),
    path('library_02/', views.library_index_02, name='library_02'),
    path('library_03/', views.library_index_03, name='library_03'),
    # signup
    path('accounts/signup/', views.signup, name='signup'),

    # games
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),

    # themes
    path('themes/create/', views.ThemeCreate.as_view(), name='themes_create'),
    path('themes/<int:pk>/update/', views.ThemeUpdate.as_view(), name='themes_update'),

] 