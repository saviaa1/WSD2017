from gamelist.models import Game
from developer.forms import AddGame
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from social_django.models import UserSocialAuth
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from payment.models import Purchase


# Create your views here.
@login_required
def adding(request):
    if request.method == 'POST':
        form = AddGame(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.developer = request.user.profile
            instance.save()
            return redirect('profile')
    else:
        form = AddGame()
    isDeveloper = request.user.profile.developer
    if isDeveloper:
        return render(request, 'adding.html', {'form': form})
    else:
        return redirect('index')


@login_required
def deleting(request, object_id):
    game = Game.objects.get(id=object_id)
    gameOwned = game.developer == request.user.profile
    if gameOwned:
        object = get_object_or_404(Game, pk=object_id)
        object.delete()
        return redirect('profile')
    else:
        return redirect('profile')


@login_required
def profile(request):
    user = request.user
    try:
        twitterLogin = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitterLogin = None

    try:
        googleLogin = user.social_auth.get(provider='google-oauth2')
    except UserSocialAuth.DoesNotExist:
        googleLogin = None

    userCanLogout = (user.social_auth.count() > 1 or user.has_usable_password())
    return render(request, 'profile.html', {
        'twitterLogin': twitterLogin,
        'googleLogin': googleLogin,
        'userCanLogout': userCanLogout,
    })


@login_required
def editing(request, object_id):
    game = Game.objects.get(id=object_id)
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
        c = {"form": form, "object_id": game}
        return render(request, "adding.html", c)
    else:
        redirect(request, 'profile.html')


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password set')
            return redirect('password')
        else:
            messages.error(request, 'An error occured')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})


@login_required
def statistics(request, object_id):
    game = Game.objects.get(id=object_id)
    gameOwned = game.developer == request.user.profile
    purchase = Purchase.objects.filter(gameid=object_id)
    if gameOwned:
        return render(request, 'statistics.html', {
            'game': game,
            'purchase': purchase
        })
    else:
        return redirect('profile')
