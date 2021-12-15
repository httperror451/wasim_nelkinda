from django.shortcuts import render
from calculator.models import *
# Create your views here.
def Indexpage(request):
    data = {
        'testdata':hello()
    }

    return render(request,'index.html',data)