from django.shortcuts import render
from rest_framework import viewsets
from yugioh.serializers import CardDetailSerializers
from yugioh.models import CardDetails

class YugiohViewSet(viewsets.ModelViewSet):
    queryset = CardDetails.objects.all()
    serializer = CardDetailSerializers(queryset, many=True)