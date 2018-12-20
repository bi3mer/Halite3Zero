#!/usr/bin/env python3
# Python 3.6

# heavily based one: https://www.youtube.ycom/watch?v=gCNIGvYbX1c&index=8&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz
#
# Open Questions:
# * maybe update this so the player matters when it's four player. Not sure.
# * do we want the width and height of the map in the net?

from hlt.positionals import Direction, Position
from hlt import constants
from Utility.MapData import MapData
from Utility.Math import round4
import logging
import random
import time
import hlt
import sys

from Utility.ShipModel import ShipModel

game = hlt.Game()
game.ready("Biemer_Halite3Zero_Training")

SIZE = 16

'''
COMMANDS
0 -> stay still
1 -> North
2 -> East
3 -> South
4 -> West
5 -> construct drop off
'''

shipModel = ShipModel(True, True)
f = open(f"game_training_data/{sys.argv[1]}_{game.my_id}.csv", "w")

while True:
    game.update_frame()
    me = game.me
    game_map = game.game_map
    command_queue = []

    dropoff_positions = [d.position for d in list(me.get_dropoffs())] + [me.shipyard]
    ship_positions = [s.position for s in list(me.get_ships())]

    mapData = MapData(dropoff_positions, ship_positions)

    current_halite_amount = me.halite_amount
    rounded_halite = round4(me.halite_amount, 1000000)
    turn_percentage = round4(game.turn_number, constants.MAX_TURNS)

    for ship in me.get_ships():
        can_build_drop_off = 1 if current_halite_amount >= 4000 else 0
        data = [turn_percentage, rounded_halite, can_build_drop_off]

        for y in range(-1 * SIZE, SIZE):
            for x in range(-1 * SIZE, SIZE):
                halite, potential_ship, structure = mapData.get_data(game_map, ship.position + Position(x,y))

                data.append(halite)
                data.append(potential_ship)
                data.append(structure)

        command = shipModel.predict(data)
        if command == 5:
            if current_halite_amount >= 4000 and not mapData.contains_structure(game_map, ship.position):
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

    if me.halite_amount >= 1000 and turn_percentage <= 0.5 and not game_map[me.shipyard].is_occupied:
        command_queue.append(me.shipyard.spawn())

    # Send your moves back to the game environment, ending this turn.
    game.end_turn(command_queue)