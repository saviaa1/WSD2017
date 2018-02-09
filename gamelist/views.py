from django.views import generic

from .models import Game


# Create your views here.
class GameListView(generic.ListView):
    model = Game
