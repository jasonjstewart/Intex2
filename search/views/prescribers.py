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
    # Creates empty prescribers variable
    prescribers = []

    # if this is a POST request then process form data
    if request.method == 'POST':
        # Creates instance of form
        form = SearchPrescriber(request.POST)

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
            prescribers = query_set

            form = SearchPrescriber()
            #moves to context tuple
            context = {
                'prescribers': prescribers,
                'form': form,
            }

            return request.dmp.render('prescribers.html', context)

    # If GET, renders blank form
    else:
        form = SearchPrescriber()

    context = {
        'form': form,
        'prescribers': prescribers,
    }

    return request.dmp.render('prescribers.html', context)

class SearchPrescriber(forms.Form):
    # Creates list of Gender options
    GENDER_CHOICES = [
        ('', 'All'),
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    # Creates list of Specialty options
    SPECIALTIES = []
    for item in smod.Prescriber.objects.values_list('specialty', flat=True):
        SPECIALTIES.append((item, item))

    # Elimitates duplicates
    specialties_set = set(SPECIALTIES)
    SPECIALTIES.clear()
    SPECIALTIES = list(specialties_set)
    SPECIALTIES.sort()
    SPECIALTIES.insert(0,('', 'Search all specialties'))

    # Creates list of Credentials options
    CREDENTIALS = []
    for item in smod.Prescriber.objects.values_list('credentials', flat=True).exclude(credentials__exact=''):
        CREDENTIALS.append((item, item))

    # Elimintates duplicates
    credentials_set = set(CREDENTIALS)
    CREDENTIALS.clear()
    CREDENTIALS = list(credentials_set)
    CREDENTIALS.sort()
    CREDENTIALS.insert(0,('','Search all credentials'))

    # Creates list of Location options
    LOCATIONS = []
    for item in smod.Statedata.objects.all():
        LOCATIONS.append((item.stateabbrev, item.state))

    # Adds option for any state
    LOCATIONS.insert(0,('', 'Search all locations'))

    fname = forms.CharField(label='First Name', max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'id': 'search-box', 'style': 'margin: 10px 0px 0px 10px;'}))
    lname = forms.CharField(label='Last Name', max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'id': 'search-box', 'style': 'margin: 10px 0px 0px 10px;'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))
    credentials = forms.ChoiceField(choices=CREDENTIALS, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))
    location = forms.ChoiceField(choices=LOCATIONS, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))
    specialty = forms.ChoiceField(choices=SPECIALTIES, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))

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
        