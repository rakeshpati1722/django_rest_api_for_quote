from django.db import models

# Create your models here.
class QuoteModel(models.Model):
    Quote = models.CharField(max_length=256)
    Author = models.CharField(max_length=256)
    Rating = models.CharField(max_length=256, blank=True)

def __str__(self):
    return self.Quote