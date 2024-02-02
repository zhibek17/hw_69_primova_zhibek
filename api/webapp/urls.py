from django.urls import path
from webapp.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
