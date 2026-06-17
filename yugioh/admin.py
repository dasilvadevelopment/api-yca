from django.contrib import admin
from yugioh.models import Rarity, CardType, MonsterType, MonsterAttribute, FrameType, Series, CardDetails
# Register your models here.

admin.site.register(Rarity)
admin.site.register(CardType)
admin.site.register(MonsterType)
admin.site.register(MonsterAttribute)
admin.site.register(FrameType)
admin.site.register(Series)
admin.site.register(CardDetails)