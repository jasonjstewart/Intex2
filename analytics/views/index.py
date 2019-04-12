from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    if request.user.is_authenticated and request.user.user_type > 2:
        return request.dmp.render('index.html')

    else:
        return HttpResponseRedirect('account/')