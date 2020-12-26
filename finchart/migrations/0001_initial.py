# Generated by Django 2.0 on 2020-12-26 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='会社名')),
            ],
        ),
        migrations.CreateModel(
            name='Fstatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiscal_year', models.DateField(verbose_name='決算日')),
                ('bs_current_assets', models.IntegerField(default=0, verbose_name='流動資産（百万円）')),
                ('bs_fixed_assets', models.IntegerField(default=0, verbose_name='固定資産（百万円）')),
                ('bs_deferred_assets', models.IntegerField(default=0, verbose_name='繰延資産（百万円）')),
                ('bs_current_liabilities', models.IntegerField(default=0, verbose_name='流動負債（百万円）')),
                ('bs_fixed_liabilities', models.IntegerField(default=0, verbose_name='固定負債（百万円）')),
                ('bs_net_assets', models.IntegerField(default=0, verbose_name='純資産（百万円）')),
                ('pl_gross_sales', models.IntegerField(default=0, verbose_name='総売上（百万円）')),
                ('pl_gross_profit', models.IntegerField(default=0, verbose_name='売上総利益（百万円）')),
                ('pl_operating_profit', models.IntegerField(default=0, verbose_name='営業利益（百万円）')),
                ('pl_ordinary_income', models.IntegerField(default=0, verbose_name='経常利益（百万円）')),
                ('pl_income_before_tax', models.IntegerField(default=0, verbose_name='税引前当期純利益（百万円）')),
                ('pl_net_income', models.IntegerField(default=0, verbose_name='当期純利益（百万円）')),
                ('cf_operating', models.IntegerField(default=0, verbose_name='営業ＣＦ（百万円）')),
                ('cf_investment', models.IntegerField(default=0, verbose_name='投資ＣＦ（百万円）')),
                ('cf_finance', models.IntegerField(default=0, verbose_name='財務ＣＦ（百万円）')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finchart.Company')),
            ],
        ),
    ]
