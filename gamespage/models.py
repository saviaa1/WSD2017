from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=255, unique=True, blank=False)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	image_url = models.URLField(blank=True)
	game_url = models.URLField(blank=False)
	