from django.shortcuts import render
from gamelist.models import Game
from django.views.decorators.csrf import csrf_protect
import json
# from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url="/login")

# TODO: temp vars, kun SQL tehty poista nämä, jos ihan tyhjä niin testgame antaa error
gameState = {'playerItems': [], 'score': 0}
GLOBAL_Entry = None


@csrf_protect
def gameviews(request, gameid):
    game = Game.objects.get(id=gameid)  # TODO antaa 404 jos gameid ei olemassa

    if request.method == "POST":
        # TODO: pitäisikö käyttää try catch rakennetta täällä.
        # Muutamassa kohdassa mahd kaatua jos tulee
        global gameState, GLOBAL_Entry
        jsonDATA = json.loads(request.POST['data'])
        print(jsonDATA)

        if jsonDATA["messageType"] == "SCORE":
            score = float(jsonDATA["score"])
            print("score = ", score)
            # TODO: tallenna SQL

        elif jsonDATA["messageType"] == "SAVE":
            # TODO: if else globaalin muuttujan takia
            if not gameState:
                gameState = jsonDATA["gameState"]
            else:
                gameState.clear()
                gameState = jsonDATA["gameState"]
            print("gameState = ", gameState)
            # TODO: tallenna SQL
        # TODO: onko seuraavalla käyttöä?
            '''elif jsonDATA["messageType"] == "LOAD_REQUEST":
            # TODO: jos löytyy gameState lähetä se muuten lähetä errorMessage
            if not gameState:
                print("load_request: fail")
                # TODO: lähetä error message iframille
            else:
                # TODO: lataa SQL ja lähetä se
                print("load_request = ", gameState)'''

        else:
            print("if POST success, something inside failed")

    else:
        print("if POST fail")

    return render(
        request,
        "gamepage.html",
        {"game": game, "savedGame": json.dumps(gameState)},
    )
