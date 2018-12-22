#!/usr/bin/env python3
# Python 3.6

from hlt.positionals import Direction
from hlt import constants
import logging
import random
import hlt

COLLECTING = 0
RETURNING = 1

game = hlt.Game()
game.ready("bi3mer_one_ship_move_bot")
ship_states = {}

while True:
	game.update_frame()
	me = game.me
	game_map = game.game_map

	command_queue = []

	for ship in me.get_ships():
		if ship.id not in ship_states:
			ship_states[ship.id] = COLLECTING

		if ship_states[ship.id] == COLLECTING:
			if ship.halite_amount >= constants.MAX_HALITE * 0.6:
				ship_states[ship.id] = RETURNING
			else:
				if game_map[ship.position].halite_amount > 5:
					command_queue.append(ship.stay_still())
				else:
					command_queue.append(
									ship.move(
										random.choice([ Direction.North, Direction.South, Direction.East, Direction.West ])))

		if ship_states[ship.id] == RETURNING:
			if ship.position == me.shipyard.position:
				command_queue.append(ship.stay_still())
				ship_states[ship.id] = COLLECTING
			else:
				move = game_map.naive_navigate(ship, me.shipyard.position)
				command_queue.append(ship.move(move));

	if game.turn_number == 1:
		command_queue.append(me.shipyard.spawn())

	game.end_turn(command_queue)
