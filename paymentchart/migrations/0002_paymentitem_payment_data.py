# Generated by Django 2.0 on 2020-12-31 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentchart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentitem',
            name='payment_data',
            field=models.DateField(default=datetime.date.today, verbose_name='決済月日'),
        ),
    ]