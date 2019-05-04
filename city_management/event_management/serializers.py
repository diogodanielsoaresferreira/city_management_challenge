from rest_framework import serializers
from event_management.models import Event
from drf_extra_fields.geo_fields import PointField

class EventSerializer(serializers.HyperlinkedModelSerializer):
	location = PointField()

	class Meta:
		model = Event
		fields = ('id', 'description', 'author', 'state', 'category', 'creation_date', 'update_date', 'location',)

class EventOnlyStateSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Event
		fields = ('id', 'state',)
