from django.http import HttpResponseNotFound
from django.shortcuts import render
from gamelist.models import Game
from hashlib import md5

#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url="/login")
def payments(request, gameid):
    try: 
        game = Game.objects.get( id = gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    userid = "userid" #TODO use user id
    pid = str(userid) + "_"+ str(gameid)
    sid = "GameShopASD"
    amount = game.price;
    secret_key = "***REMOVED***"
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()
    return render(
        request,
        "payments.html",
        context={"pid":pid, "sid":sid, "checksum":checksum, "game":game},
    )
    
def success(request, gameid):
    try: 
        game = Game.objects.get( id = gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return render(
        request,
        "success.html",
        context={"game":game},
    )    
    
def cancel(request, gameid):
    try: 
        game = Game.objects.get( id = gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return render(
        request,
        "cancel.html",
        context={"game":game},
    )    
    
def error(request, gameid):
    try: 
        game = Game.objects.get( id = gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return render(
        request,
        "error.html",
        context={"game":game},
    )