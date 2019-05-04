from django.db import models
#from django.contrib.gis.db import models as geomodels


class Event(models.Model):

	TO_BE_VALIDATED = 1
	VALIDATED = 2
	SOLVED = 3

	STATE_CHOICES = (
		(TO_BE_VALIDATED, 'To Be Validated'),
		(VALIDATED, 'Validated'),
		(SOLVED, 'Solved'),
	)

	CONSTRUCTION = 1
	SPECIAL_EVENT = 2
	INCIDENT = 3
	WEATHER_CONDITION = 4
	ROAD_CONDITION = 5

	CATEGORY_CHOICES = (
		(CONSTRUCTION, 'Construction'),
		(SPECIAL_EVENT, 'Special Event'),
		(INCIDENT, 'Incident'),
		(WEATHER_CONDITION, 'Weather Condition'),
		(ROAD_CONDITION, 'Road Condition'),
	)

	description = models.TextField(blank=False)
	#localization = geomodels.PointField()
	author = models.CharField(max_length=255, blank=False)
	creation_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	state = models.IntegerField(choices=STATE_CHOICES, default=TO_BE_VALIDATED, null=False)
	category = models.IntegerField(choices=CATEGORY_CHOICES, null=False)

	class Meta:
		ordering = ('-update_date',)