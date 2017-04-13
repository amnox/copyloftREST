from django.contrib.auth.models import User
from copyloftserver.serializers.UserSerializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
