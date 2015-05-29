from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import EventListSerializer, EventDetailSerializer
from .models import Event

class EventViewSet(viewsets.ViewSet):

	queryset = Event.objects.all()

	def list(self, request):
		"""
		Solo si es usuario muestra toda la lista
		"""
		events = Event.objects.all()
		serializer = EventListSerializer(events, many=True, context={'request': request})
		return Response(serializer.data)
		
	def retrieve(self, request, pk):
		"""
		Muestra el detalle de un articulo
		"""
		events = Event.objects.get(id = pk)
		serializer = EventDetailSerializer(events, context={'request': request})
		return Response(serializer.data)