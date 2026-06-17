from rest_framework import viewsets
from yugioh.serializers import CardDetailSerializers
from yugioh.models import CardDetails

class YugiohViewSet(viewsets.ModelViewSet):
    queryset = CardDetails.objects.all()
    serializer_class = CardDetailSerializers