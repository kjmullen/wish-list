# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_list_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='stripe_token',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
