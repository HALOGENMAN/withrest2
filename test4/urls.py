from django.urls import path
from . import views
urlpatterns = [
    path("test41/<int:id>",views.pool.as_view()),
    path("test41",views.pool.as_view()),
]