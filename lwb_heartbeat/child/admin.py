from django.contrib import admin
from .models import Child, LWBProgram, MedicalCodes, Country, Education, Nutrition, Trafficking, HealingHome, FosterCare, GeneralUpdate, MedicalUpdate, GrowthData

# Register your models here.
admin.site.register((Country))
admin.site.register((Child))
admin.site.register((MedicalCodes))
admin.site.register((GeneralUpdate))
admin.site.register((MedicalUpdate))
admin.site.register((GrowthData))
admin.site.register((LWBProgram))
admin.site.register((Education))
admin.site.register((FosterCare))
admin.site.register((HealingHome))
admin.site.register((Trafficking))
admin.site.register((Nutrition))


