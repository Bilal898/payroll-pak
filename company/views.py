from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company
# Create your views here.


def company_create_view(request, *args, **kwargs):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {'company_name': request.POST['company_name']}
        # context = {'company_data': request.POST}
        # print(context)
        return redirect(request, "company/company_dashboard.html", context)
        form = CompanyForm(request.POST or None)
    # else:
    #     print(form.errors)
    context = {
        'form': form
    }

    return render(request, "company/company_create.html", context)


def company_dashboard_view(request, *args, **kwargs):
    return render("company/company_dashboard.html")
