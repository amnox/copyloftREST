# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 16:46
from __future__ import unicode_literals

import copyloftserver.models.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copyloftserver', '0006_auto_20170427_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartbook',
            name='file',
            field=models.FileField(null=True, upload_to=copyloftserver.models.models.user_directory_path),
        ),
    ]
