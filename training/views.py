from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, TrainingProgram
from .forms import EmployeeForm, TrainingProgramForm

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Employee Training Tracker!</h1>")


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'training/employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'training/employee_form.html', {'form': form})

# Program views
def program_list(request):
    programs = TrainingProgram.objects.all()
    return render(request, 'training/program_list.html', {'programs': programs})

def program_create(request):
    if request.method == 'POST':
        form = TrainingProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = TrainingProgramForm()
    return render(request, 'training/program_form.html', {'form': form})

