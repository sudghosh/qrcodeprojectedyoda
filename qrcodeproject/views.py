from django.shortcuts import render
from website.models import website

def home(request,val):
    val= val
    name = 'Welcome To'
    obj = website.objects.get(id=val)

    context = {
        'name': name,
        'obj': obj
    }

    return render(request,'home.html',context)