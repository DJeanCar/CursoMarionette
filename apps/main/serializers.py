from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name")


class EventListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = ("id", "name", "address", "image")


class EventDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event