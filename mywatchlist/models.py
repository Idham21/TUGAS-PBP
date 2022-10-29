from email.policy import default
from django.db import models

class MyWatchList(models.Model):
    watched = models.BooleanField(default=True)
    title = models.TextField()
    rating = models.IntegerField()
    realease_date = models.DateField()
    review = models.TextField()