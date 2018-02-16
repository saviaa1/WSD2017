from django.http import HttpResponseNotFound, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import json
from gamelist.models import Game
from gamepage.models import GameData

# Create your views here.


@csrf_protect
@login_required(login_url="/login")
def gameviews(request, gameid):
    try:
        game = Game.objects.get(id=gameid)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    try:
        gameData = GameData.objects.filter(game=game).order_by("-highscore")
        highscores = []
        for i in range(min(5, len(gameData))):
            highscores.append((gameData[i].player.user, gameData[i].highscore))
    except ObjectDoesNotExist:
        highscores = []
    try:
        gameDataForUser = GameData.objects.get(game=game, player=request.user.profile)
    except ObjectDoesNotExist:
        gameDataForUser = GameData(player=request.user.profile, game=game)

    if request.method == "POST":
        jsonDATA = json.loads(request.POST['data'])
        if jsonDATA["messageType"] == "SCORE":
            score = float(jsonDATA["score"])
            if (not gameDataForUser.highscore or score > gameDataForUser.highscore):
                gameDataForUser.highscore = score
                gameDataForUser.save()

        elif jsonDATA["messageType"] == "SAVE":
            print(jsonDATA["gameState"])
            gameDataForUser.gameState = str(jsonDATA["gameState"]).replace("\'", "\"")
            gameDataForUser.save()

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
            {"game": game, "highscores": highscores},
        )
    else:
        return redirect('purchase', gameid=gameid)


@csrf_protect
@login_required(login_url="/login")
def loadgamedata(request, gameid):
    try:
        game = Game.objects.get(id=gameid)
        gameDataForUser = GameData.objects.get(game=game, player=request.user.profile)
    except ObjectDoesNotExist:
        print("Return load error")
        return JsonResponse({"gameState": None})
    print("Return load success")
    print(gameDataForUser.gameState)
    return JsonResponse({"gameState": gameDataForUser.gameState})
