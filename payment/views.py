from django.shortcuts import render
from hashlib import md5

# Create your views here.
def payments(request):
    pid = "123"
    sid = "GameShopASD"
    amount = 5
    secret_key = "***REMOVED***"
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()
    return render(
        request,
        "payments.html",
        context={"pid":pid, "sid":sid, "amount":amount, "checksum":checksum},
    )
    
def success(request):
    return render(
        request,
        "success.html",
        context={},
    )    
    
def cancel(request):
    return render(
        request,
        "cancel.html",
        context={},
    )    
    
def error(request):
    return render(
        request,
        "error.html",
        context={},
    )