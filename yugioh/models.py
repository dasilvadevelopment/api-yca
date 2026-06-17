from django.db import models
from common.models import CardInfo

class Rarity(models.Model):
    name = models.CharField(max_length=20)

class CardType(models.Model):
    name = models.CharField(max_length=20)

class MonsterType(models.Model):
    name = models.CharField(max_length=20)

class MonsterAttribute(models.Model):
    name = models.CharField(max_length=20)

class FrameType(models.Model):
    name = models.CharField(max_length=20)

class Series(models.Model):
    name = models.TextField()

class CardDetails(CardInfo):
    rarity = models.ForeignKey('Rarity', related_name='Rarity', on_delete=models.CASCADE, null=True, blank=True)
    card_type = models.ForeignKey('CardType', related_name='CardType', on_delete=models.CASCADE, null=True, blank=True)
    monster_type = models.ForeignKey('MonsterType', related_name='MonsterType', on_delete=models.CASCADE, null=True, blank=True)
    monster_attribute = models.ForeignKey('MonsterAttribute', related_name='MonsterAttribute', on_delete=models.CASCADE, null=True, blank=True)
    frame_type = models.ForeignKey('FrameType', related_name='FrameType', on_delete=models.CASCADE, null=True, blank=True)
    full_series = models.ForeignKey('Series', related_name='Series', on_delete=models.CASCADE)
    level = models.IntegerField(null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)