from django.db import models
from common.models import CardInfo

class Rarity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CardType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class MonsterType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class MonsterAttribute(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class FrameType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Series(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
class CardDetails(CardInfo):
    card_type = models.ForeignKey('CardType', related_name='card_types', on_delete=models.CASCADE, null=True, blank=True)
    monster_type = models.ForeignKey('MonsterType', related_name='monster_types', on_delete=models.CASCADE, null=True, blank=True)
    monster_attribute = models.ForeignKey('MonsterAttribute', related_name='monster_attributes', on_delete=models.CASCADE, null=True, blank=True)
    frame_type = models.ForeignKey('FrameType', related_name='frame_types', on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class PrintSeries(models.Model):
    card = models.ForeignKey('CardDetails', related_name='printings', on_delete=models.CASCADE)
    rarity = models.ForeignKey('Rarity', related_name='cards', on_delete=models.CASCADE, null=True, blank=True)
    full_series = models.ForeignKey('Series', related_name='series', on_delete=models.CASCADE)
    series_code = models.CharField(max_length=50)
    