from django.contrib import admin
from django.urls import path, include
from AdminDashboard import views

urlpatterns = [
    path('', views.index, name='adminDashboard'),
    path('home', views.home_view, name='admin-home'),
    path('analytics', views.analytics_view, name='admin-analytics'),
    path('weekly-traffic', views.weekly_traffic, name='admin-weekly-traffic')
]
