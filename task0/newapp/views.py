from django.shortcuts import render
from .models import profile
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	if request.method == 'POST':
		uname = request.POST.get('username')
		ps = request.POST.get('password')
		user = authenticate(username = uname, password = ps)
		if user:
			return render(request, 'home.html')
		else:
			return render(request, 'index.html', context = {'inv' : 'invalid details'})

	return render(request, 'index.html')
			
def userlogin(request):
	if request.method == 'POST':
		logout(request)
		return HttpResponseRedirect(reverse(''))
	return render(request,'home.html')
def registeruser(request):
	if request.method == 'POST':
		username = request.POST.get("username")
		firstname = request.POST.get('first_name')
		lastname = request.POST.get('last_name')
		email = request.POST.get('email')
		phonenumber = request.POST.get('phonenumber')
		pass1 = request.POST.get("password1")
		pass2 = request.POST.get('password2')
		if pass1 == pass2 and User.objects.filter(username = username).first() == None:
			user = User.objects.create_user(username = username, first_name = firstname ,last_name = lastname, email = email, password = pass1 )
			profile.objects.create(user = user, phno = phonenumber)
			usertwo = authenticate(username = username, password = pass1)
			if usertwo:
				return render(request, 'home.html')
		elif(pass1 != pass2):
			return render(request, 'register.html',context = {'invpass':'wrong password'})
		elif(User.objects.filter(username = username).first() != None):
			return render(request,'register.html',context = {"usererror":'already exists'})
	return render(request,"register.html")				 



