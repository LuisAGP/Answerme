from django.shortcuts import render
from django.http import HttpResponse
from .models import Answer
from questions.models import Question
from Answerme.Helpers import queryset_to_json, clean_description
import json

# Create your views here.
def answers(request):
    return render(request, 'answers.html', {})




'''
Function to save a answer to a question
@author Luis GP
@return JSON
'''
def save_answer(request):
    response = {}

    if 'POST' not in request.method:
        return HttpResponse("Method not allowed")

    try:

        data = request.POST

        new_answer = Answer()
        new_answer.id_question = Question.objects.get(pk=data['id_question'])
        new_answer.description = clean_description(data['description'])
        new_answer.id_user     = request.user.id
        new_answer.user_name   = request.user.username
        new_answer.votes       = 0

        new_answer.save()

        response = {'message': "The answer was save", 'code': 200}

    except Exception as e:
        response = {'message': f'error: {e}', 'code': 500}


    return HttpResponse(json.dumps(response), content_type="application/json")





'''
Function to get a answers to a question
@author Luis GP
@return JSON
'''
def get_answers(request):

    if 'POST' not in request.method:
        return HttpResponse("Method not allowed")

    try:

        data = request.POST

        question = Question.objects.get(pk=data['id_question'])
        ans = Answer.objects.filter(id_question=question)
        
        response = {'answers': queryset_to_json(ans), 'code': 200}

    except Exception as e:
        response = {'message': f'error: {e}', 'code': 500}


    return HttpResponse(json.dumps(response), content_type="application/json")