from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.base ),
    path('signup/', views.signupPage,name='signupPage'),
    path('login', views.loginPage, name='loginpage'),
    path('logout/',views.logoutPage, name='logoutPage'),
    path('update/',views.updateProfile,name='updateProfile'),
    path('employment/', views.add_employement,name="employmentPage"),
    path('update_employment_details/', views.Update_employment,name="updateEmployment"),
    path('delete_employment_details/<str:pk>', views.delete_employment,name="deleteEmployment"),

]