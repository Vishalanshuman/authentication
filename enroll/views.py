from django.forms import modelformset_factory, inlineformset_factory
from django.shortcuts import render, redirect, get_list_or_404
from .forms import CreateUser, ProfileCreation,Adhar_card_form,Employment_form
from django.contrib import messages
from .models import Employment_details
from django.contrib.auth import authenticate, login, logout
from django.db import transaction , IntegrityError
from .models import Adhar_card
from django.contrib.auth.models import User


# Create your views here.

def base(request):
    context = {}
    return render(request,'base.html', context)


def signupPage(request):
    if request.method =="POST":
        user = CreateUser(request.POST)
        profile_form  = ProfileCreation(request.POST)
        if  user.is_valid() and profile_form.is_valid():
            user = user.save()
            profile = profile_form.save(commit=False)

            profile.user = user
            profile.save()

            messages.success(request," Successfully Registered ")
            return redirect('loginpage')
        messages.info(request,user.errors, profile_form.errors)
    form = CreateUser()
    profile_form = ProfileCreation()
    context = {'form':form, 'profile_form':profile_form}
    return render(request, 'signup.html',context)

def updateProfile(request):
 
    if request.method =="POST":
        user = CreateUser(request.POST, instance = request.user)
        profile_form  = ProfileCreation(request.POST, instance=request.user.profile)
        if  user.is_valid() and profile_form.is_valid():
            user = user.save()
            profile = profile_form.save(commit=False)

            profile.user = user
            profile.save()

            messages.success(request," Successfully Registered ")
            return redirect('loginpage')
        messages.info(request,user.errors, profile_form.errors)

    form = CreateUser(instance = request.user)
    profile_form = ProfileCreation(instance=request.user.profile)
    context = {'form':form, 'profile_form':profile_form}
    return render(request, 'update_profile.html',context)

def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You are successfully loggedin....')
            return redirect('employmentPage')
        else:
          messages.info(request, "Username or password is incorrect..")
    context = {}
    return render(request, 'login.html',context)

def logoutPage(request):
    logout(request)
    messages.success(request, "You are successfully Loggedout....")
    return redirect('/')

def add_employement(request):
    if request.user.is_authenticated:

        employmentFormset = modelformset_factory(Employment_details,form=Employment_form, extra=5)
        formset = employmentFormset(request.POST or None, request.FILES or None, queryset=Employment_details.objects.none())
        form = Adhar_card_form(request.POST or None,request.FILES or None)
        if request.method=="POST":
            if form.is_valid() and formset.is_valid():
                    adhar = form.save(commit=False)
                    adhar.employee = request.user
                    adhar.save()
                    
                    formset1=formset.save(commit=False)
                    for fields in formset1:
                        fields.employee=request.user
                        fields.save()
                    messages.success(request, 'Details submitted successfully')
                    return redirect('/')
            messages.info(request,form.errors, formset.errors)
        context = {'form':form,'formset':formset}
        return render(request, 'employment.html',context)
    return redirect('loginpage')

def Update_employment(request):
    if request.user.is_authenticated:
        employmentFormset = modelformset_factory(model= Employment_details, form=Employment_form, extra=0)
        formset = employmentFormset(request.POST or None, request.FILES or None, queryset=Employment_details.objects.filter(employee=request.user))
        form = Adhar_card_form(request.POST or None,request.FILES or None, instance=request.user.adhar_card or None)
        if request.method=="POST":
            if form.is_valid() and formset.is_valid():
                    adhar = form.save(commit=False)
                    adhar.employee = request.user
                    adhar.save()
                    formset1=formset.save(commit=False)
                    for fields in formset1:
                        fields.employee = request.user
                        fields.save()
                    messages.success(request, 'Details submitted successfully')
                    return redirect('/')
            messages.info(request,form.errors, formset.errors)
        context = {'form':form,'formset':formset}
        return render(request, 'Update_employment.html',context)
    else:
        return redirect("loginpage")

def delete_employment(request, pk):
    object = get_list_or_404(Employment_details, pk=pk)
    object.delete()
    messages(request, 'Employment Record Deleted Successfully.')
    return redirect('updateEmployment')