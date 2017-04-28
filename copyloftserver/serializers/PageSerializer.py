from copyloftserver.models.models import Page
from rest_framework import serializers

class PageListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Page
		fields = ('id', 'name', 'covers','size','cost')

class PageSingleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Page
		fields = ('id', 'name', 'covers','size','cost')