from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('register/',CreateUser,name='register'),
    path('edit/<str:pk>/',Edit,name='edit'),
    path('delete/<str:pk>/',Delete,name='delete'),
    path('details/',Details,name='details'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',logout_view,name='logout'),
]