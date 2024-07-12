from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Esta es la prueba del funcionamiento del index")
def details(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)