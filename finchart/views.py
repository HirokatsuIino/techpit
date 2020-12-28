from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Company
from .models import Fstatement


# class IndexTemplateView(TemplateView):
#     template_name = 'finchart/index.html'

class IndexView(TemplateView):
    template_name = 'finchart/index.html'

    def get_context_data(self, **kwargs):
        fstatement_list = Fstatement.objects.all().order_by('company')
        params = {
            'fstatement_list': fstatement_list,
        }
        return params


class CompanyView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        company_name = kwargs['object'].name
        fstatement_list = Fstatement.objects.filter(company=kwargs['object']).order_by('-fiscal_year')[:4]
        params = {
            'company_name': company_name,
            'fstatement_list': fstatement_list,
        }
        return params