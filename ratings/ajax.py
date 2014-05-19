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