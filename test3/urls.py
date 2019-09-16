from django.urls import path
from .views import *
urlpatterns =[
    path("test3",pool.as_view()),
    path("test3/<int:id>",pool1.as_view()),
]