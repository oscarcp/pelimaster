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


class Game():

    def __init__(self):
        """
        Start everything. Declare dictionaries and lists, open files and get
        all the content ready.
        """
        self.films_file = open('lista.txt', 'r')
        self.films = []
        self.players = {}

        [self.films.append([line]) for line in self.films_file]
        self.films_file.close()

    def _end(self):
        """
        This function terminates the game, after showing a basic statistic of
        the game.
        """
        self.end_time = datetime.datetime.now()
        self.t = str((self.end_time - self.start_time)).split(':')
        self.counter = len(self.players) - 1
        self.p = self.players.items()
        self.fwinner = max(self.players, key = lambda a: self.players.get(a))
        print "\n\n En una partida de {0} jugadores, los resultados son:\n".format(len(self.players))
        print " Duración: {0} horas, {1} minutos, {2} segundos.\n".format(self.t[0],
                                                                          self.t[1],
                                                                          self.t[2].split('.')[0])
        print " Puntuacion\n ----------\n"
        while self.counter >= 0:
            print " {0} ha conseguido {1} puntos.".format(self.p[self.counter][0],
                                                          self.p[self.counter][1])
            self.counter -= 1
        print "\n ******* Ha ganado: {0} *******\n".format(self.fwinner)
        # Clear everything
        del self.films[:]
        self.players.clear()
        sys.exit(0)

    def _get_players(self):
        """
        This function asks the number of players and their names. Names are
        stored in a dictionary as a key with a value of zero for every player.
        """
        self.i = 0
        self.check = 0
        while self.check == 0:
            try:
                self.n_players = int(raw_input('* Cuantos jugadores? '))
                self.check = 1
            except ValueError:
                print '* ERROR: ¡Debes introducir un numero!'
        if self.n_players == 1:
            print '* ¿Me estas tomando el pelo? ¡A esto no se puede jugar solo!.'
            sys.exit(0)
        while self.i < self.n_players:
            self.player_name = raw_input('Nombre del jugador {0}: '.format(self.i))
            self.players[self.player_name] = 0
            self.i += 1

    def _get_points(self):
        """
        This function stores the points earned by a player. It simply increases
        the number of the value by one in the pair [key,value].
        """
        try:
            self.winner = raw_input('* Quién ganó? (nombre de jugador): ')
            self.players[self.winner] += 1
        except:
            self._get_points()

    def _get_film(self):
        """
        This function gets a random film from the film list.
        """
        print '\n {0:>5}'.format(random.choice(self.films)[0])

    def start(self):
        """
        This function starts the game. It gets the time when the game is
        started and enters a loop asking to generate a new film. If the player
        does not want a new film _end() is executed.
        """
        self._get_players()
        self.start_time = datetime.datetime.now()
        while True:
            self.generate = raw_input('* ¿Generar película? (s/n) ')
            if self.generate == 'n' or self.generate == 'no':
                self._end()
            else:
                self._get_film()
                self._get_points()

if __name__ == '__main__':
    game = Game()
    game.start()
