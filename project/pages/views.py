from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'pages\index.html',{'name':'ahmed','age':'25'})

def about(request):
    return render(request,'pages/about.html')

def python(request):
    return render(request,'pages/python.html')

def sql(request):
    return render(request,'pages/sql.html')


def excel(request):
    return render(request,'pages/excel.html')

def powerbi(request):
    return render(request,'pages/powerbi.html')

def tableau(request):
    return render(request,'pages/tableau.html')

def projects(request):
    return render(request,'pages/projects.html')

def contact(request):
    return render(request,'pages/contact.html')