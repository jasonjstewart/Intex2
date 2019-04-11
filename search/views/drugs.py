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
    # Creates empty drugs variable
    drugs = []

    # if this is a POST request then process form data
    if request.method == 'POST':
        # Creates instance of form
        form = SearchDrugs(request.POST)

        # Checks validity of Form
        if form.is_valid():
            # Processes the data
            if form.search_drugname != '':
                query_set = smod.Drugs.objects.filter(drugname__icontains=form.search_drugname)
            else:
                query_set = smod.Drugs.objects.all()
            
            if form.search_isopioid != '':
                query_set = query_set.filter(isopioid__icontains=form.search_isopioid)

            # Saves query set
            drugs = query_set

            form = SearchDrugs()
            #moves to context tuple
            context = {
                'drugs': drugs,
                'form': form,
            }

            return request.dmp.render('drugs.html', context)

    # If GET, renders blank form
    else:
        form = SearchDrugs()

    context = {
        'form': form,
        'drugs': drugs,
    }

    return request.dmp.render('drugs.html', context)

class SearchDrugs(forms.Form):
    # Creates list of Drug type options
    TYPE_CHOICES = [
        ('1', 'Opioid'),
        ('0', 'Non-Opioid'),
        ('', 'Both'),
    ]

    # Creates list of Drugs options
    DRUGS = []
    for item in smod.Drugs.objects.values_list('drugname', flat=True):
        DRUGS.append(item)

    drugname = forms.CharField(label='Drug Name', max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'id': 'search-box', 'style': 'margin: 10px 0px 0px 10px;'}))

    isopioid = forms.ChoiceField(label='Drug Type', choices=TYPE_CHOICES, required=False, widget=forms.Select(attrs={'class':'custom-select', 'style': 'margin: 10px 0px 0px 10px;'}))

    #Method to validate data
    def clean(self):
        #Save data to clean variable
        self.search_drugname = self.cleaned_data.get('drugname')
        self.search_isopioid = self.cleaned_data.get('isopioid')

        # Ensures they search on at least one value
        if self.search_drugname == '' and self.search_isopioid == '':
            raise forms.ValidationError('Please search on at least one value')

        # Checks if names are blank

        # Returns cleaned data
        return self.cleaned_data
        