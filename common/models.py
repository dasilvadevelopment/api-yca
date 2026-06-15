from django.db import models

class CardInfo(models.Model):
    name = models.CharField(max_length=150)
