#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (c) 2010 Oscar Carballal Prego <info@oscarcp.com>
#
# Distributed under terms of the MIT license.

# TODO:
# - Solve the codification problem in Windows.
# - Improve the films list to have a director and description.

# FIXME:
# - generate_random() does not print 5 spaces before text in format string

# Import python modules
import sys
import random
import datetime

# Open files and create empty lists
films_file = open('lista.txt', 'r')
films = []
players = {}


def generate_random():
    """
    This function picks a random film from the films list.
    """
    print '\n {0:>5}'.format(random.choice(films)[0])


def get_players():
    """
    This function asks how many players and their names to store them and
    make the stats after the game.
    """
    i = 0
    check = 0
    while check == 0:
        try:
            n_players = int(raw_input('* Cuantos jugadores? '))
            check = 1
        except ValueError:
            print '* ERROR: ¡Debes introducir un numero!'
    if n_players == 1:
        print '* ¿Me estas tomando el pelo? ¡A esto no se puede jugar solo!.'
        sys.exit(0)
    while i < n_players:
        player_name = raw_input('Nombre del jugador {0}: '.format(i))
        players[player_name] = 0
        i += 1


def get_points():
    try:
        winner = raw_input('* Quién ganó? (nombre de jugador): ')
        players[winner] += 1
    except:
        get_points()


def endgame():
    end = datetime.datetime.now()
    time = str((end - start)).split(':')
    counter = len(players) - 1
    p = players.items()
    final_winner = max(players, key = lambda a: players.get(a))
    print " "
    print " "
    print " En una partida de {0} jugadores, los resultados son:".format(len(players))
    print " "
    print " Duración: {0} horas, {1} minutos, {2} segundos.".format(time[0],
                                                                    time[1],
                                                      time[2].split('.')[0])
    print " "
    print " Puntuacion"
    print " ----------"
    print " "
    while counter >= 0:
        print " {0} ha conseguido {1} puntos.".format(p[counter][0],
                                                      p[counter][1])
        counter -= 1
    print " "
    print " ******* Ha ganado: {0} *******".format(final_winner)
    print " "
    sys.exit(0)

# Set start time (due to the speed of execution we can put this here instead
# of calling it in the first game call, it just makes some microseconds more)
start = datetime.datetime.now()

# Fill the films list with film names
[films.append([line]) for line in films_file]
# Now that the list is ready close the file
films_file.close()
# Bring the players to me!
get_players()

# Some kind of main loop
while True:
    generate = raw_input('* ¿Generar película? (s/n) ')
    [endgame() if generate == 'n' or generate == 'no' else generate_random()]
    get_points()
