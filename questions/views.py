from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *
from Answerme.Helpers import queryset_to_json
import datetime

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







'''
This function clean de HTML code and retrn only the HTML code of the question
@author Luis GP
@param String
@return String
'''
def clean_description(description):

    description = str(description).replace('<pre class="ql-syntax"', '<pre class="pre-code"')
    description = description.replace('contenteditable="true"', '')
    description = description.replace('class="ql-editor"', '')
    description = description.replace('<div class="ql-clipboard" contenteditable="true" tabindex="-1"></div><div class="ql-tooltip ql-hidden"><a class="ql-preview" target="_blank" href="about:blank"></a><input type="text" data-formula="e=mc^2" data-link="https://quilljs.com" data-video="Embed URL"><a class="ql-action"></a><a class="ql-remove"></a></div>', "")

    return description