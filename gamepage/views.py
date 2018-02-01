from django.http import HttpResponseNotFound
from django.shortcuts import render
from gamelist.models import Game
#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url="/login")
def gameviews(request, gameid):
    try: 
        game = Game.objects.get( id = gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return render(
        request,
        "gamepage.html",
        context={"game":game},
    )
