from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('users/', views.users, name="users"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('categories/', views.categories, name="categories"),
    path('authors/', views.authors, name="authors"),


]