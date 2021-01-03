from django.db import models
import datetime
# Create your models here.


class BankList(models.Model):
    bank_code = models.CharField("銀行コード", max_length=100, blank=False, unique=True)
    bank_name = models.CharField("銀行名", max_length=100, blank=True, default='')

    def __str__(self):
        return self.bank_name


# 0:未払い 1:支払い済
class PaymentResult(models.Model):
    result_name = models.CharField("支払い状況", max_length=100, blank=True, default='未払い')
    result_status = models.IntegerField("支払い状況ステータス", default=0)

    def __str__(self):
        return self.result_name


class PaymentItem(models.Model):
    payment_data = models.DateField("決済月日", default=datetime.date.today)
    payment_name = models.CharField("支払い項目", max_length=100, blank=True, default='')
    payment_value = models.IntegerField("支払い額", default=0)
    bank = models.ForeignKey(to=BankList, on_delete=models.CASCADE, related_name='banks', default=1)
    result = models.ForeignKey(to=PaymentResult, on_delete=models.CASCADE, related_name='result', default=0)

    def __str__(self):
        return self.payment_name