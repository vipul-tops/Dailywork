from django.shortcuts import render
from .models import Employee
# Create your views here.
def crud(request):
	return render(request,'crud.html')

def add_employee(request):
	if request.method=="POST":
		Employee.objects.create(
        	name=request.POST['name'],
        	email=request.POST['email'],
        	address=request.POST['address'],
        	phone=request.POST['phone'],
        	)
		return render(request,'crud.html')
	else:
		return render(request,'crud.html')