from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import *
from answers.models import Answer
from Answerme.Helpers import queryset_to_json, clean_description

# Create your views here.
def questions(request):
    return render(request, 'questions.html', {})





'''
Function to get all questions with his labels
@author Luis GP
@return JSON
'''
def get_questions(request):
    questions = Question.objects.filter(deleted_at=None, id_user=request.user.id)
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

    return HttpResponse(json.dumps(response), content_type="application/json")




'''
New Questions View
@author Luis GP
'''
def new_question(request):
    return render(request, 'newQuestion.html', {})


'''
Details for a question
@author Luis GP
'''
def question_details(request, idQuestion):

    question = Question.objects.get(id_question=idQuestion)
    labels   = LabelsQuestion.objects.filter(id_question=idQuestion)
    ans      = Answer.objects.filter(id_question=question.id_question)

    return render(request, 'questionDetails.html', {'question': question, 'labels': labels, 'answers': ans, 'id_user': request.user.id})






'''
This function is for fill the list of labels availables
@author Luis GP
@return JSON
'''
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

            description = clean_description(data['description'])

            question.id_user     = request.user.id
            question.title       = data['title']
            question.description = description 
            question.views       = 0

            question.save()

            for i in labels:
                label    = Label.objects.get(pk=i)
                question = Question.objects.get(pk=question.pk)
                lq       = LabelsQuestion()

                lq.id_question = question
                lq.id_label    = label
                lq.label       = label.name
                lq.save()

            
            response = {'message': "The question was save successfuly!", 'code': 200}

    except Exception as e:
        response = {'message': f"error: {e}", 'code': 500}
            


    return HttpResponse(json.dumps(response), content_type="application/json")