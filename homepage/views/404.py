from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect
from account import models as amod

@view_function
def handler404(request):
    return render(request, '404.html', status=404)
