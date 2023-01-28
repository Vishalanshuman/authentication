from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.base ),
    path('signup/', views.signupPage,name='signupPage'),
    path('login', views.loginPage, name='loginpage'),
    path('logout/',views.logoutPage, name='logoutPage'),
    path('update/',views.updateProfile,name='updateProfile'),
    path('adhar_detail/', views.Adhar_detail, name='adhar'),
    path('update_adhar/', views.update_adhar, name='adhar_update'),
    path('employment/', views.add_employement,name="employmentPage"),
    path('employment-list/', views.employee_list,name="employment_list"),
    path('employment-list/<int:id>/', views.Update_employment,name="employment_update"),
    path('employment/<int:id>/', views.delete_employment,name="employment_delete"),

]