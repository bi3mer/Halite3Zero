#!/usr/bin/env python3
# Python 3.6

# heavily based one: https://www.youtube.com/watch?v=gCNIGvYbX1c&index=8&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz
#
# Open Questions:
# * maybe update this so the player matters when it's four player. Not sure.
# * do we want the width and height of the map in the net?


from hlt.positionals import Direction, Position
from hlt import constants
import logging
import random
import uuid
import hlt

game = hlt.Game()
game.ready("Biemer_Halite3Zero_Training")

SIZE = 16
f = open(f"game_training_data/{str(uuid.uuid4())}.csv", "w")

'''
0 -> stay still
1 -> North
2 -> East
3 -> South
4 -> West
5 -> construct drop off
'''
commands = [ 0, 1, 2, 3, 4, 5]


def round_halite(halite_amount, max_halite=constants.MAX_HALITE):
    return round(halite_amount / max_halite, 4)

while True:
    game.update_frame()
    me = game.me
    game_map = game.game_map
    command_queue = []

    dropoff_positions = [d.position for d in list(me.get_dropoffs())] + [me.shipyard]
    ship_positions = [s.position for s in list(me.get_ships())]

    current_halite_amount = me.halite_amount
    rounded_halite = round_halite(me.halite_amount, 1000000)

    for ship in me.get_ships():
        can_build_drop_off = 1 if current_halite_amount >= 4000 else 0s
        surroundings = [rounded_halite, can_build_drop_off]

        for y in range(-1 * SIZE, SIZE):
            for x in range(-1 * SIZE, SIZE):
                current_cell = game_map[ship.position + Position(x, y)]

                halite = current_cell.halite_amount
                halite = 0 if halite == None else round_halite(halite)

                potential_ship = current_cell.ship
                if potential_ship is None:
                    potential_ship = 0
                else: 
                    ship_friend_foe = 1 if current_cell.position in ship_positions else -1
                    potential_ship = round_halite(ship_friend_foe * potential_ship.halite_amount)

                structure =  current_cell.structure
                if structure is None:
                    structure = 0
                else:
                    structure = 1 if current_cell in dropoff_positions else -1

                surroundings.append(halite)
                surroundings.append(potential_ship)
                surroundings.append(structure)

        # replace with net and pass in surroudings and current halite amount
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
        elif command == 2:
            command_queue.append(ship.move(Direction.South))
        else:
            command_queue.append(ship.move(Direction.West))
        else command == 0:
            command_queue.append(ship.stay_still())

        f.write(str(command) + ',' + ','.join(str(item) for item in surroundings) + '\n')
        f.flush()

    # If the game is in the first 200 turns and you have enough halite, spawn a ship.
    # Don't spawn a ship if you currently have a ship at port, though - the ships will collide.
    if game.turn_number <= 200 and me.halite_amount >= constants.SHIP_COST and not game_map[me.shipyard].is_occupied:
        command_queue.append(me.shipyard.spawn())

    # Send your moves back to the game environment, ending this turn.
    game.end_turn(command_queue)
