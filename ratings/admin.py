from django.contrib import admin
from ratings.models import Profile, Advice
# Register your models here.

class AdviceAdmin(admin.ModelAdmin):
	fieldsets = [
		('Advice Content', {'fields': ['company', 'ticker' , 'price_target', 'time_frame', 'content']}),
	]
	list_display = ('company', 'id')
	search_fields = ['company', 'id']

class ProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		("Proile Content", {'fields': ['profile_number', 'rep', 'status']}),
	]
	list_display = ('profile_number',)
	search_fields = ['profile_number']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Advice,AdviceAdmin)