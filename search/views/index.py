from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from search import models as smod
from django import forms
from django.http import HttpResponseRedirect
from django.db import connection
from django.utils.html import escape

@view_function
def process_request(request):
    if request.user.is_authenticated:
        return request.dmp.render('index.html')

    else:
        return HttpResponseRedirect('account/')
    