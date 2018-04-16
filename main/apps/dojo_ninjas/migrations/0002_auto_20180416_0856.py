# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas.Dojo'),
        ),
    ]
