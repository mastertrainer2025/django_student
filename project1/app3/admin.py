from django.contrib import admin
from .models import Employee, User , ImageModel

# Register your models here.
admin.site.register(Employee)
admin.site.register(User)
admin.site.register(ImageModel)