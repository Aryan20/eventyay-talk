# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-23 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0015_auto_20170419_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='do_not_record',
            field=models.BooleanField(default=False, verbose_name='Don\'t record my talk.'),
        ),
    ]
