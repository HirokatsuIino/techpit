from django.db import models
import datetime
# Create your models here.


class PaymentItem(models.Model):
    payment_data = models.DateField("決済月日", default=datetime.date.today)
    payment_name = models.CharField("支払い項目", max_length=100, blank=True, default='')
    payment_value = models.IntegerField("支払い額", default=0)
