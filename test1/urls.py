from django.urls import path,include
from .views import *
from rest_framework import routers



urlpatterns = [
    path("test2",test2),
    path("test2/<int:id>",test21),
]