from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('', views.cookie_jar_home, name='cookie_jar_home'),
    path('full-screen/', views.cookie_jar_home_fs, name='cookie_jar_home_fs'),  # Displays Full Screen
    path('change-background/', views.cookie_change_bg, name='cookie_change_bg'),  # Displays Change BG page
    path('welcome/', views.cookie_welcome, name='cookie_welcome'),  # Displays welcome page
    path('create/', views.cookie_create, name='cookie_create'),
    path('read/', views.cookie_read, name='cookie_read'),
    path('<int:pk>/details/', views.cookie_details, name='cookie_details'),
    path('<int:pk>/update/', views.cookie_update, name='cookie_update'),
    path('<int:pk>/delete/', views.cookie_delete, name='cookie_delete'),
    path('bs/', views.cookie_bs, name='cookie_bs'),
    path('joke-api/', views.cookie_joke_api, name='cookie_joke_api'),
    path('save_joke-api/', views.cookie_save_joke, name='cookie_save_joke'),
    path('read_joke-api/', views.cookie_read_joke, name='cookie_read_joke'),

]
