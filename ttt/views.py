from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ttt.lib.game import Game

import importlib.machinery, os, time

def index(request):
    return render(request, 'ttt/index.html')

def play_game(request):
    return render(request, 'ttt/play_game.html')

def new_game(request):
    global player_name, game
    if request.POST.get('player_name', ''):
        player_name = request.POST.get('player_name', '')
        game = Game(player_name)
        if game.whose_turn == game.machine_player:
            game.take_turn()
        return render(request, 'ttt/new_game.html', game.render_data)
    else:
        if game.whose_turn == game.player_name:
            choice = request.POST.get('choice', '')
            time.sleep(2)
            game.take_turn(int(choice))
            return render(request, 'ttt/new_game.html', game.render_data
            )
        else:
            game.take_turn()
            time.sleep(2)
            return render(request, 'ttt/new_game.html', game.render_data
            )
