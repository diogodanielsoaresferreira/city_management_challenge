from django.shortcuts import render
from event_management.models import Event
from rest_framework import viewsets
from event_management.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
