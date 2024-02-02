from django.urls import path
from . import views

app_name = 'calculate'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('substarct/', views.subtract, name='subtract'),
    path('multiply/', views.multiply, name='multiply'),
    path('divide/', views.divide, name='divide'),
]
