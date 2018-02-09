from django.shortcuts import render
from gamelist.models import Game
from django.http import HttpResponse
import json
# from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url="/login")


def gameviews(request, gameid):
    game = Game.objects.get(id=gameid)  # TODO antaa 404 jos gameid ei olemassa
    return render(
        request,
        "gamepage.html",
        context={"game": game},
    )


# TODO: temp vars, kun SQL tehty poista nämä
gameState = dict()
GLOBAL_Entry = None


def iframeMessage(request):  # TODO: pitäisikö käyttää try catch rakennetta täällä. muutamassa kohdassa mahd kaatua jos tulee muuta kuin pitäisi
    if request.method == "POST":
        global gameState, GLOBAL_Entry
        jsonDATA = json.loads(request.POST['data'])
        print(jsonDATA)

        if jsonDATA["messageType"] == "SCORE":
            score = float(jsonDATA["score"])
            print("score = ", score)
            # TODO: tallenna SQL
            return HttpResponse("score success")

        elif jsonDATA["messageType"] == "SAVE":
            # TODO: if else globaalin muuttujan takia
            if not gameState:
                gameState = jsonDATA["gameState"]
            else:
                gameState.clear()
                gameState = jsonDATA["gameState"]
            print("gameState = ", gameState)
            # TODO: tallenna SQL
            return HttpResponse("save gameState succeess")

        elif jsonDATA["messageType"] == "LOAD_REQUEST":
            # TODO: jos löytyy gameState lähetä se muuten lähetä errorMessage
            if not gameState:
                print("load_request: fail")
                # TODO: lähetä error message iframille
                return HttpResponse("load_request, None")
            else:
                # TODO: lataa SQL ja lähetä se
                print("load_request = ", gameState)
                return HttpResponse("load_request, succeess")

        else:
            print("if POST success, something inside failed")
            return HttpResponse("err")

    else:
        print("if POST fail")
        return HttpResponse("err")
