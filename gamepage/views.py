from django.http import HttpResponseNotFound, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from gamelist.models import Game
from gamepage.models import GameData

# Create your views here.

@csrf_protect
@login_required(login_url="/login")
def gameviews(request, gameid):
    try: 
        game = Game.objects.get( id = gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    try: 
        gameData = GameData.objects.get( game = game, player = request.user.profile )
    except ObjectDoesNotExist:
        gameData = GameData(player = request.user.profile, game = game)
        
    if request.method == "POST":
        jsonDATA = json.loads(request.POST['data'])
        if jsonDATA["messageType"] == "SCORE":
            score = float(jsonDATA["score"])
            if (not gameData.highscore or score > gameData.highscore):
                gameData.highscore = score
                gameData.save()

        elif jsonDATA["messageType"] == "SAVE":
            print(jsonDATA["gameState"])
            gameData.gameState = str(jsonDATA["gameState"]).replace("\'", "\"")
            gameData.save()

        else:
            print("if POST success, something inside failed")

    else:
        print("if POST fail")

    gameOwned = game.developer == request.user.profile
    if not gameOwned:
        owners = game.owners.all()
        for owner in owners:
            if owner == request.user.profile:
                gameOwned = True
                break
    if gameOwned:
        return render(
            request,
            "gamepage.html",
            context={"game":game, "savedGame": json.dumps(gameData.gameState)},
        )
    else:
        return redirect('purchase', gameid=gameid)
        
@csrf_exempt
@login_required(login_url="/login")
def loadgamedata(request, gameid):
    try: 
        game = Game.objects.get( id = gameid )
        gameData = GameData.objects.get( game = game, player = request.user.profile )
    except ObjectDoesNotExist:
        return JsonResponse({"gameState": "ERROR"})
    return JsonResponse({"gameState": gameData.gameState})