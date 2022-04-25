from django.shortcuts import render
from django.http import HttpResponse
from .models import Answer, Vote
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





'''
Function to save a vote up
@author Luis GP
'''
def vote_up(request):

    response = {'code': 500}

    if 'POST' not in request.method:
        return HttpResponse("Method not allowed")

    id_answer = request.POST['id_answer']
    answer    = Answer.objects.get(pk=id_answer)
    user_vote = Vote.objects.filter(id_answer__id_answer=id_answer, id_user=request.user.id).first()

    if not user_vote:
        vote = Vote()
        vote.id_answer     = answer
        vote.id_user       = request.user.id
        vote.positive_vote = True
        vote.save()

    elif not user_vote.positive_vote:
        user_vote.positive_vote = True
        user_vote.negative_vote = False
        user_vote.save()       
        

    if answer.id_question.id_user == request.user.id: # This case is the solution
        if answer.id_question.id_solution:
            solution = Answer.objects.get(pk=answer.id_question.id_solution)
            solution.is_solution = False
            solution.save()

        answer.is_solution = True
        answer.id_question.id_solution = answer.pk
        answer.id_question.save()
        answer.save()

    
    answer.recalculate_votes()

    response = {'code': 200}

    return HttpResponse(json.dumps(response), content_type="application/json")






'''
Function to save a vote down
@author Luis GP
'''
def vote_down(request):

    response = {'code': 500}

    if 'POST' not in request.method:
        return HttpResponse("Method not allowed")

    id_answer = request.POST['id_answer']
    answer    = Answer.objects.get(pk=id_answer)
    user_vote = Vote.objects.filter(id_answer__id_answer=id_answer, id_user=request.user.id).first()

    if not user_vote:
        vote = Vote()
        vote.id_answer     = answer
        vote.id_user       = request.user.id
        vote.negative_vote = True
        vote.save()

    elif not user_vote.negative_vote:
        user_vote.positive_vote = False
        user_vote.negative_vote = True
        user_vote.save()

    answer.recalculate_votes()

    response = {'code': 200}

    return HttpResponse(json.dumps(response), content_type="application/json")