from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect("main:profile")
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login'})
    else:
        if request.user.is_authenticated is True:
            return render(request, 'main/login.html')
        elif request.GET.get('next'):
            return render(request, 'main/login.html', {'error_message': 'You must log in to see this page' })
    return render(request, 'main/login.html')
    
def logout_user(request):
    logout(request)
    return render(request, 'main/login.html')
    
def signup(request):
    def generateVerificationCode():
        return randint(11054,99999)
        
    if request.method == "POST":
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        
        attemptObj = SignUpAttempt.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            verification_code = generateVerificationCode())
        
        request.session['attempt_id'] = attemptObj.id
        return HttpResponseRedirect(reverse('main:verification_code'))
    else:
        return render(request, 'main/signupProcess/signupForm.html')

def verificationCode(request):
    if request.method == "POST":
        verification_code = request.POST.get('verification_code')
        attempt_id = request.POST.get('attempt_id')
        
        attemptObj = SignUpAttempt.objects.get(id=attempt_id)
        
        if verification_code == attemptObj.verification_code:
            return render(request, 'main/profile.html')
        else:
            x = {}
            x['attempt_id'] = request.session.get('attempt_id')
            x['error_message'] = "WRONG"
            return render(request, 'main/signupProcess/verificationCode.html',x)
        
    else:
        x = {}
        x['attempt_id'] = request.session.get('attempt_id')
        return render(request, 'main/signupProcess/verificationCode.html',x)

def profile(request):
    x = {}
    
    # currentUser = request.user
    currentUser = UserProfile.objects.get(user=request.user)
    x['currentUser'] = currentUser
    
    return render(request, 'main/profile.html', x)
# Create your views here.
