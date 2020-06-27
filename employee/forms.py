from django.forms import ModelForm
from .models import EmployeePayrollProfile


class PayProfileForm(ModelForm):

    class Meta:
        model = EmployeePayrollProfile
        fields = '__all__'
