from event_management.models import Event
from event_management.serializers import EventSerializer, EventOnlyStateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from ast import literal_eval


class EventList(APIView):
	"""
	List all events or create a new event
	"""

	def get(self, request, format=None):
		event = Event.objects.all()

		author = self.request.query_params.get('author', None)
		if author is not None:
			event = event.filter(author__iexact=author)

		category = self.request.query_params.get('category', None)
		if category is not None:
			event = event.filter(category__iexact=category)

		localization = self.request.query_params.get('localization', None)
		
		if localization is not None:
			try:
				localization_dict = literal_eval(localization)
				
				latitude = localization_dict["latitude"]
				longitude = localization_dict["longitude"]

				radius = self.request.query_params.get('radius', None)
				
				try:
					radius = float(radius)
				except Exception as e:
					pass

				if radius is None or not isinstance(radius, float): 
					radius = 5

				point = Point(longitude, latitude)
				event = event.filter(localization__distance_lt=(point, Distance(km=radius)))
			except Exception as e:
				pass

		serializer = EventSerializer(event, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = EventSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EventDetail(APIView):
	"""
	Retrieve or update an event
	"""

	def get_object(self, pk):
		try:
			return Event.objects.get(pk=pk)
		except Event.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		event = self.get_object(pk)
		serializer = EventSerializer(event)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		event = self.get_object(pk)
		serializer = EventOnlyStateSerializer(event, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		