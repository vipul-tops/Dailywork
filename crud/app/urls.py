from django.urls import path
from . import views

urlpatterns = [
    path('',views.crud,name='crud'),
    path('add-employee/',views.add_employee,name='add-employee'),
]