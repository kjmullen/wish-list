# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20160414_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='expired',
        ),
    ]