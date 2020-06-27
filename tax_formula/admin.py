from django.contrib import admin
from .models import TaxSlabs2019
# Register your models here.


class InLineTaxSlabs2019(admin.StackedInline):
    model = TaxSlabs2019
    extra = 3


class TaxSlabs2019Admin(admin.ModelAdmin):
    list_display = ('slab', 'slab_basic_deduction',
                    'slab_percentage_deduction')


admin.site.register(TaxSlabs2019, TaxSlabs2019Admin)
