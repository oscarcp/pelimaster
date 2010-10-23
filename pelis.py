# -*- coding: utf-8 -*-

# TODO:
# - Replace lists for dictionaries.
# - Solve the codification problem in Windows.
# - Improve the films list to have a director and description.

# Import python modules
import sys
import random
import datetime
import pdb

# Open files and create empty lists
films_file = open('lista.txt', 'r')
films = []
players = []
points = []
n_players = 0


def generate_random():
    """
    This function picks a random film from the films list.
    """
    print '\n    %s' % (random.choice(films)[0])


def get_players():
    """
    This function asks how many players and their names to store them and
    make the stats after the game.
    """
    i = 0
    global n_players
    try:
        n_players = int(raw_input('* Cuantos jugadores? '))
    except:
        print 'ERROR: Debe introducir un numero. Saliendo...'
        sys.exit(1)
    if n_players == 1:
        print '* ¿Me estas tomando el pelo? ¡A esto no se puede jugar solo!.'
        sys.exit(0)
    else:
        # Ojo con esto, vamos a crear la lista vacia
        fake_players = n_players - 1
        while fake_players >= 0:
            points.append(0)
            fake_players -= 1
    while i < n_players:
        player_name = raw_input('Nombre del jugador %s: ' % (i))
        players.append(player_name)
        i += 1


def get_points():
    winner = int(raw_input('* Quién ganó? (numero de jugador): '))
    points[winner] += 1
    

def endgame():
    global n_players
    films_file.close()
    end = datetime.datetime.now()
    game_time = str((end - start)).split(':')
    print " "
    print " "
    print " En una partida de %s jugadores, los resultados son:" % (n_players)
    print " "
    print " Duración: %s horas, %s minutos, %s segundos." % (game_time[0],
                                                             game_time[1],
                                               game_time[2].split('.')[0])
    print " "
    print " Puntuacion"
    print " ----------"
    print " "
    players_counter = n_players - 1
    while players_counter >= 0:
        print " %s ha conseguido %s puntos." % (players[players_counter],
                                        points[players_counter])
        players_counter -= 1
    print " "
    pos_winner = points.index(max(points))
    print " ******* Ha ganado: %s *******" % (players[pos_winner])
    print " "
    sys.exit(0)

# Set start time (due to the speed of execution we can put this here instead
# of calling it in the first game call, it just makes some microseconds more)
start = datetime.datetime.now()

# Fill the films list with film names
[films.append([line]) for line in films_file]

get_players()
players_file = open('players.txt', 'a')

while True:
    generate = raw_input('* ¿Generar película? (s/n) ')
    [endgame() if generate == 'n' or generate == 'no' else generate_random()]
    get_points()
