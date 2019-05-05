from event_management.models import Event
from event_management.serializers import EventSerializer, EventOnlyStateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from ast import literal_eval
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class EventList(APIView):
	"""
	get:
	Returns a list with all events. Supports query filtering by author, category or location (point or point and radius).

	post:
	Creates a new event.
	"""


	@swagger_auto_schema(manual_parameters=[
		openapi.Parameter('author', openapi.IN_QUERY,  type=openapi.TYPE_STRING, required=False, description="Author of the event"),
		openapi.Parameter('category', openapi.IN_QUERY,  type=openapi.TYPE_STRING, required=False, enum=["CON", "SPE", "INC", "WEC", "ROC"], description="Category of the event: 'CON' - Construction, 'SPE' - Special Event, 'INC' - Incident, 'WEC' - Weather Condition, 'ROC' - Road Condition."),
		openapi.Parameter('location', openapi.IN_QUERY,  type=openapi.TYPE_STRING, required=False, description="Json string with latitude and longitude of the point to search around  (e.g. {'latitude': 37.8, 'longitude': -9.5})"),
		openapi.Parameter('radius', openapi.IN_QUERY,  type=openapi.TYPE_NUMBER, required=False, description="Radius (in Km) to search around. If not location is specified but radius is not specified, it will be assumed radius=5")
		], 
		responses={200: EventSerializer(many=True)})
	def get(self, request, format=None):
		event = Event.objects.all()

		author = self.request.query_params.get('author', None)
		if author is not None:
			event = event.filter(author__iexact=author)

		category = self.request.query_params.get('category', None)
		if category is not None:
			event = event.filter(category__iexact=category)

		location = self.request.query_params.get('location', None)
		
		if location is not None:
			try:
				location_dict = literal_eval(location)
				
				latitude = location_dict["latitude"]
				longitude = location_dict["longitude"]

				radius = self.request.query_params.get('radius', None)
				
				try:
					radius = float(radius)
				except Exception as e:
					pass

				if radius is None or not isinstance(radius, float): 
					radius = 5

				point = Point(longitude, latitude)
				event = event.filter(location__distance_lt=(point, Distance(km=radius)))
			except Exception as e:
				pass

		serializer = EventSerializer(event, many=True)
		return Response(serializer.data)

	@swagger_auto_schema(
		request_body=EventSerializer,
		responses={201: EventSerializer(many=True)})
	def post(self, request, format=None):
		serializer = EventSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EventDetail(APIView):
	"""
	get:
	Retrieves an event with the required id.

	put:
	Updates the state of an event.
	"""

	def get_object(self, pk):
		try:
			return Event.objects.get(pk=pk)
		except Event.DoesNotExist:
			raise Http404

	@swagger_auto_schema(manual_parameters=[
		openapi.Parameter('id', openapi.IN_PATH,  type=openapi.TYPE_INTEGER, description="Id of the event"),
		],
		responses={200: EventSerializer, 404: "{'detail': 'Not found'}"})
	def get(self, request, pk, format=None):
		event = self.get_object(pk)
		serializer = EventSerializer(event)
		return Response(serializer.data)

	@swagger_auto_schema(manual_parameters=[
		openapi.Parameter('id', openapi.IN_PATH,  type=openapi.TYPE_INTEGER, description="Id of the event"),
		],
		request_body=EventOnlyStateSerializer,
		responses={200: EventOnlyStateSerializer, 404: "{'detail': 'Not found'}"})
	def put(self, request, pk, format=None):
		event = self.get_object(pk)
		serializer = EventOnlyStateSerializer(event, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		