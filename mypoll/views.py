from django.shortcuts import render ,HttpResponse  , get_object_or_404
from django.db.models import F
from django.urls import reverse
# from django.template import loader
from .models import Question ,Choice
from django.http import Http404 ,HttpResponseRedirect
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

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "mypoll/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request,"mypoll/detail.html",
                      {
                          "question" : question,
                          "error_message" : "you did not select a choice",
                          "selected_Choice" : selected_choice
                      },
                    )   
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("mypoll:results", args=(question.id,)))