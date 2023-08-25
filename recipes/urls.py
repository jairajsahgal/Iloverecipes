
from django.urls import path, include

from . import views
from .views import blogview, videopage, BookDetailView
from django.conf.urls import *
from django.urls import path 



app_name= "recipes"

urlpatterns = [
    path("", views.Main, name="Main"),

    path("home", views.Main, name="Home"),

    path('foodblog/', blogview.as_view(), name="foodblog"),

    path('details/<int:pk>', videopage.as_view(), name='details'),

    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    

    path('links/', views.link_view, name='links'),


    path('base/', views.base, name='base'),

    path('search/', views.search_results, name='search_results'),


]








