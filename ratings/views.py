from random import randrange
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from ratings.models import Advice, Profile, UserConnection, User, PerformanceVote, QualityVote
from dajaxice.decorators import dajaxice_register
from dajaxice.core import dajaxice_functions
import logging

def index(request, user_id):
	param_dictionary = {}
	
	advice_list = Advice.objects.all()
	advice_dict = {}

	param_dictionary['advice_list'] = advice_list
	
	# add callback check to verify they are a registered user

	advice_rep = {}
	advice_status = {}
	profile_dict = {}
	is_control = False

	user = User.objects.filter(user_id=int(user_id))
	if user:
		user= user[0]
		user_connections = UserConnection.objects.filter(user=user)
		for user_connect in user_connections:
			advice = user_connect.advice
			prof = user_connect.profile
			if prof.profile_number==0 :
				is_control = True

			advice_rep[advice] = prof.rep
			advice_status[advice] = prof.status
			profile_dict[advice] = prof
			advice_dict[advice.pk] = advice
	else:
		user = User(user_id=user_id, participation_timestamp = timezone.now())
		user.save()

		is_control = randrange(0,5) == 0
		control_prof = get_object_or_404(Profile, profile_number=0)
		# for each advice create a user connection with a random profile
		for advice_piece in advice_list:
			if is_control:
				prof = control_prof
			else:
				prof = get_object_or_404(Profile, profile_number = randrange(1,5))
			user_connect = UserConnection(user=user, advice=advice_piece, profile=prof)
			user_connect.save()

			advice_rep[advice_piece] = user_connect.profile.rep
			advice_status[advice_piece] = user_connect.profile.status
			profile_dict[advice_piece] = prof
			advice_dict[advice_piece.pk] = advice_piece

	param_dictionary['advice_dict'] = advice_dict
	param_dictionary['advice_rep'] = advice_rep
	param_dictionary['advice_status'] = advice_status
	param_dictionary['profile_dict'] = profile_dict
	param_dictionary['user'] = user
	param_dictionary['is_control'] = is_control


	return render(request, 'ratings/index.html', param_dictionary)

def detail(request, advice_id):
	advice = get_object_or_404(Advice, pk=advice_id)
	return render(request, 'ratings/detail.html', {'advice':advice})

# @dajaxice_register
# def vote(request, advice_id, profile_id, isPerformance, value, user_id):
# 	user = get_object_or_404(User, user_id=user_id)
# 	prof = get_object_or_404(Profile, profile_number = profile_id)
# 	advice = get_object_or_404(Advice, pk = advice_id)
# 	time = timezone.now()
# 	user_vote;
# 	if bool(isPerformance):
# 		logging.debug("QualityVote")
# 		user_vote = PerformanceVote(user=user, profile=prof, timestamp=time, value=value, advice=advice)
# 		user_vote.save()
# 	else:
# 		logging.debug("QualityVote")
# 		user_vote = QualityVote(user=user, profile=prof, timestamp=time, value=value, advice=advice)
# 		user_vote.save()
# 	return simplejson.dumps({'message':'was %s' % value})
