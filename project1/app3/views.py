# students/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee, User
from django.shortcuts import render, redirect
from django import forms
from .models import SimpleImage



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

# myapp/views.py

# Create a simple ModelForm right in the view for maximum simplicity
class SimpleImageForm(forms.ModelForm):
    class Meta:
        model = SimpleImage
        fields = ['title', 'image']

def upload_image(request):
    if request.method == 'POST':
        # Pass request.POST for text data and request.FILES for the file
        form = SimpleImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Saves the file and stores the path in the database
            return redirect('upload_success') # Redirect after successful upload
    else:
        form = SimpleImageForm()

    all_images = SimpleImage.objects.all() # Fetch existing images for display
    return render(request, 'upload.html', {'form': form, 'images': all_images})

def upload_success(request):
    # A simple success page or redirect back to the upload page
    return render(request, 'success.html')