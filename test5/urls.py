from django.urls import path
from .views import pool

urlpatterns = [
    path("test6",pool.as_view()),
    path("test6/<int:id>",pool.as_view()),
]