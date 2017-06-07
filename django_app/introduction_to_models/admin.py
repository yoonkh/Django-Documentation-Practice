from django.contrib import admin

from .models import Person
from .models import Player, Club, TradeInfo

admin.site.register(Player)
admin.site.register(Club)
admin.site.register(TradeInfo)
admin.site.register(Person)
