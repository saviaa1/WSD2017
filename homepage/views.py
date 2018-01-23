from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    num_games = 0
    num_customers = 0
    return render(
        request,
        "index.html",
        context={"num_games":num_games, "num_customers":num_customers},
    )
