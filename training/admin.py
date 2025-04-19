from django.contrib import admin
from .models import Employee, TrainingProgram, Enrollment

# Register your models here.

# Employee Admin Registration
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'designation')  
    search_fields = ('name', 'email', 'department', 'designation')
    list_filter = ('department',)

# Training Program Admin Registration
@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'trainer_name')  
    search_fields = ('title', 'trainer_name')

# Enrollment Admin Registration
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'training_program', 'status')  
    list_filter = ('status',)  
