from Utility import round_halite
from hlt import constants

# TODO
# * implement ability to move a ship on the map

class MapData:
	def __init__(self, dropoff_positions, ship_positions):
		self.data = {}
		self.dropoff_positions = dropoff_positions
		self.ship_positions = ship_positions

	def get_data(self, game_map, position):
		if position not in self.data:
			current_cell = game_map[position]

			halite = current_cell.halite_amount
			halite = 0 if halite == None else round_halite(halite, constants.MAX_HALITE)

			potential_ship = current_cell.ship
			if potential_ship is None:
			    potential_ship = 0
			else: 
			    ship_friend_foe = 1 if current_cell.position in self.ship_positions else -1
			    potential_ship = round_halite(ship_friend_foe * potential_ship.halite_amount, constants.MAX_HALITE)

			structure =  current_cell.structure
			if structure is None:
			    structure = 0
			else:
				structure = 1 if current_cell in self.dropoff_positions else -1

			self.data[position] = (halite, potential_ship, structure)

		return self.data[position]

