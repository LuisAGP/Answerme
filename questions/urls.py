from django.urls import path
from .views import *

urlpatterns = [
    path('',                                 questions,     name='questions'),
    path('ask/',                             new_question,  name="ask"),
    path('getQuestions/',                    get_questions, name="getQuestions"),
    path('saveQuestion/',                    save_question, name="saveQuestion"),
    path('getLabels/',                       get_labels,    name="getLabels"),
    path('questionDetails/<int:idQuestion>', question_details, name="questionDetails"),
]