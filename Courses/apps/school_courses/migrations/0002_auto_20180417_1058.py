# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='courses',
        ),
        migrations.AddField(
            model_name='description',
            name='course',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='school_courses.Course'),
            preserve_default=False,
        ),
    ]
