from django.db import models
from gamelist.models import Game

# Create your models here.
class Purchase(models.Model):
    username = models.CharField(max_length=150, blank=False)
    gameid = models.IntegerField(blank=False, default=1)
    date = models.DateField(auto_now=True)