from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms

@view_function
def process_request(request):

    #Processes form
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
    else: 
        form = Login()

    context = {
        'form': form,
    }

    #render the template
    return request.dmp.render('index.html', context)

class Login(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    #method to validate data
    def clean(self):
        self.user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid username or password.')
        return self.cleaned_data