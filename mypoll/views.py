from django.shortcuts import render ,HttpResponse 
# from django.template import loader
from .models import Question ,Choice
from django.http import Http404
# Create your views here.
def index(request):
    question_ls = Question.objects.all()
    # template =  loader.get_template("mypoll/index.html")
    context = {"question_ls" : question_ls }
    return render(request,"mypoll/index.html",context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question dpes not exit")
    choice  = Choice.objects.filter(question = question)
    context = {"choice" : choice,
               "question" : question}

    return render(request,"mypoll/detail.html",context)