from  django.urls import path
from .views import Indexclass,LoginClass,ViewUser,viewProduct,AddPost

app_name ='Login'
urlpatterns = [
    path('', Indexclass.as_view(), name = "index"),
    path('Login/',LoginClass.as_view(),name = 'Login'),
    path('user-view/', ViewUser.as_view(), name = "user_view"),
    path("viewProduct/",viewProduct, name="product"),
    path("add-post/", AddPost.as_view(), name = "add_post" )
]
