from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Company
from .models import Fstatement
from django.views.generic.list import MultipleObjectMixin


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


class CompanyView(DetailView, MultipleObjectMixin):
    model = Company
    paginate_by = 4

    def get_context_data(self, **kwargs):
        object_list = Fstatement.objects.filter(company=kwargs['object']).order_by('-fiscal_year')
        context = super(CompanyView, self).get_context_data(object_list=object_list, **kwargs)

        return context

class FstatementView(DetailView):
    model = Fstatement
