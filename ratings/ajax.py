from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def vote(request,value):
    return simplejson.dumps({'message':'Your value was %s' % value})