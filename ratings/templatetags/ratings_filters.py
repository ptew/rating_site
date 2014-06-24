from django import template
import random

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary[key]

@register.filter(name='get_status')
def get_status(dictionary, key):
	return "1.3" if int(dictionary[key]) == 1 else "4.7"

@register.filter(name='get_rand')
def get_rand(dictionary,key):
	return random.choice(["3"])

@register.filter(name='get_rep')
def get_rep(dictionary, key):
    return random.choice(["134th"]) if int(dictionary[key]) == 1 else random.choice(["2nd"])