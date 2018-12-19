#!/usr/bin/env python3
# Python 3.6

# heavily based one: https://www.youtube.ycom/watch?v=gCNIGvYbX1c&index=8&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz
#
# Open Questions:
# * maybe update this so the player matters when it's four player. Not sure.
# * do we want the width and height of the map in the net?

from hlt.positionals import Direction, Position
from hlt import constants
from mapdata import MapData
from Utility import round_halite
import logging
import random
import time
import hlt
import sys

game = hlt.Game()
game.ready("Biemer_Halite3Zero_Training")

SIZE = 16
f = open(f"game_training_data/{sys.argv[1]}_{game.my_id}.csv", "w")

'''
0 -> stay still
1 -> North
2 -> East
3 -> South
4 -> West
5 -> construct drop off
'''
commands = [ 0, 1, 2, 3, 4, 5]

while True:
    game.update_frame()
    me = game.me
    game_map = game.game_map
    command_queue = []

    dropoff_positions = [d.position for d in list(me.get_dropoffs())] + [me.shipyard]
    ship_positions = [s.position for s in list(me.get_ships())]

    mapData = MapData(dropoff_positions, ship_positions)

    current_halite_amount = me.halite_amount
    rounded_halite = round_halite(me.halite_amount, 1000000)
    turn_percentage = round_halite(game.turn_number, constants.MAX_TURNS)

    for ship in me.get_ships():
        can_build_drop_off = 1 if current_halite_amount >= 4000 else 0
        data = [turn_percentage, rounded_halite, can_build_drop_off]

        for y in range(-1 * SIZE, SIZE):
            for x in range(-1 * SIZE, SIZE):
                halite, potential_ship, structure = mapData.get_data(game_map, ship.position + Position(x,y))

                data.append(halite)
                data.append(potential_ship)
                data.append(structure)

        # replace with net and pass in surroudings and current halite amount
        # TODO: apply move commands and make dropoff for map data
        command = random.choice(commands)

        if command == 5:
            if current_halite_amount >= 4000:
                current_halite_amount -= 4000
                command_queue.append(ship.make_dropoff())
            else:
                command_queue.append(ship.stay_still())
        elif command == 1:
            command_queue.append(ship.move(Direction.North))
        elif command == 2:
            command_queue.append(ship.move(Direction.East))
        elif command == 3:
            command_queue.append(ship.move(Direction.South))
        elif command == 4:
            command_queue.append(ship.move(Direction.West))
        else:
            command_queue.append(ship.stay_still())

        f.write(str(command) + ',' + ','.join(str(item) for item in data) + '\n')
        f.flush()

    # If the game is in the first 200 turns and you have enough halite, spawn a ship.
    # Don't spawn a ship if you currently have a ship at port, though - the ships will collide.
    if game.turn_number <= 200 and me.halite_amount >= constants.SHIP_COST and not game_map[me.shipyard].is_occupied:
        command_queue.append(me.shipyard.spawn())

    # Send your moves back to the game environment, ending this turn.
    game.end_turn(command_queue)