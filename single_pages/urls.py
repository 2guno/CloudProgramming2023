from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('about_me/', views.about_me),
]