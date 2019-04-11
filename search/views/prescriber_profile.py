from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from search import models as smod
from django import forms
from django.http import HttpResponseRedirect
from django.db import connection
from django.utils.html import escape
from django.db.models import Avg

@view_function
def process_request(request, prescriberid):
    # Saves prescriber object
    prescriber = smod.Prescriber.objects.get(prescriberid=prescriberid)

    # Returns list of drugs prescribed by doctor
    drugs = smod.Triple.objects.filter(prescriberid=prescriberid)

    # Grabs average drugs prescriptions
    for item in drugs:
        average_prescription = smod.Triple.objects.filter(drugname=item.drugname.drugname).aggregate(Avg('qty'))
    
    context = {
        'prescriber': prescriber,
        'drugs': drugs,
    }

    return request.dmp.render('prescriber_profile.html', context)        