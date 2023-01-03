from django.shortcuts import render
from home.models import Rohildb
from home.forms import FormRohil

def home(request):
    rohil = Rohildb.objects.all()
    context = {
        'rohil': rohil,
    }
    return render(request,'index.html',context)

def create(request):
    form = FormRohil()
    
    context = {
        'form': form,
    }
    return render(request,'create.html',context)