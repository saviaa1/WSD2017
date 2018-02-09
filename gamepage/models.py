from django.db import models
from authentication.models import Profile
from gamelist.models import Game

# Create your models here.
class GameData(models.Model):
    player = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE, null=True, related_name='gamedata')
    game = models.ForeignKey('gamelist.Game', on_delete=models.CASCADE, null=True, related_name='gamedata')
    gameState = models.TextField(null=True)
    highscore = models.FloatField(null=True)
    