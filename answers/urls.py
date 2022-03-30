from django.urls import path
from .views import *

urlpatterns = [
    path('', answers, name='answers')
]