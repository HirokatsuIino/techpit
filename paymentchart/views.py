from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import ListView
from .models import PaymentItem
from .forms import PaymentItemForm
from django.views.generic.edit import ModelFormMixin


# Create your views here.
class PaymentItemListView(ListView):
    model = PaymentItem
    # form_class = PaymentItemForm
    # template_name = 'paymentchart/paymentitem_list.html'

    def get_context_data(self, **kwargs):
        payment_list = PaymentItem.objects.all()
        params = {
            'payment_list': payment_list,
        }
        return params

    # def form_valid(self, form):
    #     result = form.save(commit=False)
    #     result.payment_name = self.get_object()
    #     result.payment_value = self.get_object()
    #     result.save()
    #     return HttpResponseRedirect(self.request.path_info)
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         self.object = self.get_object()
    #         return self.form_invalid(form)
