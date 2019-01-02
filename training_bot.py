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
from Utility import HaliteUtil
from Utility import DataGen
from Utility.HaliteTracker import HaliteTracker
from hlt.positionals import Direction, Position
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

f = open(f'{sys.argv[1]}_{game.my_id}.csv', 'w')

while True:
    game.update_frame()
    me = game.me
    game_map = game.game_map
    command_queue = []

    mapData = DataGen.construct_map_data(me)
    world_data = DataGen.world_data(game, me, constants.MAX_TURNS)
    haliteTracker = HaliteTracker(me.halite_amount)

    for ship in me.get_ships():
        data = DataGen.generate_data(mapData, game_map, ship, SIZE)

        command = shipModel.predict(data, world_data)
        if command == 5:
            if not haliteTracker.can_afford_dropoff() and not mapData.contains_structure(game_map, ship.position):
                haliteTracker.buy_dropoff()
            else:
                command = 0

        command_queue.append(HaliteUtil.convert_ml_command_to_move(command, ship))
        DataGen.write_data_training_bot(f, command, world_data, data)

    # if me.halite_amount >= 1000 and turn_percentage <= 0.8 and len(me.get_ships()) < 4:
    #     command_queue.append(me.shipyard.spawn())
    if len(me.get_ships()) < 1 and me.halite_amount >= constants.SHIP_COST:
        command_queue.append(me.shipyard.spawn())

    # Send your moves back to the game environment, ending this turn.
    game.end_turn(command_queue)