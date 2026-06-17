from django.db import models

class CardInfo(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        abstract = True