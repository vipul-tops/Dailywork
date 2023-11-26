from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def insert(request):
    if request.method == "POST":
        Student.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            contact = request.POST['contact'],
            address = request.POST['address']
        )
        msg = "Submit Successfully"
        return render(request,'insert.html',{'msg':msg})
    else:
        return render(request,'insert.html')
    
def show(request):
    st = Student.objects.all()
    return render(request,'show.html',{'st':st})

def edit(request,pk):
    st = Student.objects.get(id=pk)
    return render(request,'edit.html',{'st':st})

def update(request,pk):
    st = Student.objects.get(id=pk)
    st.name = request.POST['name']
    st.email = request.POST['email']
    st.contact = request.POST['contact']
    st.address = request.POST['address']

    st.save()

    return redirect('show')


def delete(request,pk):
    st = Student.objects.get(id=pk)
    st.delete()
    return redirect('show')