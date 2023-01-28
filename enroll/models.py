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
    
class Employee_doc(models.Model):
    employee = models.OneToOneField(User,on_delete=models.CASCADE)
    adhar_card = models.CharField(max_length=12)
    adhar_file = models.ImageField(upload_to="adhar_card_file", null=False)

    def __str__(self):
        return self.employee.username

class Employment_details(models.Model):
    employee  = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    company = models.CharField(max_length=300)
    certificate_file = models.ImageField(upload_to='employment_certificates', null=True)
    join_date = models.DateField(null=False)
    last_working_day = models.DateField(null=False)

    def __str__(self):
        return "%s %s"%(self.employee.username, self.company)



