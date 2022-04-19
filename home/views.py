from django.shortcuts import render
from questions.models import *
from Answerme.Helpers import queryset_to_json

# Create your views here.

def home(request):

    questions = Question.objects.filter(deleted_at=None)
    response = []

    for i in questions:
        question = {}
        labels   = queryset_to_json(i.labelsquestion_set.all())

        question['id_question'] = i.id_question
        question['title']       = i.title
        question['description'] = i.description
        question['views']       = i.views
        question['updated_at']  = i.updated_at.strftime("%d/%m/%Y")
        question['labels']      = labels

        response.append(question)        

    return render(request, 'home.html', {'questions': response})
