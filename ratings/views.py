from random import randrange, shuffle
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from ratings.models import Advice, Profile, UserConnection, User, PerformanceVote, QualityVote, World, Vote
from dajaxice.decorators import dajaxice_register
from dajaxice.core import dajaxice_functions
import logging

def index(request, user_id):
	param_dictionary = {}

	# add callback check to verify they are a registered user
	advice_dict = {}
	advice_rep = {}
	advice_status = {}
	profile_dict = {}
	advice_list = []

	user = User.objects.filter(user_id=int(user_id))
	if user:
		user= user[0]
		world_number = get_object_or_404(UserConnection, user = user).world_number
		# world_instances = World.objects.filter(world_number=world_number)
		# for world in world_instances:
		# 	advice = world.advice
		# 	prof = world.profile
		# 	if prof.profile_number==0 :
		# 		is_control = True

		# 	advice_rep[advice] = prof.rep
		# 	advice_status[advice] = prof.status
		# 	profile_dict[advice] = prof
		# 	advice_dict[advice.pk] = advice
	else:
		user = User(user_id=user_id, participation_timestamp = timezone.now())
		user.save()

		world_number = randrange(0,5)
		user_connect = UserConnection(user=user, world_number=world_number)
		user_connect.save()
		# for each advice create a user connection with a random profile
		# for advice_piece in advice_list:
		# 	if is_control:
		# 		prof = control_prof
		# 	else:
		# 		prof = get_object_or_404(Profile, profile_number = randrange(1,5))
		# 	user_connect = UserConnection(user=user, advice=advice_piece, profile=prof)
		# 	user_connect.save()

		# 	advice_rep[advice_piece] = user_connect.profile.rep
		# 	advice_status[advice_piece] = user_connect.profile.status
		# 	profile_dict[advice_piece] = prof
		# 	advice_dict[advice_piece.pk] = advice_piece

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
	for quality_vote in Vote.objects.filter(user = user, is_performance=False):
		quality_votes[quality_vote.advice.company] = quality_vote.value

	performance_votes = {}
	for performance_vote in Vote.objects.filter(user = user, is_performance=True):
		performance_votes[performance_vote.advice.company] = performance_vote.value

	param_dictionary['advice_list'] = advice_list

	param_dictionary['advice_dict'] = advice_dict
	param_dictionary['advice_rep'] = advice_rep
	param_dictionary['advice_status'] = advice_status
	param_dictionary['profile_dict'] = profile_dict
	param_dictionary['user'] = user
	param_dictionary['is_control'] = world_number > 1 ? True : None
	param_dictionary['quality_votes'] = quality_votes
	param_dictionary['performance_votes'] = performance_votes
	param_dictionary['world_number'] = world_number + 1

	return render(request, 'ratings/index.html', param_dictionary)

def detail(request, advice_id):
	advice = get_object_or_404(Advice, pk=advice_id)
	return render(request, 'ratings/detail.html', {'advice':advice})

@dajaxice_register
def submit_vote(request, advice_id, profile_id, isPerformance, value, user_id):
	user = get_object_or_404(User, user_id=user_id)
	prof = get_object_or_404(Profile, profile_number = profile_id)
	advice = get_object_or_404(Advice, pk = advice_id)
	time = timezone.now()
	user_vote;
	if bool(isPerformance):
		user_vote = PerformanceClickVote(user=user, profile=prof, timestamp=time, value=value, advice=advice)
		user_vote.save()
	else:
		user_vote = QualityClickVote(user=user, profile=prof, timestamp=time, value=value, advice=advice)
		user_vote.save()
	return simplejson.dumps({'message':'was %s' % value})
