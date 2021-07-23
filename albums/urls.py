from django.urls import path
from . import views
from . views import albums_create_views

urlpatterns = [
    path('', views.albums_list, name='albums_list'),
    path('create/', albums_create_views),


]
