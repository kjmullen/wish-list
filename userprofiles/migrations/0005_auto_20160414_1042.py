# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_auto_20160414_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.UserProfile'),
        ),
    ]
