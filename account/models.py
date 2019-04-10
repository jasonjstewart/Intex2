from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponseRedirect

# Create your models here.

class customUser (AbstractUser):

    USER_TYPE_CHOICES = (
        (0, 'Default'),
        (1, 'Data Clerk'),
        (2, 'Prescriber'),
        (3, 'Health Official'),
        (4, 'Admin')
    )

    user_type =models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default='0')