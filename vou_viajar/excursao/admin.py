from django.contrib import admin

from .models import Excursion, ExcursionSituation, ExcursionType, Destiny, ServiceProvider, ServiceProviderType
from .models import Transport, Estimate, TravelItinerary

admin.site.register(Excursion)
admin.site.register(ExcursionSituation)
admin.site.register(ExcursionType)
admin.site.register(Destiny)
admin.site.register(ServiceProvider)
admin.site.register(ServiceProviderType)
admin.site.register(Transport)
admin.site.register(Estimate)
admin.site.register(TravelItinerary)