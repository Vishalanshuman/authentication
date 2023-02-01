from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm  
from .models import Profile, Adhar_card, Employment_details
from django import forms
from django.forms import inlineformset_factory


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
        model = Adhar_card
        fields = '__all__'
        exclude = 'employee',

class DateInput(forms.DateInput):
    input_type='date'
class Employment_form(forms.ModelForm):
    class Meta:
        model = Employment_details
        fields = ['employee', 'company','certificate_file','join_date','last_working_day']
        exclude = 'employee',
        widgets={'last_working_day': DateInput(),'join_date': DateInput()}







employmentFormSet = inlineformset_factory(
    User, Employment_details, form=Employment_form,
    extra=1, can_delete=True, can_delete_extra=True
)

