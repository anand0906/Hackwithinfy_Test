
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *

def home(request):
    form=InputForm()
    if request.method=='POST':
        form=InputForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context={
        'form':form
    }
    return render(request,'home.html',context)