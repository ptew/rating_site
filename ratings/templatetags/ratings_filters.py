from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary[key]

@register.filter(name='get_status')
def get_status(dictionary, key):
	return "underperformed" if int(dictionary[key]) == 1 else "outperformed"

@register.filter(name='get_rep')
def get_rep(dictionary, key):
    return "lowly" if int(dictionary[key]) == 1 else "highly"