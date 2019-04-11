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
    drugs = {}
    drugs_id = {}
    for item in smod.Triple.objects.filter(prescriberid=prescriberid):
        drugs[item.drugname.drugname] = item.qty
        drugs_id[item.drugname.drugname] = item.drugname.drugid

    # Grabs average drugs prescriptions
    average_prescription = {}
    for item in drugs:
        average_prescription[item] = int(smod.Triple.objects.filter(drugname=item).aggregate(Avg('qty'))['qty__avg'])
    
    context = {
        'prescriber': prescriber,
        'drugs': drugs,
        'drugs_id': drugs_id,
        'average_prescription': average_prescription,
    }

    return request.dmp.render('prescriberProfile.html', context)        