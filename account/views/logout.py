from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms
from django.shortcuts import redirect

@view_function
def process_request(request):
    logout(request)

    #render the template
    return redirect('/account/login')