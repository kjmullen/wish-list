# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0005_auto_20160414_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
