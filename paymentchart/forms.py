from django import forms
from .models import PaymentItem


class PaymentItemForm(forms.ModelForm):
    class Meta:
        model = PaymentItem
        fields = ('payment_data', 'payment_name', 'payment_value', 'bank', 'result',)

    def clean_payment_data(self):
        p_data = self.cleaned_data.get('payment_data')
        return p_data

    def clean_payment_name(self):
        p_name = self.cleaned_data.get('payment_name')
        if p_name == '':
            raise forms.ValidationError('入力してください。')
        else:
            return p_name

    def clean_payment_value(self):
        p_value = self.cleaned_data.get('payment_value')
        return p_value

    def clean_bank(self):
        p_bank = self.cleaned_data.get('bank')
        return p_bank

    def clean_result(self):
        p_result = self.cleaned_data.get('result')
        return p_result

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
