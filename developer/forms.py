from django import forms
from gamelist.models import Game
from django.forms import ModelForm

class AddGame(ModelForm):
    class Meta:
        model = Game
        fields = [ 'name', 'description', 'category', 'price', 'image_url', 'game_url', ]
