from django.contrib import admin
from django.urls import path 
from . import views
from .views import IndexView




urlpatterns = [
    path('',IndexView.as_view(),name='Index' ), 
    path('update/<str:pk>',views.edit,name='edit'),
    path('delete/<str:pk>',views.delete,name='delete'),
]
