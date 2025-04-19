from django import forms
from .models import Employee, TrainingProgram, Enrollment

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgram
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['employee', 'training_program', 'status']
