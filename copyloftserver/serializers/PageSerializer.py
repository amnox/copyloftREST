from copyloftserver.models.models import Page
from copyloftserver.models.models import InkType
from copyloftserver.models.models import PageQuality
from rest_framework import serializers


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'name', 'covers', 'size', 'cost')


class PageSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'name', 'covers', 'size', 'cost')


class PageQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PageQuality
        fields = ('id', 'name', 'cost', 'page_id')


class PageInkSerializer(serializers.ModelSerializer):
    class Meta:
        model = InkType
        fields = ('id', 'name', 'cost', 'page_id')
