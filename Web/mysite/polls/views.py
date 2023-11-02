from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from . models import Question
# Create your views here.
def index(request):
    my_name = "Hoang Duy"
    tai_san = {"Phone","laptop","Plane","money"}
    context = {"name":my_name,"tai_san":tai_san}
    return render(request,"polls/index.html",context)
def view_list(request):
    list_questiom = Question.objects.all()
    contex = {"dsquest": list_questiom}
    return render(request,"polls/question_list.html",contex)

def detail_view(request,question_id):
    q = Question.objects.get(pk=question_id)
    return render(request,"polls/detail_question.html",{"qs":q})

def vote(request,question_id):
    q  = Question.objects.get(pk = question_id)
    try:
        data = request.POST["choice"]
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("Khong co cau tra loi")
    c.vote = c.vote + 1
    c.save()
    return render(request,"polls/result.html",{"q":q})