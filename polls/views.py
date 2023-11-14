from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo. Estas en el indice de /polls")

# def detail(request, Question_id):
#     return HttpResponse()

# def results(request, Question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

# def vote(request, Question_id):
#     return HttpResponse("You are voting on question %s." % question_id)