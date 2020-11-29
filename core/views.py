from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def Details(request):
    profiles=Profile.objects.all()
    return render(request,'details.html',{'profiles':profiles})

def CreateUser(request):
    context={}
    if request.POST:
        form1=UserForm(request.POST)
        form2=ProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save(commit=False)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            f2.save()
            return redirect('index')
        else:
            context['form1']=form1
            context['form2']=form2
    else:
        form1=UserForm()
        form2=ProfileForm()
        context['form1']=form1
        context['form2']=form2
    return render(request,'register.html',context)

def Edit(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    context={}
    user=MyUser.objects.get(pk=pk)
    profile=Profile.objects.get(user=user)
    form1=UserForm(request.POST or None, request.FILES or None,instance=user)
    form2=ProfileForm(request.POST or None, request.FILES or None,instance=profile)
    if request.POST:
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('details')
    context={'form1':form1,'form2':form2}
    return render(request,'edit.html',context)

def Delete(request,pk):
    user=MyUser.objects.get(pk=pk)
    # profile=Profile.objects.get(user=user)
    user.delete()
    return redirect('details')

def logout_view(request):
    logout(request)
    return redirect('index')
