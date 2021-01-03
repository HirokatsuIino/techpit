from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import PaymentItem
from .forms import PaymentItemForm
from django.views.generic.edit import ModelFormMixin


# Create your views here.
class PaymentItemListView(generic.ListView):
    model = PaymentItem
    # form_class = PaymentItemForm
    # template_name = 'paymentchart/paymentitem_list.html'

    def get_context_data(self, **kwargs):
        payment_list = PaymentItem.objects.all().order_by('-payment_data')
        groupby_bank = PaymentItem.objects.values('bank__bank_code', 'bank__bank_name').annotate(
            total=Sum('payment_value'),
        ).order_by('bank__bank_code').reverse()

        params = {
            'payment_list': payment_list,
            'groupby_bank': groupby_bank,
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


class PaymentItemDetail(generic.DetailView):
    model = PaymentItem
    # template_name = 'amazon/item_detail.html'

    def get_context_data(self, **kwargs):
        object_list = PaymentItem.objects.filter(bank__id=self.kwargs['pk'])
        bank_name = PaymentItem.objects.values_list('bank__bank_name', flat=True).filter(bank__id=self.kwargs['pk']).first()
        params = {
            'object_list': object_list,
            'bank_name': bank_name,
        }
        return params


class PaymentItemCreateView(generic.CreateView):
    model = PaymentItem
    form_class = PaymentItemForm
    # template_name = 'paymentchart/paymentitem_detail.html'

    def form_valid(self, form):
        review = form.save(commit=False)
        print(review)
        print('def form_valid')
        # review.product = self.get_object()
        # review.save()
        return HttpResponseRedirect(self.request.path_info)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(form)
        print('def post')
        if form.is_valid():
            print('if form.is_valid():')
            return self.form_valid(form)
        else:
            print('else')
            self.object = self.get_object()
            print(self.object)
            return self.form_invalid(form)

