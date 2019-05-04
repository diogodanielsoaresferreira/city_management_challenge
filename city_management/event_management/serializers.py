from rest_framework import serializers
from event_management.models import Event
from drf_extra_fields.geo_fields import PointField

class EventSerializer(serializers.HyperlinkedModelSerializer):
	localization = PointField()

	class Meta:
		model = Event
		fields = ('id', 'description', 'author', 'state', 'category', 'creation_date', 'update_date', 'localization',)

class EventOnlyStateSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Event
		fields = ('id', 'state',)
