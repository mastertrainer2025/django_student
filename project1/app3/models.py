# students/models.py
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    grade = models.CharField(max_length=10) # e.g., "10th", "B+", etc.
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # In practice, use hashed passwords

    def __str__(self):
        return self.username
    
class ImageModel(models.Model):
    title = models.CharField(max_length=200)
    # ImageField automatically uses Pillow to validate the file is an image.
    # upload_to='images/' specifies a subdirectory inside MEDIA_ROOT
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

class SimpleImage(models.Model):
    title = models.CharField(max_length=100)
    # The image file will be saved inside 'media/uploads/'
    image = models.ImageField(upload_to='uploads/') 
    
    def __str__(self):
        return self.title