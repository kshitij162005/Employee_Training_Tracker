from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Employee, TrainingProgram
from .forms import EmployeeForm, TrainingProgramForm
from .models import Employee, TrainingProgram, Enrollment
from .forms import EnrollmentForm

# Create your views here.

def index(request):
    return render(request, 'training/index.html')

def home(request):
    return HttpResponse("<h1>Welcome to Employee Training Tracker!</h1>")


def employee_list(request):
    department = request.GET.get('department')
    employees = Employee.objects.all()
    if department:
        employees = employees.filter(department=department)

    departments = Employee.objects.values('department').distinct()
    return render(request, 'training/employee_list.html', {
        'employees': employees,
        'departments': departments
    })

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



def employee_list(request):
    employees = Employee.objects.all()
    department = request.GET.get('department')

    if department:
        employees = employees.filter(department=department)

    departments = Employee.objects.values('department').distinct()
    return render(request, 'training/employee_list.html', {'employees': employees, 'departments': departments})

def enroll_employee(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # ✅ use redirect instead of render
    else:
        form = EnrollmentForm()
    return render(request, 'training/enroll_employee.html', {'form': form})

def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('employee', 'training_program').all()
    return render(request, 'training/enrollment_list.html', {'enrollments': enrollments})


def success(request):
    return render(request, 'training/success.html')  # Create a success page


