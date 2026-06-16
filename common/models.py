from django.db import models

class CardInfo(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    series = models.CharField(max_length=20)
    image = models.ImageField()

    class Meta:
        abstract = True