from rest_framework import serializers
from copyloftserver.models.models import ServiceUser
from django.contrib.auth.models import User

class ServiceUserObject(serializers.RelatedField):
	def to_representation(self, value):
		return {'first_name':value.first_name,'last_name':value.last_name,'email':value.email}

class ServiceUserSerializer(serializers.ModelSerializer):
	#user = ServiceUserObject(read_only=`True`)
	class Meta:
		model = ServiceUser
		fields = ('user', 'phone', 'date_joined')
