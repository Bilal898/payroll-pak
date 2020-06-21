from django.shortcuts import render

# Create your views here.


def employee_create_view(request):
    return render(request, "employee/employee_create.html")
