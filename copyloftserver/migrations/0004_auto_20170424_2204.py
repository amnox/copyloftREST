# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copyloftserver', '0003_auto_20170416_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbook',
            name='binding',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.CoverBinding'),
        ),
        migrations.AlterField(
            model_name='cartbook',
            name='cover_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.Cover'),
        ),
    ]