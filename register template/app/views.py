from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def register(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg =  "Email Aready Registered"
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    contact = request.POST['contact'],
                    password = request.POST['password'],
                )
                return render(request,'login.html',{'msg':msg})
            else:
                msg = "Password & Confirm Password Does Not Match"
                return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'register.html')

def home(request):
    img = Image.objects.all()
    return render(request,'home.html',{'img':img})

def login(request):  
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            if user.password == request.POST['password']:
                request.session['name'] = user.name
                request.session['email'] = user.email
                return redirect('home')
            else:
                msg = "Invalid Password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg = "Email Not Registerd"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
def imgform(request):
    if request.method == "POST":
        Image.objects.create(
            imgname = request.POST['imgname'],
            addimg = request.FILES['addimg'],
        )
        return redirect('home')
    else:
        return render(request,'imgform.html')