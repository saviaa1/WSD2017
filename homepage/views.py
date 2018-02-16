from django.shortcuts import render
from gamelist.models import Game
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    num_games = Game.objects.all().count()
    num_customers = User.objects.all().count()
    return render(
        request,
        "index.html",
        context={"num_games": num_games, "num_customers": num_customers},
    )
