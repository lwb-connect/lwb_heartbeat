from django.contrib import admin
from .models import Child, LWBProgram, MedicalCodes, Country, Education

# Register your models here.
admin.site.register((Country))
admin.site.register((Child))
admin.site.register((LWBProgram))
admin.site.register((MedicalCodes))
admin.site.register((Education))
