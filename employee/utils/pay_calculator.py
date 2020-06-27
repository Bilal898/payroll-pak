from tax_formula.models import TaxSlabs2019
from django.db.models import Q


class PayCalculator(monthly_salary=0, med_allw=0):

    def __init__(self, monthly_salary=0, med_allw=0):
        self.monthly_salary = monthly_salary
        self.yearly_salary = self.monthly_salary * 12
        self.med_allw = med_allw

    def find_slab(self):
        slab = TaxSlabs2019.objects.filter(
            slab__gt=self.yearly_salary
        )[0]
        return slab
