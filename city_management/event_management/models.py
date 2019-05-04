from django.db import models
#from django.contrib.gis.db import models as geomodels


class Event(models.Model):

	TO_BE_VALIDATED = "TBV"
	VALIDATED = "VAL"
	SOLVED = "SOL"

	STATE_CHOICES = (
		(TO_BE_VALIDATED, 'To Be Validated'),
		(VALIDATED, 'Validated'),
		(SOLVED, 'Solved'),
	)

	CONSTRUCTION = "CON"
	SPECIAL_EVENT = "SPE"
	INCIDENT = "INC"
	WEATHER_CONDITION = "WEC"
	ROAD_CONDITION = "ROC"

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
	state = models.CharField(choices=STATE_CHOICES, default=TO_BE_VALIDATED, max_length=3)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=3, null=False)

	class Meta:
		ordering = ('-update_date',)