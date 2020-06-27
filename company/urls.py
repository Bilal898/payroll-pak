from django.urls import path
from .views import company_create_view, company_dashboard_view

app_name = 'company'
urlpatterns = [
    path('create/', company_create_view, name="company_create"),
    path('', company_dashboard_view, name="company_dashboard"),
]
