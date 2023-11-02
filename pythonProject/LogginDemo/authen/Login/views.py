from django.shortcuts import render,HttpResponse
from django.views import  View
from django.contrib.auth import  authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  PostForm
# Create your views here.


class Indexclass(View):
    def get(self, request):
        return HttpResponse('<h1>Xin Chao</h1>')


class LoginClass(View):
    def get(self,request):

        return render(request,'Login/Login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username = username, password = password)
        if my_user is None:
            return HttpResponse("Deo co tai khoan thi cut")

        login(request,my_user)
        return render(request, 'Login/success.html')


class ViewUser(LoginRequiredMixin, View):
    login_url = '/Login/'
    def get(self,request):
        return HttpResponse("<h1>Day la view user</h1>")

@decorators.login_required(login_url='/Login/')
def viewProduct(request):
    return HttpResponse("Xem san pham")


class AddPost(LoginRequiredMixin,View):
    login_url = '/Login/'

    def get(self,request):
        form = PostForm
        context = {'fm':form}
        return render(request, 'Login/add_post.html', context)

    def post(self,request):
        f = PostForm(request.POST)
        if  not f.is_valid():
            return HttpResponse("ban nhap sai du lieu roi")
        #cach reload lai database user
        print(request.user.get_all_permissions())
        if request.user.has_perm('Login.add_post'): # viet thuong
            f.save()
        else:
             return HttpResponse("may khong co quyen")

        return HttpResponse("Ok nha")