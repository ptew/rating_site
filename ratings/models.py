from django.db import models
from django.utils import timezone
import datetime

class Profile(models.Model):
	profile_number = models.IntegerField(default=0)
	rep = models.IntegerField(default=0)
	status = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.profile_number)

class Advice(models.Model):
	company = models.CharField(max_length=20)
	ticker = models.CharField(max_length=20)
	content = models.TextField()
	price_target = models.FloatField(default=0)
	time_frame = models.IntegerField(default=0)

	def __unicode__(self):
		return self.company

class User(models.Model):
	user_id = models.IntegerField(default=0)
	participation_timestamp = models.DateTimeField('date published')

class Vote(models.Model):
	profile = models.ForeignKey(Profile)
	advice = models.ForeignKey(Advice)
	user = models.ForeignKey(User)
	value = models.IntegerField(default=0)
	timestamp = models.DateTimeField('date published')
	is_performance = models.BooleanField()
	is_submission = models.BooleanField()

class QualityVote(models.Model):
	profile = models.ForeignKey(Profile)
	advice = models.ForeignKey(Advice)
	user = models.ForeignKey(User)
	value = models.IntegerField(default=0)
	timestamp = models.DateTimeField('date published')

class PerformanceVote(models.Model):
	profile = models.ForeignKey(Profile)
	advice = models.ForeignKey(Advice)
	user = models.ForeignKey(User)
	value = models.IntegerField(default=0)
	timestamp = models.DateTimeField('date published')

class UserConnection(models.Model):
	user = models.ForeignKey(User)
	world_number = models.IntegerField(default=0)

class World(models.Model):
	world_number = models.IntegerField(default=0)
	advice = models.ForeignKey(Advice)
	profile = models.ForeignKey(Profile)