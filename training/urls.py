from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_create, name='employee_create'),

    path('programs/', views.program_list, name='program_list'),
    path('programs/add/', views.program_create, name='program_create'),
]