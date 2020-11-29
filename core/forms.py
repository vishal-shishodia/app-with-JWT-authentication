from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):
    email=forms.EmailField(max_length=50)
    # password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    # password2=forms.CharField(label="Password Confirmation",widget=forms.PasswordInput)

    class Meta:
        model=MyUser
        fields=['email','username','password1','password2']
        # fields=['email','username']

    # def clean_password2(self):
    #     password1=self.cleaned_data.get('password1')
    #     password2=self.cleaned_data.get('password2')
    #     if password1 and password2 and password1!=password2:
    #         raise forms.ValidationError('Password mismatch')
    #     return password2

    # def save(self,commit=True):
    #     user=super(UserForm,self).save(commit=False)
    #     user.set_password(self.cleaned_data['password2'])
    #     if commit:
    #         user.save()
    #     return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address']
