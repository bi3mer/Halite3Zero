from hlt.positionals import Direction

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

def convert_ml_command_to_move(command, ship):
	if command == 5:
		return ship.make_dropoff()
	elif command == 1:
	    return ship.move(Direction.North)
	elif command == 2:
	    return ship.move(Direction.East)
	elif command == 3:
	    return ship.move(Direction.South)
	elif command == 4:
	    return ship.move(Direction.West)
	else:
	    return ship.stay_still()