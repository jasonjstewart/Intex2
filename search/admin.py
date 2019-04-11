from django.contrib import admin
from search.models import Prescriber

# Register your models here.

class PrescriberAdmin(admin.ModelAdmin):
    model = Prescriber
    list_display = ['fname', 'lname', 'gender','state','specialty','opioid_prescriber']

admin.site.register(Prescriber, PrescriberAdmin)