from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from search import models as smod
from django import forms
from django.http import HttpResponseRedirect
from django.db import connection
from django.utils.html import escape
from django.db.models import Q

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
                prescriber_query_set = smod.Prescriber.objects.filter(fname__icontains=form.search_fname)
            else:
                prescriber_query_set = smod.Prescriber.objects.all()
            
            if form.search_lname != '':
                prescriber_query_set = prescriber_query_set.filter(lname__icontains=form.search_lname)

            if form.search_gender != '':
                prescriber_query_set = prescriber_query_set.filter(gender__iexact=form.search_gender)

            if form.search_credentials != '':
                prescriber_query_set = prescriber_query_set.filter(credentials__iexact=form.search_credentials)

            if form.search_location != '':
                prescriber_query_set = prescriber_query_set.filter(state__exact=form.search_location)

            if form.search_specialty != '':
                prescriber_query_set = prescriber_query_set.filter(specialty__iexact=form.search_specialty)

            # Creates list of requested prescriber IDs
            list_prescribers = prescriber_query_set.values_list('prescriberid', flat=True)
            print(list_prescribers)

            # if form.search_drugname != '':
            #     for prescriber in prescriber_query_set:
            #         for item in smod.Triple.objects.filter(drugname=form.search_drugname):
            #             if prescriber.prescriberid == item.prescriberid:
                            

            # Saves query set
            #prescribers = prescriber_query_set

            form = SearchPrescriber()
            #moves to context tuple
            context = {
                'form': form,
            }

            return request.dmp.render('drugsAndPrescribers.html', context)

    # If GET, renders blank form
    else:
        form = SearchPrescriber()

    context = {
        'form': form,
        'prescribers': prescribers,
    }

    return request.dmp.render('drugsAndPrescribers.html', context)

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

    # Creates list of Drug type options
    TYPE_CHOICES = [
        ('1', 'Opioid'),
        ('0', 'Non-Opioid'),
        ('', 'Both'),
    ]

    # Creates list of Drugs options
    DRUGS = []
    for item in smod.Drugs.objects.values_list('drugname', flat=True):
        DRUGS.append((item, item))

    DRUGS.insert(0,('', 'Search all drugs'))

    fname = forms.CharField(label='First Name', max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'id': 'search-box', 'style': 'margin: 10px 0px 0px 10px;'}))
    lname = forms.CharField(label='Last Name', max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'id': 'search-box', 'style': 'margin: 10px 0px 0px 10px;'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))
    credentials = forms.ChoiceField(choices=CREDENTIALS, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))
    location = forms.ChoiceField(choices=LOCATIONS, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))
    specialty = forms.ChoiceField(choices=SPECIALTIES, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))
    drugname = forms.ChoiceField(label='Drug Name', choices=DRUGS, required=False, widget=forms.Select(attrs={'class': 'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))
    isopioid = forms.ChoiceField(label='Drug Type', choices=TYPE_CHOICES, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px; '}))

    #Method to validate data
    def clean(self):
        #Save data to clean variable
        self.search_fname = self.cleaned_data.get('fname')
        self.search_lname = self.cleaned_data.get('lname')
        self.search_gender = self.cleaned_data.get('gender')
        self.search_credentials = self.cleaned_data.get('credentials')
        self.search_location = self.cleaned_data.get('location')
        self.search_specialty = self.cleaned_data.get('specialty')
        self.search_drugname = self.cleaned_data.get('drugname')
        self.search_isopioid = self.cleaned_data.get('isopioid')

        # Ensures they search on at least one value
        if self.search_fname == '' and self.search_lname == '' and self.search_gender == '' and self.search_credentials == '' and self.search_location == '' and self.search_specialty == '' and self.drugname == '' and self.isopioid == '':
            raise forms.ValidationError('Please search on at least one value')

        # Checks if names are blank

        # Returns cleaned data
        return self.cleaned_data
        