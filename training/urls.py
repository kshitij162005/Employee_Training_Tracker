from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-employee/', views.employee_create, name='employee_create'),
    path('employees/', views.employee_list, name='employee_list'),
    path('add-program/', views.program_create, name='program_create'),
    path('enrollments/', views.enrollment_list, name='view_enrollments'),
    path('programs/', views.program_list, name='program_list'),
    path('enroll/', views.enroll_employee, name='enroll_employee'),
    path('success/', views.success, name='success'),
    path('enrollments/', views.enrollment_list, name='enrollment_list'),

]