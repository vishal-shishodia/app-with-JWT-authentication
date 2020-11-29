from django.urls import path
from .views import *

urlpatterns=[
    path('signin/',UserLoginView.as_view()),
]