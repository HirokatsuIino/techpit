from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PaymentItem


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'paymentchart/index.html'

    def get_context_data(self, **kwargs):
        payment_list = PaymentItem.objects.all()
        params = {
            'payment_list': payment_list,
        }
        return params
