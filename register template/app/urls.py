from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('imgform/',views.imgform,name='imgform'),
]