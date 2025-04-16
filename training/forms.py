from django import forms
from .models import Employee, TrainingProgram

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgram
        fields = '__all__'
