# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceUser(models.Model):
	#User Table
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.BigIntegerField()
	date_joined = models.DateField(auto_now_add=True)

class UserAddress(models.Model):
	#Saved User Addresses
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey('ServiceUser',on_delete=models.CASCADE,)
	house = models.CharField(max_length=200)
	street_1 = models.CharField(max_length=200)
	house_2 = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	pincode = models.PositiveSmallIntegerField()

class Cart(models.Model):
	#User Cart
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey('ServiceUser',on_delete=models.CASCADE,)
	payment = models.NullBooleanField()
	date = models.DateField(auto_now_add=True)
	payment_date = models.DateField(null=True)


class CartBook(models.Model):
	#List of books in a cart
	id = models.AutoField(primary_key=True)
	cart_id = models.ForeignKey('Cart',on_delete=models.CASCADE,)
	page_count = models.PositiveSmallIntegerField()
	page_size = models.ForeignKey('Page',on_delete=models.PROTECT,)
	page_quality = models.ForeignKey('PageQuality',on_delete=models.PROTECT,)
	ink_type = models.ForeignKey('InkType',on_delete=models.PROTECT,)
	cover_id = models.ForeignKey('Cover',on_delete=models.PROTECT,)
	binding = models.ForeignKey('CoverBinding',on_delete=models.PROTECT,)
	price = models.DecimalField(max_digits=5, decimal_places=2)

class OrderMapping(models.Model):
	#Order map for each book
	id = models.AutoField(primary_key=True)
	cart_book_id = models.OneToOneField(CartBook,on_delete = models.CASCADE)
	date = models.DateField(auto_now_add=True)
	provider_id = models.ForeignKey('Provider',on_delete=models.PROTECT,)

class OrderStatus(models.Model):
	#Status Logs of each order
	id = models.AutoField(primary_key=True)
	order_mapping_id = models.ForeignKey('OrderMapping',on_delete=models.CASCADE,)
	status_code = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	date = models.DateField(auto_now_add=True)

class Provider(models.Model):
	#Print Service Provider Details
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	business_name = models.CharField(max_length=200)
	phone = models.BigIntegerField()
	address_line_1 = models.CharField(max_length=200)
	address_line_2 = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	pincode = models.CharField(max_length=200)

class ProviderVerification(models.Model):
	#Provider Verification Documents
	id = models.AutoField(primary_key=True)
	provider_id = models.ForeignKey('Provider',on_delete=models.CASCADE,)

class ProviderPickupAddress(models.Model):
	#Provider Wherehouse Location
	id = models.AutoField(primary_key=True)
	provider_id = models.ForeignKey('Provider',on_delete=models.CASCADE,)

class Cover(models.Model):
	#Available Covers
	id = models.AutoField(primary_key=True)
	cover_type = models.CharField(max_length=200)
	cost = models.DecimalField(max_digits=5, decimal_places=2)
	
class CoverBinding(models.Model):
	#Available Binding Types
	id = models.AutoField(primary_key=True)
	cost = models.DecimalField(max_digits=5, decimal_places=2)
	cover_id = models.ForeignKey('Cover',on_delete=models.PROTECT,)

class Page(models.Model):
	#Page types
	id = models.AutoField(primary_key=True)
	covers = models.ForeignKey('Cover',on_delete=models.PROTECT,)
	size = models.CharField(max_length=200)
	cost = models.DecimalField(max_digits=5, decimal_places=2)

class PageQuality(models.Model):
	#Page quality
	id = models.AutoField(primary_key=True)
	page_id = models.ForeignKey('Page',on_delete=models.PROTECT,)

class InkType(models.Model):
	#ink to be used
	id = models.AutoField(primary_key=True)
	page_id = models.ForeignKey('Page',on_delete=models.PROTECT,)