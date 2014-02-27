from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from ratings import Vote, Profile, User, Advice

@dajaxice_register
def vote(request,value):

    return simplejson.dumps({'message':'Your value was %s' % value})