from rest_framework import serializers
from event_management.models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('description', 'author')