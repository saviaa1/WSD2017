from django.shortcuts import render
from django.http import JsonResponse
from gamelist.models import Game
from django.core import serializers
from django.db.models import Max
from gamepage.models import GameData
from django.db.models.query import QuerySet
from django.db.models import Max
from payment.models import Purchase
from django.contrib.auth.decorators import login_required




#Gets all the games from the site
def games(request):
    if request.method == 'GET':
        gameObjects = Game.objects.all()
        gameSerialized = serializers.serialize('json', gameObjects)
        return JsonResponse(gameSerialized, safe=False)

#Gets all highscores
def highscores(request):
    if request.method == 'GET':
        gameDataObjects = GameData.objects.all()
        gameDataSerialized = serializers.serialize('json', gameDataObjects)
        return JsonResponse(gameDataSerialized, safe=False)

#Gets all highscores based on game requested
def highscoresPerGame(request, object_id):
    if request.method == 'GET':
        gameDataObjects = GameData.objects.all().filter(game = object_id).order_by('highscore')
        gameDataSerialized = serializers.serialize('json', gameDataObjects)
        return JsonResponse(gameDataSerialized, safe=False)

#Gets all sales per game to the developer that added the game
@login_required
def saleStatistics(request, object_id):
    isDeveloper = request.user.profile.developer
    game = Game.objects.get( id = object_id )
    gameOwned = game.developer == request.user.profile
    if request.method == 'GET' and isDeveloper and gameOwned:
        purchaseObjects = Purchase.objects.all().filter(gameid = object_id, success = True)
        purchaseSerialized = serializers.serialize('json', purchaseObjects)
        return JsonResponse(purchaseSerialized, safe=False)
