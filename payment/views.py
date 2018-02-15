from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import redirect
from hashlib import md5
from django.contrib.auth.models import User
from gamelist.models import Game
from payment.models import Purchase
from django.contrib.auth.decorators import login_required

sid = "GameShopASD"
secret_key = "***REMOVED***"

# Create your views here.
@login_required(login_url="/login")
def payments(request, gameid):
    try:
        game = Game.objects.get( id = gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

    purchase = Purchase(username = request.user, gameid = gameid)
    purchase.save()

    amount = game.price;
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(purchase.id, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()

    return render(
        request,
        "payments.html",
        context={"pid":purchase.id, "sid":sid, "checksum":checksum, "game":game},
    )

@login_required(login_url="/login")
def success(request):
    pid = request.GET.get('pid')
    ref = request.GET.get('ref')
    result = request.GET.get('result')
    checksum = request.GET.get('checksum')
    checksumstr = "pid={}&ref={}&result={}&token={}".format(pid, ref, result, secret_key)
    m = md5(checksumstr.encode("ascii"))
    checksum2 = m.hexdigest()
    if checksum == checksum2:
        try:
            purchase = Purchase.objects.get( id = pid )
            game = Game.objects.get( id = purchase.gameid )
            purchase.success = True
            purchase.save()
        except ObjectDoesNotExist:
            return HttpResponseNotFound()
        game.owners.add(request.user.profile)
        return render(
            request,
            "success.html",
            context={"game":game},
        )
    else:
        return redirect('purchase/error', request=request)

def cancel(request):
    pid = request.GET.get('pid')
    try:
        purchase = Purchase.objects.get( id = pid )
        game = Game.objects.get( id = purchase.gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return render(
        request,
        "cancel.html",
        context={"game":game},
    )

def error(request):
    pid = request.GET.get('pid')
    try:
        purchase = Purchase.objects.get( id = pid )
        game = Game.objects.get( id = purchase.gameid )
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return render(
        request,
        "error.html",
        context={"game":game},
    )
