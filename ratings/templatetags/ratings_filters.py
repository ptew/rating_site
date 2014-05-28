from django import template
import random

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary[key]

@register.filter(name='get_status')
def get_status(dictionary, key):
	return "underperformed" if int(dictionary[key]) == 1 else "outperformed"

@register.filter(name='get_rand')
def get_rand(dictionary,key):
	return random.choice(["3","4"])

@register.filter(name='get_rep')
def get_rep(dictionary, key):
    return random.choice(["131st","133rd"]) if int(dictionary[key]) == 1 else random.choice(["3rd","5th"])