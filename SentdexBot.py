# Python 3.6
# src: https://pythonprogramming.net/cleaning-up-halite-iii-ai-coding-competition/
import logging
import hlt  #main halite stuff
from hlt import constants  # halite constants
from hlt.positionals import Direction, Position  # helper for moving
import random  # randomly picking a choice for now.
import math
import sys

from Utility.MapData import MapData
from Utility.Math import round4

game = hlt.Game()  # game object
# Initializes the game
game.ready("Sentdebot")

SIZE = 16

f = open(f"{sys.argv[1]}_{game.my_id}.csv", "w")

def convert_move_to_ml_command(move):
    '''
    COMMANDS
    0 -> stay still
    1 -> North
    2 -> East
    3 -> South
    4 -> West
    5 -> construct drop off
    '''
    if type(move) == int:
        return move
    elif move == Direction.Still:
        return 0
    elif move == Direction.North:
        return 1
    elif move == Direction.East:
        return 2
    elif move == Direction.South:
        return 3
    elif move == Direction.West:
        return 4
    else:
        return 5

ship_states = {}
while True:
    game.update_frame()
    logging.info('you have to work here')
    me = game.me
    game_map = game.game_map  # game map data. Recall game is
    command_queue = []
    direction_order = [Direction.North, Direction.South, Direction.East, Direction.West, Direction.Still]

    mapData = MapData(
        [d.position for d in list(me.get_dropoffs())] + [me.shipyard],
        [s.position for s in list(me.get_ships())])

    current_halite_amount = me.halite_amount
    rounded_halite = round4(me.halite_amount, 1000000)
    turn_percentage = round4(game.turn_number, constants.MAX_TURNS)

    position_choices = []
    for ship in me.get_ships():
        logging.info("i am always here")
        command = -1

        can_build_drop_off = 1 if current_halite_amount >= 4000 else 0
        world_data = [turn_percentage, rounded_halite, can_build_drop_off]
        data = []

        for y in range(-1 * SIZE, SIZE):
            row = []
            for x in range(-1 * SIZE, SIZE):
                row.append(mapData.get_data(game_map, ship.position + Position(x,y)) + world_data)
            data.append(row)

        if ship.id not in ship_states:
            ship_states[ship.id] = "collecting"

        if ship_states[ship.id] == "collecting":
            position_options = ship.position.get_surrounding_cardinals() + [ship.position]
            position_dict = {}
            halite_dict = {}

            for n, direction in enumerate(direction_order):
                position_dict[direction] = position_options[n]

            for direction in position_dict:
                position = position_dict[direction]
                halite_amount = game_map[position].halite_amount
                if position_dict[direction] not in position_choices:
                    if direction == Direction.Still:
                        halite_amount *= 4
                    halite_dict[direction] = halite_amount

            directional_choice = max(halite_dict, key=halite_dict.get)
            position_choices.append(position_dict[directional_choice])

            command = ship.move(game_map.naive_navigate(ship, ship.position+Position(*directional_choice)))
            command_queue.append(command);

            if ship.halite_amount >= constants.MAX_HALITE * 0.75:
                ship_states[ship.id] = "depositing"

        elif ship_states[ship.id] == "depositing":
            move = game_map.naive_navigate(ship, me.shipyard.position)
            command = move
            upcoming_position = ship.position + Position(*move)
            if upcoming_position not in position_choices:
                position_choices.append(upcoming_position)
                command_queue.append(ship.move(move))
                if move == Direction.Still:
                    ship_states[ship.id] = "collecting"
            else:
                position_choices.append(ship.position)
                command = ship.move(game_map.naive_navigate(ship, ship.position+Position(*Direction.Still)))
                command_queue.append(command)

        logging.info('i am here')
        logging.info(command)
        logging.info(convert_move_to_ml_command(command))
        f.write(str(convert_move_to_ml_command(command)) + ',' + ','.join(str(item) for item in data) + '\n')
        f.flush()

    # ship costs 1000, dont make a ship on a ship or they both sink
    if not game.turn_number > constants.MAX_TURNS *.75 and len(me.get_ships()) < math.ceil(game.turn_number / 25):
        if me.halite_amount >= 1000 and not game_map[me.shipyard].is_occupied:
            command_queue.append(me.shipyard.spawn())

    game.end_turn(command_queue)