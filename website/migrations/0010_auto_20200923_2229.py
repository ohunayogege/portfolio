# Generated by Django 3.1.1 on 2020-09-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_paymentcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcode',
            name='code',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]