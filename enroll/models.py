from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    country = CountryField(default='select your country')
    term_condition = models.BooleanField(default=False)
    agree_notifications = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

