
from django.contrib import admin
from django.urls import path
from apollo_app import views
urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('safe_a/', views.safe_a),
]
