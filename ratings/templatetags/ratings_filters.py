from django import template
import random

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary[key]

@register.filter(name='get_status')
def get_status(dictionary, key):
	prefix = random.choice(["3","4"]) + " ideas have "
	return prefix + "underperformed" if int(dictionary[key]) == 1 else prefix + "outperformed"

@register.filter(name='get_rep')
def get_rep(dictionary, key):
    return "not ranked" if int(dictionary[key]) == 1 else "ranked " + random.choice(["2nd","3rd","5th","7th"])