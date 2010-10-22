# -*- coding: utf-8 -*-

import sys
import random

films_file = open('lista.txt', 'r')
players_file = open('players.txt', 'w')
films = []
players = []

# LLenamos la tupla con los nombres de las películas
[films.append([line]) for line in films_file]

# Esta función saca una película al azar
def generate_random():
    print '\n    %s' % (random.choice(films)[0])

def get_players():
    i = 0
    try:
        n_players = int(raw_input('* Cuantos jugadores? '))
    except:
        print 'ERROR: Debe introducir un número. Saliendo...'
        sys.exit(1)
    while i < n_players:
        player_name = raw_input('Nombre del jugador %s: ' % (i))
        # Aqui debería grabar el nombre en el archivo players.txt
        i += 1
    players_file.close()

get_players()
players_file = open('players.txt', 'a')

while True:
    generate = raw_input('* ¿Generar película? (s/n) ')
    [sys.exit(0) if generate == 'n' or generate == 'no' else generate_random()]
    winner = raw_input('* Quien acertó (numero de jugador): ')
    players_file.write(winner)
