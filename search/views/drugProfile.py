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
def process_request(request, drugid):
    # Saves prescriber object
    drug = smod.Drugs.objects.get(drugid=drugid)

    # Returns list of drugs prescribed by doctor
    prescribers = {}
    for item in smod.Triple.objects.filter(drugname=drug.drugname).order_by('-qty')[:10]:
        prescribers[item.prescriberid] = item.qty

    # Grabs average drugs prescriptions
    average_prescription = int(smod.Triple.objects.filter(drugname=drug.drugname).aggregate(Avg('qty'))['qty__avg'])
    
    context = {
        'drug': drug,
        'prescribers': prescribers,
        'average_prescription': average_prescription,
    }

    if request.user.is_authenticated:
        return request.dmp.render('drugProfile.html', context)

    else:
        return HttpResponseRedirect('/account/')