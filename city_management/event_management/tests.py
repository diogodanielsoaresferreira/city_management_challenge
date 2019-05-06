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
		"""
		Retrieve all events in the database
		"""
		url = reverse('events')
		
		description = "des1"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		description = "des3"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 41.0625, "longitude": 0.677068}'
		state = "VAL"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_2 = self.client.post(url, data, format='json')

		self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 2)

		description = "des3"
		category = "CON"
		author = "aut2"
		location = '{"latitude": 38.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_3 = self.client.post(url, data, format='json')

		self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 3)

		response_4 = self.client.get(url, format='json')
		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual(len(content), 3)


	def test_get_event_by_author(self):
		"""
		Retrieve events in the database by author
		"""
		url = reverse('events')
		
		description = "des1"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		description = "des3"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 41.0625, "longitude": 0.677068}'
		state = "VAL"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_2 = self.client.post(url, data, format='json')

		self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 2)

		description = "des3"
		category = "CON"
		author = "aut2"
		location = '{"latitude": 38.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_3 = self.client.post(url, data, format='json')

		self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 3)

		query = {'author': 'aut1'}
		response_4 = self.client.get(url, query, format='json')
		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual(len(content), 2)

		
	def test_get_event_by_category(self):
		"""
		Retrieve events in the database by category
		"""
		url = reverse('events')
		
		description = "des1"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		description = "des3"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 41.0625, "longitude": 0.677068}'
		state = "VAL"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_2 = self.client.post(url, data, format='json')

		self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 2)

		description = "des3"
		category = "SPE"
		author = "aut2"
		location = '{"latitude": 38.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_3 = self.client.post(url, data, format='json')

		self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 3)

		query = {'category': 'SPE'}
		response_4 = self.client.get(url, query, format='json')
		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual(len(content), 1)


	def test_get_event_by_author_and_category(self):
		"""
		Retrieve events in the database by author and category
		"""
		url = reverse('events')
		
		description = "des1"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		description = "des3"
		category = "CON"
		author = "aut2"
		location = '{"latitude": 41.0625, "longitude": 0.677068}'
		state = "VAL"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_2 = self.client.post(url, data, format='json')

		self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 2)

		description = "des3"
		category = "SPE"
		author = "aut2"
		location = '{"latitude": 38.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_3 = self.client.post(url, data, format='json')

		self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 3)

		query = {'category': 'CON' ,'author': 'aut2'}
		response_4 = self.client.get(url, query, format='json')
		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual(len(content), 1)


	def test_get_event_by_location(self):
		"""
		Retrieve events in the database by location
		"""
		url = reverse('events')
		
		description = "des1"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		description = "des3"
		category = "CON"
		author = "aut2"
		location = '{"latitude": 41.0625, "longitude": 0.677068}'
		state = "VAL"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_2 = self.client.post(url, data, format='json')

		self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 2)

		description = "des3"
		category = "SPE"
		author = "aut2"
		location = '{"latitude": 38.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_3 = self.client.post(url, data, format='json')

		self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 3)

		query = {'location': '{"latitude": 41.06, "longitude": 0.67}'}
		response_4 = self.client.get(url, query, format='json')
		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual(len(content), 1)


	def test_get_event_by_location_not_found(self):
		"""
		Retrieve events in the database by location, test if it does not return any
		"""
		url = reverse('events')
		
		description = "des1"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		description = "des3"
		category = "CON"
		author = "aut2"
		location = '{"latitude": 41.0625, "longitude": 0.677068}'
		state = "VAL"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_2 = self.client.post(url, data, format='json')

		self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 2)

		description = "des3"
		category = "SPE"
		author = "aut2"
		location = '{"latitude": 38.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_3 = self.client.post(url, data, format='json')

		self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 3)

		query = {'location': '{"latitude": 40.0, "longitude": 0.0}'}
		response_4 = self.client.get(url, query, format='json')
		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual(len(content), 0)


	def test_get_event_by_location_and_radius(self):
		"""
		Retrieve events in the database by location and radius
		"""
		url = reverse('events')
		
		description = "des1"
		category = "CON"
		author = "aut1"
		location = '{"latitude": 37.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		description = "des3"
		category = "CON"
		author = "aut2"
		location = '{"latitude": 41.0625, "longitude": 0.677068}'
		state = "VAL"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_2 = self.client.post(url, data, format='json')

		self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 2)

		description = "des3"
		category = "SPE"
		author = "aut2"
		location = '{"latitude": 38.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_3 = self.client.post(url, data, format='json')

		self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 3)

		query = {'location': '{"latitude": 40.0, "longitude": 0.0}', 'radius': '1000'}
		response_4 = self.client.get(url, query, format='json')
		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual(len(content), 1)


	def test_get_one_event(self):
		"""
		Retrieve event in the database by id
		"""
		url = reverse('events')
		
		description_1 = "des1"
		category_1 = "CON"
		author_1 = "aut1"
		location_1 = '{"latitude": 37.0625, "longitude": -95.677068}'
		state_1 = "TBV"
		data = {"description": description_1, "author": author_1, "location": location_1, "state": state_1, "category": category_1}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		description = "des3"
		category = "CON"
		author = "aut2"
		location = '{"latitude": 41.0625, "longitude": 0.677068}'
		state = "VAL"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_2 = self.client.post(url, data, format='json')

		self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 2)

		description = "des3"
		category = "SPE"
		author = "aut2"
		location = '{"latitude": 38.0625, "longitude": -95.677068}'
		state = "TBV"
		data = {"description": description, "author": author, "location": location, "state": state, "category": category}
		response_3 = self.client.post(url, data, format='json')

		self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 3)


		path_parameter = {'pk': response_1.json()["id"]}
		url = reverse('event', kwargs=path_parameter)
		response_4 = self.client.get(url, format='json')
		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual(content["id"], response_1.json()["id"])
		self.assertEqual(content["description"], description_1)
		self.assertEqual(content["author"], author_1)
		self.assertEqual(json.dumps(content["location"]), location_1)
		self.assertEqual(content["state"], state_1)
		self.assertEqual(content["category"], category_1)


class UpdateEventState(APITestCase):
	
	def test_update_event_state(self):
		"""
		Update state of event in the database
		"""
		url = reverse('events')
		
		description_1 = "des1"
		category_1 = "CON"
		author_1 = "aut1"
		location_1 = '{"latitude": 37.0625, "longitude": -95.677068}'
		state_1 = "TBV"
		data = {"description": description_1, "author": author_1, "location": location_1, "state": state_1, "category": category_1}
		response_1 = self.client.post(url, data, format='json')

		self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Event.objects.count(), 1)

		path_parameter = {'pk': response_1.json()["id"]}
		url = reverse('event', kwargs=path_parameter)
		data = {'state': 'VAL'}
		response_4 = self.client.put(url, data, format='json')

		self.assertEqual(response_4.status_code, status.HTTP_200_OK)
		content = response_4.json()
		self.assertEqual("VAL", response_4.json()["state"])

