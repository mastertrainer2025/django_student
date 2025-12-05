# students/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee, User



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            messages.success(request, "Login successful.")
            return redirect('home')
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        User.objects.create(username=username, password=password,email=email)
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')
def logout(request): 
    messages.info(request, "You have been logged out.")
    return redirect('register')

def upload(request):
    return render(request , 'upload.html')