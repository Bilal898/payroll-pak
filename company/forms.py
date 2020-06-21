from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    company_email = forms.EmailField()

    class Meta:
        model = Company
        fields = ["company_name",
                  "company_address",
                  "company_phone",
                  "company_email"
                  ]

    # def clean_company_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("company_email")
    #     if not email.endswith("com"):
    #         raise forms.ValidationError("not a valid email")
    #     return email
