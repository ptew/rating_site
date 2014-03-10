from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from ratings.models import Advice, Profile, User, Vote
from dajaxice.core import dajaxice_functions
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
import logging

@dajaxice_register
def click_vote(request, advice_id, profile_id, isPerformance, value, is_submission, user_id):
	user = get_object_or_404(User, user_id=user_id)
	prof = get_object_or_404(Profile, profile_number = profile_id)
	advice = get_object_or_404(Advice, pk = advice_id)
	time = timezone.now()
	user_vote = Vote(user=user, profile=prof, timestamp=time, value=value, advice=advice, is_performance=bool(isPerformance), is_submission=bool(is_submission))
	user_vote.save()
	return simplejson.dumps({'message':'was %s' % value})