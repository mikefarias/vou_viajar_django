from django.contrib import admin

from .models import User, TravelAgency, Profile, ContactTravelAgency

admin.site.register(User)
admin.site.register(TravelAgency)
admin.site.register(Profile)
admin.site.register(ContactTravelAgency)
