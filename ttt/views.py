from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ttt.lib.game import Game
from django.core.cache import cache
from ttt.lib.ttt_board import TicTacToe

import importlib.machinery, os, time, pickle, random

def index(request):
    return render(request, 'ttt/index.html')

def play_game(request):
    return render(request, 'ttt/play_game.html')

def new_game(request):
    #global player_name, game
    if request.POST.get('player_name', ''):
        cache.set('player_name', request.POST.get('player_name', ''))
        player_name = cache.get('player_name')
        game = Game(player_name)
        if game.whose_turn == game.machine_player:
            game.take_turn()
        cache.set('game', game)
        return render(request, 'ttt/new_game.html', game.render_data)

    else:
        player_name = cache.get('player_name')
        game = cache.get('game')
        if game.whose_turn == game.player_name:
            choice = request.POST.get('choice', '')
            time.sleep(1)
            game.take_turn(int(choice))
            cache.set('game', game)
            return render(request, 'ttt/new_game.html', game.render_data
            )
        else:
            game.take_turn()
            time.sleep(1)
            cache.set('game', game)
            return render(request, 'ttt/new_game.html', game.render_data
            )


def wtf_page(request):
    if cache.get('board', request.user.id):
        board = cache.get('board', request.user.id)
        board.choose_space(str(random.choice(board.free_spaces)), 'X')
        cache.set('board', board, request.user.id)
    else:
        board = TicTacToe()
        cache.set('board', board, request.user.id)
    data = board.free_spaces
    return render(request, 'ttt/wtf.html', {'data': data})
