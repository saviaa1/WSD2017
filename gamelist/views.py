from django.views import generic
from .models import Game, GameCategories


# Create your views here.
class GameListView(generic.ListView):
    model = Game
    # TODO: Paginator, muuta koko 10? numeropalkin leveyden rajoitus?
    paginate_by = 10
