from django.urls import path, include
from . import views
from .views import blogview, videopage, BookDetailView, login_view, register_view, UserProfileView
from django.conf.urls import *
from django.urls import path 
from django.contrib import admin

admin.site.site_header = "Cookbook layer"

admin.site.index_title= "Create books here"

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

    path('login/', views.login_view, name='login'),

    path('register/', views.register_view, name='registration'),

    path('profile/<int:pk>/', views.UserProfileView, name='user_profile'),

    path('user_books/<int:user_book_id>/', views.user_book_pages, name='user_book_pages'),

]











