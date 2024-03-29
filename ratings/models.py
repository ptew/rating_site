from django.db import models
from django.utils import timezone
import datetime

class Profile(models.Model):
	profile_number = models.IntegerField(default=0)
	status = models.CharField(max_length=20)
	rep = models.CharField(max_length=20)

	def __unicode__(self):
		return str(self.profile_number)

class Advice(models.Model):
	company = models.CharField(max_length=20)
	ticker = models.CharField(max_length=20)
	content = models.TextField()
	price_target = models.FloatField(default=0)
	time_scale = models.CharField(max_length=20, default="6 months")

	def __unicode__(self):
		return self.company

class User(models.Model):
	user_id = models.IntegerField(default=0)
	ip_address = models.CharField(default="0.0.0.0", max_length=20)
	participation_timestamp = models.DateTimeField('date published')
	age = models.IntegerField(default=0)
	gender = models.IntegerField(default=0)
	experience = models.IntegerField(default=0)
	investment_familiarity = models.IntegerField(default=0)
	firm = models.IntegerField(default=0)
	past_performance = models.IntegerField(default=0)
	zillow = models.IntegerField(default=0)
	costar = models.IntegerField(default=0)
	netease = models.IntegerField(default=0)
	athena = models.IntegerField(default=0)
	reputation_influence = models.IntegerField(default=0)
	affiliation_influence = models.IntegerField(default=0)

class Vote(models.Model):
	profile = models.ForeignKey(Profile)
	advice = models.ForeignKey(Advice)
	user_id = models.IntegerField(default=0)
	value = models.IntegerField(default=0)
	timestamp = models.DateTimeField('date published')
	is_performance = models.BooleanField()
	is_submission = models.BooleanField()

class UserConnection(models.Model):
	user = models.ForeignKey(User)
	world_number = models.IntegerField(default=0)

class World(models.Model):
	world_number = models.IntegerField(default=0)
	advice = models.ForeignKey(Advice)
	profile = models.ForeignKey(Profile)

class Next_Timestamp(models.Model):
	user_id = models.IntegerField(default=0)
	timestamp = models.DateTimeField('next timestamp')
	sequence_number = models.IntegerField(default=0)

class Advice_Feedback(models.Model):
	user_id = models.IntegerField(default=0)
	timestamp = models.DateTimeField('next timestamp')
	sequence_number = models.IntegerField(default=0)
	value = models.IntegerField(default=0)
	advice = models.ForeignKey(Advice)
	profile = models.ForeignKey(Profile)

