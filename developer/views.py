from django.shortcuts import render
from django.core.validators import URLValidator
from gamelist.models import Game
from developer.forms import AddGame
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def adding(request):
    if request.method == 'POST':
        form = AddGame(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.developer = request.user.profile
            instance.save()
            return redirect('index')
    else:
        form = AddGame()
    return render(request, 'adding.html', {'form': form})
