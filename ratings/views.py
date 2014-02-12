from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from ratings.models import Advice

def index(request):
	advice_list = Advice.objects.all()
	template = loader.get_template('ratings/index.html')
	context = RequestContext(request, {
		'advice_list': advice_list
		})
	return HttpResponse(template.render(context))

def vote(request, advice_id):
	advice = get_object_or_404(Advice, pk=advice_id)
	return render(request, 'ratings/vote.html', {'advice':advice})