from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponseRedirect

# Create your models here.

class User (AbstractUser):

    birthDate = models.DateTimeField(null=True)
    favcolor = models.TextField(null=True)



        # return the Sale object
