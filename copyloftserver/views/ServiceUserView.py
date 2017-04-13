from copyloftserver.models.models import ServiceUser
from copyloftserver.serializers.ServiceUserSerializer import ServiceUserSerializer
from rest_framework.decorators import api_view
from rest_framework import generics


class ServiceUserList(generics.ListCreateAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserSerializer
