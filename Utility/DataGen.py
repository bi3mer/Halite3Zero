from Utility.HaliteUtil import convert_move_to_ml_command
from hlt.positionals import Position
from Utility.MapData import MapData
from Utility.Math import round4

def construct_map_data(me):
	return MapData(
	    [d.position for d in list(me.get_dropoffs())] + [me.shipyard],
	    [s.position for s in list(me.get_ships())])

def world_data(game, me, max_turns):
	rounded_halite = round4(me.halite_amount, 1000000)
	turn_percentage = round4(game.turn_number, max_turns)

	return rounded_halite, turn_percentage

def generate_data(mapData, game_map, ship, size):
	data = []

	for y in range(-1 * size, size):
		row = []
		for x in range(-1 * size, size):
			row.append(mapData.get_data(game_map, ship.position + Position(x,y)))
		data.append(row)

	return data

def write_data(f, command, world_data, data):
	f.write(str(convert_move_to_ml_command(command)))
	f.write(',')
	f.write(','.join(str(item) for item in world_data))
	f.write(',')
	f.write(','.join(str(item) for item in data))
	f.write('\n')
	f.flush()

def write_data_training_bot(f, command, world_data, data):
	f.write(str(command))
	f.write(',')
	f.write(','.join(str(item) for item in world_data))
	f.write(',')
	f.write(','.join(str(item) for item in data))
	f.write('\n')
	f.flush()