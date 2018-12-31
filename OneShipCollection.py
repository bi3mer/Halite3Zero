#!/usr/bin/env python3
# Python 3.6

from Utility.MapData import MapData
from Utility.Math import round4
from hlt.positionals import Direction, Position
from hlt import constants
import logging
import random
import sys
import hlt

SIZE = 16
SEARCH_SIZE = 6

COLLECTING = 0
RETURNING = 1

game = hlt.Game()
game.ready("bi3mer_one_ship_move_bot")
ship_states = {}
ship_targets = {}

move_directions = [ Direction.North, Direction.South, Direction.East, Direction.West ]

f = open(f"game_training_data/{sys.argv[1]}_{game.my_id}.csv", "w")

def dist(a, b):
	return abs(a.y - b.y) + abs(a.x - b.x)

def acquire_target(game_map, ship_position):
	best_halite_over_dist = 0
	best_position = None

	for y in range(-1 * SEARCH_SIZE, SEARCH_SIZE):
		for x in range(-1 * SEARCH_SIZE, SEARCH_SIZE):
			cell_position = ship.position + Position(x,y)
			cell_halite_amount = game_map[cell_position].halite_amount
			distance = float(dist(ship_position, cell_position))
			halite_over_dist = 0 if distance == 0 else cell_halite_amount / distance

			if halite_over_dist >= best_halite_over_dist:
				best_halite_over_dist = halite_over_dist
				best_position = cell_position

	return best_position

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

while True:
	game.update_frame()
	me = game.me
	game_map = game.game_map

	command_queue = []

	mapData = MapData(
	    [d.position for d in list(me.get_dropoffs())] + [me.shipyard],
	    [s.position for s in list(me.get_ships())])

	current_halite_amount = me.halite_amount
	rounded_halite = round4(me.halite_amount, 1000000)
	turn_percentage = round4(game.turn_number, constants.MAX_TURNS)

	for ship in me.get_ships():
		command = 0

		can_build_drop_off = 1 if current_halite_amount >= 4000 else 0
		world_data = [turn_percentage, rounded_halite, can_build_drop_off]
		data = []

		for y in range(-1 * SIZE, SIZE):
		    row = []
		    for x in range(-1 * SIZE, SIZE):
		        row.append(mapData.get_data(game_map, ship.position + Position(x,y)) + world_data)
		    data.append(row)

		if ship.id not in ship_states:
			ship_states[ship.id] = COLLECTING
			ship_targets[ship.id] = acquire_target(game_map, ship.position)

		if ship_states[ship.id] == COLLECTING:
			if ship.halite_amount >= constants.MAX_HALITE * 0.8:
				ship_states[ship.id] = RETURNING
			else:
				if ship_targets[ship.id] == ship.position:
					ship_targets[ship.id] = acquire_target(game_map, ship.position)

				if game_map[ship.position].halite_amount > 5:
					command_queue.append(ship.stay_still())
				else:
					command = game_map.naive_navigate(ship, ship_targets[ship.id])
					command_queue.append(ship.move(command));

		if ship_states[ship.id] == RETURNING:
			if ship.position == me.shipyard.position:
				command_queue.append(ship.stay_still())
				ship_states[ship.id] = COLLECTING
				ship_targets[ship.id] = acquire_target(game_map, ship.position)
			else:
				command = game_map.naive_navigate(ship, me.shipyard.position)
				command_queue.append(ship.move(command));

		f.write(str(convert_move_to_ml_command(command)) + ',' + ','.join(str(item) for item in data) + '\n')
		f.flush()

	if len(me.get_ships()) < 1 and me.halite_amount >= constants.SHIP_COST:
		command_queue.append(me.shipyard.spawn())


	game.end_turn(command_queue)