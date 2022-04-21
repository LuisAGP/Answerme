from django.urls import path
from .views import *

urlpatterns = [
    path('', answers, name='answers'),
    path('saveAnswer/', save_answer, name="saveAnswer"),
    path('getAnswer/', get_answers, name="getAnswer"),
]