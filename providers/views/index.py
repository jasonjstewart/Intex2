from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    #Forces user to log in before proceeding
    if request.user.is_authenticated:
        return request.dmp.render('index.html')

    else:
        return HttpResponseRedirect('account/')

    print("\n\n\n\n\n")
    print(request.dmp.page)
    context = {
    }
    return request.dmp.render('index.html', context)