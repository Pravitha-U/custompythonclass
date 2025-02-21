from django.urls import path
from .views import rectangle_view

urlpatterns = [
    path('rectangle/', rectangle_view, name='rectangle_view'),
]