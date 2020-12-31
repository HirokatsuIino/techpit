from .models import PaymentItem


def payment_list(request):
    payment_list = PaymentItem.objects.all()

    params = {
        'payment_list': payment_list,
    }

    return params
