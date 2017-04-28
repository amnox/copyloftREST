from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from copyloftserver.models.models import Page
from copyloftserver.serializers.PageSerializer import PageListSerializer
from copyloftserver.serializers.PageSerializer import PageSingleSerializer

class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer

class PageSingle(generics.RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSingleSerializer