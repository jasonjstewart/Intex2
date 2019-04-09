from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

@view_function
def process_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

        context = {
        'form': form,
        }
    return request.dmp.render('signup.html', context)

class UserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
        self.fields['password2'].label = "Confirm Password"