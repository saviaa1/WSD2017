from django.shortcuts import render
from django.core.validators import URLValidator
from gamelist.models import Game
from developer.forms import AddGame
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
    isDeveloper = request.user.profile.developer
    if isDeveloper:
        return render(request, 'adding.html', {'form': form})
    else:
        return redirect('index')

@login_required
def deleting(request, object_id):
    game = Game.objects.get( id = object_id )
    gameOwned = game.developer == request.user.profile
    if gameOwned:
        object = get_object_or_404(Game, pk=object_id)
        object.delete()
        return redirect('profile')
    else:
        return redirect('profile')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def editing(request, object_id):
    game = Game.objects.get( id = object_id )
    gameOwned = game.developer == request.user.profile
    if gameOwned:
        if request.method == 'POST':
            form = AddGame(request.POST, instance=game)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.developer = request.user.profile
                instance.save()
                return redirect('profile')
        else:
            form = AddGame(instance=game)
        c = { "form": form, "object_id": game }
        return render(request, "adding.html", c)
    else:
        redirect(request, 'profile.html')
