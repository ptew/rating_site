from random import randrange, shuffle
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from ratings.models import *
import logging

def index(request):
	param_dictionary = {}

	# add callback check to verify they are a registered user
	advice_dict = {}
	advice_rep = {}
	advice_status = {}
	profile_dict = {}
	advice_list = []
	world_number = 0

	ip_address = get_client_ip(request)
	ip = User.objects.filter(ip_address = ip_address)
	if ip:
		user = ip[0]

		# If the user has accessed the site over an hour ago, don't allow them to vote
		diff = timezone.now() - user.participation_timestamp
		if diff.seconds > 3600:
			return render(request, 'ratings/thanks.html')

		# If the ip has submitted votes, don't allow them to vote
		if Vote.objects.filter(user_id=user.user_id,is_submission = True):

			return render(request, 'ratings/thanks.html')			

		world_number = get_object_or_404(UserConnection, user = user).world_number

	else:
		user_id = randrange(0,1000)
		while(User.objects.filter(user_id=user_id)):
			user_id = randrange(0,1000)
		user = User(user_id=user_id, participation_timestamp = timezone.now(), ip_address = ip_address)
		user.save()

		world_number = randrange(0,5)
		user_connect = UserConnection(user=user, world_number=world_number)
		user_connect.save()

	world_instances = World.objects.filter(world_number=world_number).order_by('?')
	for world in world_instances:
		advice = world.advice
		advice_list.append(advice)
		prof = world.profile

		advice_rep[advice] = prof.rep
		advice_status[advice] = prof.status
		profile_dict[advice] = prof
		advice_dict[advice.pk] = advice

	quality_votes = {}
	for quality_vote in Vote.objects.filter(user_id = user.user_id, is_performance=False):
		quality_votes[quality_vote.advice.company] = quality_vote.value

	performance_votes = {}
	for performance_vote in Vote.objects.filter(user_id = user.user_id, is_performance=True):
		performance_votes[performance_vote.advice.company] = performance_vote.value		

	param_dictionary['advice_list'] = advice_list

	param_dictionary['advice_dict'] = advice_dict
	param_dictionary['advice_rep'] = advice_rep
	param_dictionary['advice_status'] = advice_status
	param_dictionary['profile_dict'] = profile_dict
	param_dictionary['user'] = user
	param_dictionary['is_control'] = True if world_number > 1 else None
	param_dictionary['quality_votes'] = quality_votes
	param_dictionary['performance_votes'] = performance_votes
	param_dictionary['world_number'] = world_number + 1

	return render(request, 'ratings/index.html', param_dictionary)

def thankyou(request):
	return render(request, 'ratings/thanks.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

