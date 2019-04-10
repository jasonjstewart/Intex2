from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect
from account import models as amod

@view_function
def process_request(request):

    if request.user.is_authenticated:
        return request.dmp.render('index.html')

    else:
        return HttpResponseRedirect('account/')