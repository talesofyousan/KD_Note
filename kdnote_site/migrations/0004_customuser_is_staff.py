# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kdnote_site', '0003_auto_20171230_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
