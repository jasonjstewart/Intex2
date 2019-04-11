from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from search import models as smod
from django import forms
from django.http import HttpResponseRedirect
from django.db import connection
from django.utils.html import escape

@view_function
def process_request(request, prescriberid):
    # Saves prescriber object
    prescriber = smod.Prescriber.objects.get(prescriberid=prescriberid)
    
    context = {
        'prescriber': prescriber,
    }

    return request.dmp.render('prescriber_profile.html', context)        