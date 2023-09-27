from typing import Set

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    myname = " Hoàng Duy"
    tai_san  = {"Điện thoai", "Laptop","Nhiều tiền"}

    context = {"name": myname,"tai_san":tai_san}
    return render(request,"polls/index.html",context)

