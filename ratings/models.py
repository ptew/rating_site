from django.db import models
from django.utils import timezone
import datetime
		
class Advice(models.Model):
	company = models.CharField(max_length=20)
	ticker = models.CharField(max_length=20)
	content = models.TextField()
	vote_count = models.IntegerField(default=0)
	view_count = models.IntegerField(default=0)
	price_target = models.FloatField(default=0)
	time_frame = models.IntegerField(default=0)

	def __unicode__(self):
		return self.company

class Profile(models.Model):
	world = models.IntegerField(default=0)
	vote_count = models.IntegerField(default=0)
	pieces_of_advice = models.ManyToManyField(Advice, through="Connection")

	def __unicode__(self):
		return str(self.world)

class Connection(models.Model):
	profile = models.ForeignKey(Profile)
	advice = models.ForeignKey(Advice)
	vote_count = models.IntegerField(default=0)
	rating_sum = models.IntegerField(default=0)

class User(models.Model):
	user_id = models.IntegerField(default=0)
	participation_timestamp = models.DateTimeField('date published')
	view_count = models.IntegerField(default=0)
	vote_count = models.IntegerField(default=0)






