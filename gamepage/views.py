from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import redirect
from gamelist.models import Game
from payment.models import Purchase
#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url="/login")
def gameviews(request, gameid):
    try: 
        game = Game.objects.get( id = gameid )
        purchases = Purchase.objects.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    gamePurchased = False
    for purchase in purchases:
        if str(purchase.username) == str(request.user) and purchase.gameid == game.id:
            gamePurchased = True
            break
    if gamePurchased:
        return render(
            request,
            "gamepage.html",
            context={"game":game},
        )
    else:
        return redirect('purchase', gameid=gameid)
