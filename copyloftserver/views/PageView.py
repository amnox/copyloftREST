from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from copyloftserver.models.models import Page
from copyloftserver.models.models import PageQuality
from copyloftserver.models.models import InkType
from copyloftserver.serializers.PageSerializer import PageListSerializer
from copyloftserver.serializers.PageSerializer import PageSingleSerializer
from copyloftserver.serializers.PageSerializer import PageQualitySerializer
from copyloftserver.serializers.PageSerializer import PageInkSerializer


class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer


class PageSingle(generics.RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSingleSerializer


class PageQualityList(generics.ListCreateAPIView):
    queryset = PageQuality.objects.all()
    serializer_class = PageQualitySerializer


class PageQualitySingle(generics.RetrieveUpdateAPIView):
    queryset = PageQuality.objects.all()
    serializer_class = PageQualitySerializer


class PageInkList(generics.ListCreateAPIView):
    queryset = InkType.objects.all()
    serializer_class = PageInkSerializer


class PageInkSingle(generics.RetrieveUpdateAPIView):
    queryset = InkType.objects.all()
    serializer_class = PageInkSerializer
