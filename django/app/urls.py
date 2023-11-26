from django.urls import path
from . import views

urlpatterns = [
    path('',views.show,name='show'),
    path('insert/',views.insert,name='insert'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]
