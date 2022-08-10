             
from urllib import request
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# Create your views here.

def HomePage(request):
    return render(request, 'Home Page.html')

def LoginPage(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     profile = authenticate(request, user, password)
    # if profile is not None:
    #     login (request, profile)
    #     return redirect('/Dashboard/')
    # else:
    #     pass

    return render(request, 'Login Page.html')

def SignUp(request):

    # if request.method == 'POST':
    #     user = request.POST['user']
    #     password = request.POST['password']
    #     re_pass = request.POST['re_pass']
    #     profile =  User.objects.create(user, password, re_pass)
        
    #     profile.profile_user = user
    #     profile.profile_pass = password
    #     profile.profile_re_pass = re_pass

    #     profile.save()

    #     messages.success(request, "Your Account has been created.")

    #     return redirect('LoginPage')

    return render(request, 'SignUp Page.html')

def Dashboard(request):
    return render(request, 'Dashboard/Dashboard.html')

def Date(request):
    return render(request, 'Dashboard/Date.html')

def WD(request):
    return render(request, 'Dashboard/Wind Down.html')

def WD2(request):
    return render(request, 'Dashboard/Wind Down2.html')

def FM(request):
    return render(request, 'Dashboard/Focus Mode.html')

def FM2(request):
    return render(request, 'Dashboard/Focus Mode2.html')
    
def MUA(request):
    return render(request, 'Dashboard/MUA.html')
