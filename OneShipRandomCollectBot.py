#!/usr/bin/env python3
# Python 3.6

from hlt.positionals import Direction, Position
from hlt import constants
import logging
import random
import hlt

SEARCH_SIZE = 6

COLLECTING = 0
RETURNING = 1

game = hlt.Game()
game.ready("bi3mer_one_ship_move_bot")
ship_states = {}
ship_targets = {}

move_directions = [ Direction.North, Direction.South, Direction.East, Direction.West ]

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

while True:
	game.update_frame()
	me = game.me
	game_map = game.game_map

	command_queue = []

	for ship in me.get_ships():
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
					logging.info(game_map[ship.position].halite_amount)
					command_queue.append(ship.stay_still())
				else:
					move = game_map.naive_navigate(ship, ship_targets[ship.id])
					command_queue.append(ship.move(move));

		if ship_states[ship.id] == RETURNING:
			if ship.position == me.shipyard.position:
				command_queue.append(ship.stay_still())
				ship_states[ship.id] = COLLECTING
				ship_targets[ship.id] = acquire_target(game_map, ship.position)
			else:
				move = game_map.naive_navigate(ship, me.shipyard.position)
				command_queue.append(ship.move(move));

		logging.info(ship_states[ship.id])

	if len(me.get_ships()) < 1 and me.halite_amount >= constants.SHIP_COST:
		command_queue.append(me.shipyard.spawn())


	game.end_turn(command_queue)