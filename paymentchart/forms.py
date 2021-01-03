from django import forms
from .models import PaymentItem


class PaymentItemForm(forms.ModelForm):
    class Meta:
        model = PaymentItem
        fields = ('payment_data', 'payment_name', 'payment_value', 'bank', 'result',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            print(self.fields.values())
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
