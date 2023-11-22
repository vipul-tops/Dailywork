from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def forms(request):
    if request.method == "POST":
        Student.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            contact = request.POST['contact'],
            address = request.POST['address']
        )
        msg = "Submit Successfully"
        return render(request,'forms.html',{'msg':msg})
    else:
        return render(request,'forms.html')
    
def show(request):
    return render(request,'show.html')