# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 22:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment', models.NullBooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('payment_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('page_count', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cover_type', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='CoverBinding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cover_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.Cover')),
            ],
        ),
        migrations.CreateModel(
            name='InkType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('cart_book_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='copyloftserver.CartBook')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status_code', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('order_mapping_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copyloftserver.OrderMapping')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('covers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.Cover')),
            ],
        ),
        migrations.CreateModel(
            name='PageQuality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('page_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderPickupAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copyloftserver.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='ProviderVerification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copyloftserver.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('house', models.CharField(max_length=200)),
                ('street_1', models.CharField(max_length=200)),
                ('house_2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.PositiveSmallIntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copyloftserver.ServiceUser')),
            ],
        ),
        migrations.AddField(
            model_name='ordermapping',
            name='provider_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.Provider'),
        ),
        migrations.AddField(
            model_name='inktype',
            name='page_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.Page'),
        ),
        migrations.AddField(
            model_name='cartbook',
            name='binding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.CoverBinding'),
        ),
        migrations.AddField(
            model_name='cartbook',
            name='cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copyloftserver.Cart'),
        ),
        migrations.AddField(
            model_name='cartbook',
            name='cover_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.Cover'),
        ),
        migrations.AddField(
            model_name='cartbook',
            name='ink_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.InkType'),
        ),
        migrations.AddField(
            model_name='cartbook',
            name='page_quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.PageQuality'),
        ),
        migrations.AddField(
            model_name='cartbook',
            name='page_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='copyloftserver.Page'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copyloftserver.ServiceUser'),
        ),
    ]
