from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *
from Answerme.Helpers import queryset_to_json

# Create your views here.
def questions(request):
    return render(request, 'questions.html', {})



def get_questions(request):
    questions = Question.objects.filter(deleted_at=None)
    response = queryset_to_json(questions)

    print(response)

    return HttpResponse(json.dumps(response), content_type="application/json")


def new_question(request):
    return render(request, 'newQuestion.html', {})


def get_labels(request):
    label = Label.objects.filter(deleted_at=None, name__startswith=request.POST['label'])
    response = queryset_to_json(label)

    return HttpResponse(json.dumps(response), content_type="application/json")




'''
This function save a new question
@author Luis GP
@return JSON
'''
def save_question(request):
    response = {}

    try:

        if request.method == "POST":
            data     = request.POST
            labels   = data.getlist('labels[]')
            question = Question()

            question.id_user     = request.user.id
            question.title       = data['title']
            question.description = data['description'] 
            question.views       = 0

            question.save()

            for i in labels:
                label = Label.objects.get(pk=i)
                lq    = LabelsQuestion()

                lq.id_question = question.pk
                lq.id_label    = label.id_label
                lq.label       = label.name
                lq.save()

            
            response = {'message': "The question was save successfuly!", 'code': 200}

    except Exception as e:
        response = {'message': f"error: {e}", 'code': 500}
            


    return HttpResponse(json.dumps(response), content_type="application/json")