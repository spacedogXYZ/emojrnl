# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20160514_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='txt',
            field=models.CharField(max_length=5),
        ),
    ]
