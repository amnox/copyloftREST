from copyloftserver.models.models import ServiceUser
from copyloftserver.models.models import UserAddress
from copyloftserver.models.models import Cart
from copyloftserver.models.models import CartBook
from copyloftserver.serializers.ServiceUserSerializer import ServiceUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from copyloftserver.serializers.ServiceUserSerializer import ServiceUserAddress
from copyloftserver.serializers.ServiceUserSerializer import UpdateServiceUserAddress
from copyloftserver.serializers.ServiceUserSerializer import CreateServiceUserCart
from copyloftserver.serializers.ServiceUserSerializer import GetServiceUserCart
from copyloftserver.serializers.ServiceUserSerializer import ConcludeServiceUserCart
from copyloftserver.serializers.ServiceUserSerializer import ServiceUserCartBookSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from django.core.exceptions import ValidationError
import pprint


class ServiceUserList(generics.ListCreateAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserSerializer


class ServiceUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserSerializer


class GetServiceUserAddress(generics.ListCreateAPIView):
    serializer_class = ServiceUserAddress

    def get_queryset(self):
        pprint.pprint(self.request.user)
        return UserAddress.objects.filter(user_id=self.kwargs['user_id'])


class UpdateServiceUserAddress(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateServiceUserAddress

    # queryset = UserAddress.objects.all()

    def get_queryset(self):
        return UserAddress.objects.filter(user_id=self.kwargs['user_id'])


class GetServiceUserCart(generics.RetrieveAPIView):
    # queryset = Cart.objects.all()
    serializer_class = GetServiceUserCart
    lookup_field = 'user_id'

    def get_queryset(self):
        return Cart.objects.filter(payment=False)


class CreateServiceUserCart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CreateServiceUserCart

    def perform_create(self, serializer):
        old_cart = Cart.objects.filter(user_id=self.kwargs['user_id']).filter(payment=False)
        if old_cart.exists():
            raise ValidationError('Cart Exists')
        serializer.save(user_id=ServiceUser.objects.get(pk=self.kwargs['user_id']))


class ConcludeServiceUserCart(generics.UpdateAPIView):
    # queryset = Cart.objects.all()
    serializer_class = ConcludeServiceUserCart
    lookup_field = 'user_id'

    def get_queryset(self):
        return Cart.objects.filter(payment=False).filter(user_id=self.kwargs['user_id'])

    def perform_update(self, serializer):
        pprint.pprint(serializer.validated_data)
        serializer.save()


class ServiceUserCartBooks(generics.ListCreateAPIView):
    serializer_class = ServiceUserCartBookSerializer
    queryset = CartBook.objects.all()


class ServiceUserCartBook(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceUserCartBookSerializer
    queryset = CartBook.objects.all()