from django.shortcuts import render
from traveller.models import Package

def index(request):
    
    dests = Package.objects.all()

    return render(request,'index.html',{'dest':dests})
