# city_management_challenge

API for event management in a city. Each event has:
* description
* location
* author
* creation date
* update date
* state
* category

There are four endpoints available:
GET /v1/events/: Filter many events, by author, category and/or location (and radius)
POST /v1/events/: Add new events
GET /v1/events/{id}/: Get the information of one event
PUT /v1/events/{id}/: Update the state of an event

More information in the full API documentation: 0.0.0.0:8000/swagger/

To run the environment, install docker-compose and run docker-compose up.
