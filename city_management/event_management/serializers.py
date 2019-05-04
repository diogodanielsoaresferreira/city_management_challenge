from rest_framework import serializers
from event_management.models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Event
		fields = ('id', 'description', 'author', 'state', 'category', 'creation_date', 'update_date')

class EventOnlyStateSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Event
		fields = ('id', 'state',)
