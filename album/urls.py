from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('showall/', views.showall, name='showall'),
    path('betails/', views.betails, name='betails'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/delete', views.edit, name='delete'),
]
