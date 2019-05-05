import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from event_management.models import Event

class AddEventTests(APITestCase):

	def test_add_event_all_parameters(self):
		"""
		Add an event to the database with all parameters
		"""

		url = reverse('events')
		description = "des"
		category = "CON"
		author = "aut"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "category": category, "author": author, "location": location, "state": state}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)
		event = Event.objects.get()
		self.assertEqual(event.description, description)
		self.assertEqual(event.category, category)
		self.assertEqual(event.author, author)
		self.assertEqual(event.state, state)
		self.assertEqual(json.loads(event.location.json).get('coordinates')[0], json.loads(location).get('longitude'))
		self.assertEqual(json.loads(event.location.json).get('coordinates')[1], json.loads(location).get('latitude'))


	def test_add_event_without_state(self):
		"""
		Add an event to the database without the state optional parameter
		"""

		url = reverse('events')
		description = "des"
		category = "CON"
		author = "aut"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		default_state = "TBV"
		data = {"description": description, "category": category, "author": author, "location": location}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)
		event = Event.objects.get()
		self.assertEqual(event.description, description)
		self.assertEqual(event.category, category)
		self.assertEqual(event.author, author)
		self.assertEqual(event.state, default_state)
		self.assertEqual(json.loads(event.location.json).get('coordinates')[0], json.loads(location).get('longitude'))
		self.assertEqual(json.loads(event.location.json).get('coordinates')[1], json.loads(location).get('latitude'))


	def test_add_event_invalid_category(self):
		"""
		Add an event to the database with invalid category
		"""

		url = reverse('events')
		description = "des"
		category = "ABC"
		author = "aut"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		data = {"description": description, "category": category, "author": author, "location": location}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Event.objects.count(), 0)


	def test_add_event_invalid_state(self):
		"""
		Add an event to the database with invalid state
		"""

		url = reverse('events')
		description = "des"
		category = "CON"
		state = "ABC"
		author = "aut"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		data = {"description": description, "category": category, "author": author, "location": location, "state": state}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Event.objects.count(), 0)


	def test_add_event_invalid_location(self):
		"""
		Add an event to the database with invalid location
		"""

		url = reverse('events')
		description = "des"
		category = "CON"
		author = "aut"
		location = 'Rua da Pêga, Aveiro'
		default_state = "TBV"
		data = {"description": description, "category": category, "author": author, "location": location}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Event.objects.count(), 0)
		

	def test_add_event_without_description(self):
		"""
		Add an event to the database without description
		"""

		url = reverse('events')
		category = "CON"
		author = "aut"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		default_state = "TBV"
		data = {"category": category, "author": author, "location": location}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Event.objects.count(), 0)
		

	def test_add_event_without_location(self):
		"""
		Add an event to the database without location
		"""
		
		url = reverse('events')
		description = "des"
		category = "CON"
		author = "aut"
		state = "TBV"
		data = {"description": description, "category": category, "author": author, "state": state}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Event.objects.count(), 0)
		

	def test_add_event_without_author(self):
		"""
		Add an event to the database without author
		"""
		
		url = reverse('events')
		description = "des"
		category = "CON"
		author = "aut"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "category": category, "location": location, "state": state}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Event.objects.count(), 0)
		

	def test_add_event_without_category(self):
		"""
		Add an event to the database without category
		"""
		
		url = reverse('events')
		description = "des"
		category = "CON"
		author = "aut"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Event.objects.count(), 0)


class SearchEventTests(APITestCase):

	def test_get_all_events(self):
		pass
