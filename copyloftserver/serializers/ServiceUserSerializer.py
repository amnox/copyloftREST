import magic
import inspect
from docx import Document
from pprint import pprint
import re
from rest_framework import serializers
from copyloftserver.models.models import ServiceUser
from copyloftserver.models.models import UserAddress
from copyloftserver.models.models import Cart
from copyloftserver.models.models import CartBook
from django.contrib.auth.models import User


from copyloftserver.serializers.UserSerializer import UserSerializer


class ServiceUserObject(serializers.RelatedField):
    def to_representation(self, value):
        return {'first_name': value.first_name, 'last_name': value.last_name, 'email': value.email}


class ServiceUserSerializer(serializers.ModelSerializer):
    # user = ServiceUserObject(read_only=`False`)
    # user = UserSerializer(many=False, read_only=False)
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = ServiceUser
        fields = ('user', 'phone', 'date_joined')

    def create(self, validated_data):
        user = User(
            username=validated_data['user']['username'],
            password=validated_data['user']['password'],
            email=validated_data['user']['email'],
            first_name=validated_data['user']['first_name'],
            last_name=validated_data['user']['last_name']
        )
        user.save()
        serviceuser = ServiceUser(user=user, phone=validated_data['phone'])
        serviceuser.save()
        return serviceuser


class ServiceUserAddress(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('id', 'user_id', 'house', 'street_1', 'house_2', 'city', 'state', 'pincode')


class UpdateServiceUserAddress(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = UserAddress
        fields = ('id', 'user_id', 'house', 'street_1', 'house_2', 'city', 'state', 'pincode')


class CreateServiceUserCart(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user_id', 'payment', 'date', 'payment_date')


class GetServiceUserCart(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user_id', 'payment', 'date', 'payment_date')


class ConcludeServiceUserCart(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Cart
        fields = ('user_id', 'payment', 'payment_date')

    def validate_payment(self, value):
        if value in [False, None]:
            raise serializers.ValidationError("Conclude the cart naiqua")
        return value

    def validate_payment_date(self, value):
        if value in [None]:
            raise serializers.ValidationError("Enter a date naiqua")
        return value


class ServiceUserCartBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartBook
        fields = ('id',
                  'cart_id',
                  'file',
                  'page_count',
                  'page_size',
                  'page_quality',
                  'ink_type',
                  'cover_id',
                  'binding',
                  'price',
                  'commercial_page',)
