# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170603_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'Student'), (1, 'Proffesor'), (2, 'Administration'), (3, 'ElectionComisioner')], default=2),
        ),
    ]
