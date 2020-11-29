from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
	def create_user(self,email,username,password=None):
		if not email:
			raise ValueError('user must have an email address')
		email=self.normalize_email(email)
		user=self.model(email=email,username=username)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,username,password):
		user=self.create_user(email,username,password)
		user.is_superuser=True
		user.is_staff=True
		user.save(using=self._db)
		return user

class MyUser(AbstractBaseUser):
	email=models.EmailField(max_length=30,unique=True)
	username=models.CharField(max_length=255)
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)

	objects=UserProfileManager()
	USERNAME_FIELD='email' # login 
	REQUIRED_FIELDS=['username'] # required field to be filled

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None):
		return True

	def has_module_perms(self,app_label):
		return True


class Profile(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	address=models.CharField(max_length=250)
	def __str__(self):
		return self.user.email
