from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, EmployeePayrollProfile, EmployeeNetPay
from .forms import PayProfileForm
# Create your views here.


def employee_create_view(request):
    return render(request, "employee/create_employee.html")


def list_employees_view(request):
    context = {
        'employee_list': Employee.objects.all()
    }
    return render(request, "employee/list_employees.html", context)


def employee_payroll_profile_view(request, employee_id):
    # form = PayProfileForm
    # context = {
    #     'form': form
    # }
    # employee = get_object_or_404(EmployeePayrollProfile, pk=employee_id)
    # try:
    #     employee_pay = EmployeePayrollProfile.objects.get(pk=employee_id)
    # except employee_pay.DoesNotExist():
        # return HttpResponse("no student found")
    employee = Employee.objects.get(pk=employee_id)

    context = {
        'employee': employee
    }
    return render(request, "employee/employee_payroll_profile_edit.html", context)

    # if employee_pay.Exists():
    #     context = {
    #         'employee': employee_pay
    #     }
    #     return render(request, "employee/employee_payroll_profile.html", context)
    # return HttpResponseRedirect(reverse('employee:payroll_profile', args=(employee.id,)))


def employee_process_payroll(request):
    context = {
        'employee_profiles': EmployeePayrollProfile.objects.all()
    }
    return render(request, "employee/process_payroll.html", context)


def calculate_pay(request):
    if request.method != 'POST':
        return HttpResponse("<h3>method not allowed</h3>")
    else:
        print(request.POST)
        salary_list = request.POST.getlist('monthly_salary[]')
        med_allw_list = request.POST.getlist('medical_allowance[]')
        for one_salary in salary_list:
            emp = Employee.objects.get(id=one_salary)
            emp_salary_input = request.POST.get('monthly_salary[one_salary]')
            emp_med_allw_input = request.POST.get(
                'medical_allowance[one_salary]')

            # student_subject = StudentSubjects(
            #     subject_id=subj, student_id=student)
            # student_subject.save()
        context = {
            'employee_profiles': EmployeeNetPay.objects.all()
        }
        return render(request, "employee/net_salary.html", context)
