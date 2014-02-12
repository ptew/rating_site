from django.contrib import admin
from ratings.models import Profile, Advice, Connection
# Register your models here.

class ConnectionInline(admin.TabularInline):
	model = Connection
	extra = 2

class AdviceAdmin(admin.ModelAdmin):
	fieldsets = [
		('Advice Content', {'fields': ['company', 'ticker' , 'price_target', 'time_frame', 'content']}),
	]
	inlines = [ConnectionInline];
	list_display = ('company', 'id')
	search_fields = ['company', 'id']

class ProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		("Proile Content", {'fields': ['world']}),
	]
	inlines = [ConnectionInline];
	list_display = ('world',)
	search_fields = ['world']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Advice,AdviceAdmin)