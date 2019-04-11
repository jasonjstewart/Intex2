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
    # Creates empty providers variable
    providers = []

    # if this is a POST request then process form data
    if request.method == 'POST':
        # Creates instance of form
        form = SearchProvider(request.POST)

        # Checks validity of Form
        if form.is_valid():
            # Processes the data
            if form.search_fname != '':
                query_set = smod.Prescriber.objects.filter(fname__icontains=form.search_fname)
            else:
                query_set = smod.Prescriber.objects.all()
            
            if form.search_lname != '':
                query_set = query_set.filter(lname__icontains=form.search_lname)

            if form.search_gender != '':
                query_set = query_set.filter(gender__iexact=form.search_gender)

            if form.search_credentials != '':
                query_set = query_set.filter(credentials__iexact=form.search_credentials)

            if form.search_location != '':
                query_set = query_set.filter(state__exact=form.search_location)

            if form.search_specialty != '':
                query_set = query_set.filter(specialty__iexact=form.search_specialty)

            # Saves query set
            providers = query_set

            form = SearchProvider()
            #moves to context tuple
            context = {
                'providers': providers,
                'form': form,
            }

            return request.dmp.render('prescribers.html', context)

    # If GET, renders blank form
    else:
        form = SearchProvider()

    context = {
        'form': form,
        'providers': providers,
    }

    return request.dmp.render('prescribers.html', context)

class SearchProvider(forms.Form):
    # Creates list of Gender options
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('', 'Either'),
    ]

    # Creates list of Specialty options
    SPECIALTIES = []
    for item in smod.Prescriber.objects.values_list('specialty', flat=True):
        SPECIALTIES.append((item, item))

    # Elimitates duplicates
    specialties_set = set(SPECIALTIES)
    SPECIALTIES.clear()
    SPECIALTIES = list(specialties_set)
    SPECIALTIES.append(('', 'Search all specialties'))

    # Creates list of Credentials options
    CREDENTIALS = []
    for item in smod.Prescriber.objects.values_list('credentials', flat=True).exclude(credentials__exact=''):
        CREDENTIALS.append((item, item))

    # Elimintates duplicates
    credentials_set = set(CREDENTIALS)
    CREDENTIALS.clear()
    CREDENTIALS = list(credentials_set)
    CREDENTIALS.append(('', 'Search all specialties'))

    # Creates list of Location options
    LOCATIONS = []
    for item in smod.Statedata.objects.all():
        LOCATIONS.append((item.stateabbrev, item.state))

    # Adds option for any state
    LOCATIONS.append(('', 'Search all locations'))

    fname = forms.CharField(label='', max_length=11, required=False, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control mr-sm-2', 'id': 'search-box'}))
    lname = forms.CharField(label='', max_length=11, required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control mr-sm-2', 'id': 'search-box'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.Select(attrs={'class':'custom-select'}))
    credentials = forms.ChoiceField(choices=CREDENTIALS, required=False, widget=forms.Select(attrs={'class':'custom-select'}))
    location = forms.ChoiceField(choices=LOCATIONS, required=False, widget=forms.Select(attrs={'class':'custom-select'}))
    specialty = forms.ChoiceField(choices=SPECIALTIES, required=False, widget=forms.Select(attrs={'class':'custom-select'}))

    #Method to validate data
    def clean(self):
        #Save data to clean variable
        self.search_fname = self.cleaned_data.get('fname')
        self.search_lname = self.cleaned_data.get('lname')
        self.search_gender = self.cleaned_data.get('gender')
        self.search_credentials = self.cleaned_data.get('credentials')
        self.search_location = self.cleaned_data.get('location')
        self.search_specialty = self.cleaned_data.get('specialty')

        # Ensures they search on at least one value
        if self.search_fname == '' and self.search_lname == '' and self.search_gender == '' and self.search_credentials == '' and self.search_location == '' and self.search_specialty == '':
            raise forms.ValidationError('Please search on at least one value')

        # Checks if names are blank

        # Returns cleaned data
        return self.cleaned_data
        