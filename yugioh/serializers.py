from rest_framework import serializers
from .models import Rarity, CardType, MonsterType, MonsterAttribute, FrameType, Series, CardDetails

class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = ['name']

class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardType
        fields = ['name']

class MonsterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterType
        fields = ['name']

class MonsterAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterAttribute
        fields = ['name']

class FrameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrameType
        fields = ['name']

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['name']

class CardDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CardDetails
        fields = ['name', 'rarity', 'card_type', 'monster_type', 'monster_attribute', 'frame_type', 'level', 'full_series', 'attack', 'defense', 'description', 'series', 'image']
        depth = 1