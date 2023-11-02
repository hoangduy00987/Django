from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm,Send_email
from django.views import View

# Create your views here.
class IndexClass(View):
    def get(self, request):
        return HttpResponse("Hello World!!")


class ClassSave(View):

    def get(self, request):
        a = PostForm()
        return render(request, "news/add_news.html", {'f': a})

    def post(self,request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Luu roi")
        else:
            return HttpResponse("Deo luu")
    def put(self):
        pass

def email_view(request):
    b = Send_email()
    return render(request,'news/email.html',{'f':b})

def process(request):
    if request.method == "POST":
        d = Send_email(request.POST)
        if d.is_valid():
            # td = d.cleaned_data['title']
            # cc = d.cleaned_data['cc']
            # noidungg = d.cleaned_data['content']
            # email = d.cleaned_data['email']
            # context = {'td':td, 'c':cc,'b':noidungg,'a':email}
            context2 = {'email_data':d}
            return render(request, 'news/print_email.html',context2)
        else:
            HttpResponse("not")
    else:
        HttpResponse("khong phai post method")