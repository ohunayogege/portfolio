# Generated by Django 3.1.1 on 2020-09-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20200923_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentcode',
            name='email',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
    ]