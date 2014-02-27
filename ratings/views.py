from random import randrange
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from ratings.models import Advice, Profile, UserConnection, User

def index(request, user_id="0"):
	param_dictionary = {}
	
	advice_list = Advice.objects.all()
	param_dictionary['advice_list'] = advice_list
	
	user_id = int(user_id)
	
	# add callback check to verify they are a registered user

	advice_rep = {}
	advice_status = {}
	# for each advice create a user connection with a random profile
	for advice_piece in advice_list:
		prof = get_object_or_404(Profile, profile_number = randrange(0,5))
		
		user = User.objects.filter(user_id=user_id)
		if not user:
			user = User(user_id=user_id, participation_timestamp = timezone.now())
			user.save()
		else:
			user=user[0]
		
		user_connect = UserConnection(user=user, advice=advice_piece, profile=prof)
		user_connect.save()
		advice_rep[advice_piece] = user_connect.profile.rep
		advice_status[advice_piece] = user_connect.profile.status
	param_dictionary['advice_rep'] = advice_rep
	param_dictionary['advice_status'] = advice_status

	return render(request, 'ratings/index.html', param_dictionary)

def detail(request, advice_id):
	advice = get_object_or_404(Advice, pk=advice_id)
	return render(request, 'ratings/detail.html', {'advice':advice})


