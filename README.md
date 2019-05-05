# City Management Challenge

API for event management in a city. Each event has:
* description
* location
* author
* creation date
* update date
* state
* category

There are four endpoints available:
* GET /v1/events/: Filter many events, by author, category and/or location (and radius)
* POST /v1/events/: Add new events
* GET /v1/events/{id}/: Get the information of one event
* PUT /v1/events/{id}/: Update the state of an event

More information in the full API documentation: 0.0.0.0:8000/swagger/

To run the environment, install docker-compose and run docker-compose up.

The tests can be found at city_management/event_management/tests.py.
To run the tests, go inside docker and run python3 manage.py test, or run this command outside docker (but first configure a local database).

