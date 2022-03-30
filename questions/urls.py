from django.urls import path
from .views import *

urlpatterns = [
    path('', questions, name='questions'),
    path('ask/', new_question, name="ask"),
    path('getQuestions/', get_questions, name="getQuestions"),
    path('saveQuestion/', save_question, name="save_question"),
    path('getLabels/', get_labels, name="getLabels")
]