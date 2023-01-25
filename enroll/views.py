from django.shortcuts import render, redirect
from .forms import CreateUser, ProfileCreation,Adhar_card_form
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


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
            return redirect('adhar')
        else:
          messages.info(request, "Username or password is incorrect..")
    context = {}
    return render(request, 'login.html',context)

def logoutPage(request):
    logout(request)
    messages.success(request, "You are successfully Loggedout....")
    return redirect('/')


def Adhar_detail(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = Adhar_card_form(request.POST, request.FILES)
            if form.is_valid():
                adhar_form=form.save(commit=False)
                adhar_form.employee = request.user
                adhar_form.save()
                messages.success(request,"Details are submitted successfully..")
                return redirect("/")
            else:
                messages.info(request, str(form.errors))
        else:
            form = Adhar_card_form()
            context = {'form':form}
            return render(request,'adhar_detail.html', context)
    else:
        return redirect("loginpage")

def update_adhar(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = Adhar_card_form(request.POST, request.FILES, instance=request.user.employee_doc)
            if form.is_valid():
                adhar_form=form.save(commit=False)
                adhar_form.employee = request.user
                adhar_form.save()
                messages.success(request,"Details are submitted successfully..")
                return redirect("/")
            else:
                messages.info(request, str(form.errors))
        else:
            form = Adhar_card_form(instance=request.user.employee_doc)
            context = {'form':form}
            return render(request,'update_adhar.html', context)
    else:
        return redirect("loginpage")




