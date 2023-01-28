from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm  
from .models import Profile, Employee_doc, Employment_details
from django import forms


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


    first_name= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Enter your first name', 'class':'form-control'}))
    last_name= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Enter your last name', 'class':'form-control'}))
    email= forms.CharField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'placeholder':'Email', 'class':'form-control'}))
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'})
    )
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'form-control'})
        )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'})
        )
    
 
class ProfileCreation(forms.ModelForm):
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
    )
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = 'user',
    
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES, 
    )

class Adhar_card_form(forms.ModelForm):
    class Meta:
        model = Employee_doc
        fields = '__all__'
        exclude = 'employee',

class Employment_form(forms.ModelForm):
    class Meta:
        model = Employment_details
        fields = ['employee', 'company','certificate_file','join_date','last_working_day']
        exclude = 'employee',



    company= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Company Name', 'class':'form-control'}))

    join_date= forms.CharField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'placeholder':'YYYY-MM-DD', 'class':'form-control'}))
    last_working_day = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'YYYY-MM-DD', 'class':'form-control'})
    )
