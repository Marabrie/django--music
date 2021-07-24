from django.urls import path
from . import views
from . views import album_create_views
from . views import album_detail

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('create/', album_create_views),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),

]
