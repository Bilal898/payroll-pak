from tax_formula.models import TaxSlabs2019
from django.db.models import Q


class PayCalculator():

    def __init__(self, monthly_salary=0, med_allw=0, yearly_salary=0):
        self.monthly_salary = int(monthly_salary)
        self.yearly_salary = int(monthly_salary) * 12
        self.med_allw = int(med_allw)

    def find_slab(self):
        print("yearly", self.yearly_salary)
        try:
            slab = TaxSlabs2019.objects.filter(
                slab__gt=self.yearly_salary
            )[0]
            print("slab is: ", slab)
        except:
            print("slab not found")

        # print("slab", slab)
        # return slab
