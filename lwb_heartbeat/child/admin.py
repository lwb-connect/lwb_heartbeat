from django.contrib import admin
from .models import Child, Photo

# Register your models here.
admin.site.register((Child, Photo))