from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from ratings.models import Advice, Profile, User, PerformanceVote, QualityVote
from dajaxice.core import dajaxice_functions
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
import logging

@dajaxice_register
def vote(request, advice_id, profile_id, isPerformance, value, user_id):
	logging.debug("advice_id: " + str(advice_id))
	logging.debug("profile_id: " + str(profile_id))
	logging.debug("user_id: " + str(user_id))
	user = get_object_or_404(User, user_id=user_id)
	prof = get_object_or_404(Profile, profile_number = profile_id)
	advice = get_object_or_404(Advice, pk = advice_id)
	time = timezone.now()
	if bool(isPerformance):
		logging.debug("QualityVote")
		user_vote = PerformanceVote(user=user, profile=prof, timestamp=time, value=value, advice=advice)
	else:
		logging.debug("QualityVote")
		user_vote = QualityVote(user=user, profile=prof, timestamp=time, value=value, advice=advice)
	user_vote.save()
	return simplejson.dumps({'message':'was %s' % value})