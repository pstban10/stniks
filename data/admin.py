from django.contrib import admin
from .models import Persona, PrData, DateOfMedition, Records
# Register your models here.

admin.site.register(Persona)
admin.site.register(PrData)
admin.site.register(DateOfMedition)
admin.site.register(Records)
