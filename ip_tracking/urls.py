from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint
    path('', views.home, name='home'),
]
