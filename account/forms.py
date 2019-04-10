# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account.models import customUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = customUser
        fields = ('username', 'first_name', 'last_name','email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
        self.fields['password2'].label = "Confirm Password"
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = customUser
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type')
