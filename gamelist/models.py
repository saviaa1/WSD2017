from django.db import models
from authentication.models import Profile
from django.contrib.auth.models import User


class GameCategories:
    categories = (
        ("OTHER", "Other"),
        ("ACTION", "Action"),
        ("ARCADE", "Arcade"),
        ("PUZZLE", "Puzzle"),
        ("RACING", "Racing"),
        ("SHOOTER", "Shooter"),
        ("STRATEGY", "Strategy"),
    )


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image_url = models.URLField(blank=True)
    game_url = models.URLField(blank=False)
    category = models.CharField(
        max_length=25,
        default="OTHER",
        choices=GameCategories.categories,
    )
    developer = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE, null=True, related_name='games')
    owners = models.ManyToManyField('authentication.Profile', related_name='purchasedgames')
    # Set ForeignKey as profile so a game can be linked to a users profile and users can have multiple games
    # A many-to-one relation

    class meta:
        ordering = ["id"]

    def getuser(self):
        return self.profile.user
    # profile.game_set.all() gets all game objects related to profile
