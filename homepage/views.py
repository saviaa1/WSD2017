from django.shortcuts import render
from django.http import HttpResponse, Http404
from gamelist.models import Game

# Create your views here.
def index(request):
    num_games = Game.objects.all().count()
    num_customers = 0
    return render(
        request,
        "index.html",
        context={"num_games":num_games, "num_customers":num_customers},
    )
