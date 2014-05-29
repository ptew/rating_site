from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajaxice.core import dajaxice_functions
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
import logging
from dajax.core import Dajax
from ratings.models import *

@dajaxice_register
def save_next(request, sequence_number, id_number):
	next = Next_Timestamp(user_id=id_number, sequence_number=sequence_number, timestamp=timezone.now())
	next.save()
	return simplejson.dumps({'message':'sequence_number: %s' % sequence_number})

@dajaxice_register
def click_vote(request, advice_id, profile_id, isPerformance, value, is_submission, id_number):
	prof = get_object_or_404(Profile, profile_number = profile_id)
	advice = get_object_or_404(Advice, pk = advice_id)
	time = timezone.now()
	
	ip_address = get_client_ip(request)
	ip = User.objects.filter(ip_address = ip_address)
	if ip:
		diff = time - ip[0].participation_timestamp
		if diff.seconds > 3600:
			return simplejson.dumps({'message':'Vote Timeout...' })

	user_vote = Vote(user_id=id_number, profile=prof, timestamp=time, value=value, advice=advice, is_performance=bool(isPerformance), is_submission=bool(is_submission))
	user_vote.save()
	return simplejson.dumps({'message':'id was %s' % id_number })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@dajaxice_register
def save_advice_feedback(request, advice_id, profile_id, id_number, value):
	prof = get_object_or_404(Profile, profile_number = profile_id)
	advice = get_object_or_404(Advice, pk = advice_id)
	time = timezone.now()

	feedback = Advice_Feedback(user_id=id_number, profile=prof, timestamp=time, value=value, advice=advice)
	feedback.save()
	return simplejson.dumps({'message':'advice feedback: %s' % value})

@dajaxice_register
def survey_batch_one(request, id_number, age, gender, experience):
	user = get_object_or_404(User, user_id=id_number)
	user.age = age
	user.gender = int(gender)
	user.experience = experience
	user.save()
	return simplejson.dumps({'message':'user batch one update successful'})

@dajaxice_register
def survey_batch_two(request, id_number, investment_familiarity, firm, past_performance):
	user = get_object_or_404(User, user_id=id_number)
	user.investment_familiarity = investment_familiarity
	user.firm = firm
	user.past_performance = past_performance
	user.save()
	return simplejson.dumps({'message':'user batch two update successful'})

@dajaxice_register
def survey_batch_three(request, id_number, zillow, costar, netease, athena):
	user = get_object_or_404(User, user_id=id_number)
	user.zillow = int(zillow)
	user.costar = int(costar)
	user.netease = int(netease)
	user.athena = int(athena)
	user.save()
	return simplejson.dumps({'message':'user batch three update successful'})

@dajaxice_register
def survey_batch_four(request, id_number, reputation_influence, affiliation_influence):
	user = User.objects.filter(user_id=id_number)
	user.reputation_influence = int(reputation_influence)
	user.affiliation_influence = int(affiliation_influence)
	user.save()
	return simplejson.dumps({'message':'user batch four update successful'})