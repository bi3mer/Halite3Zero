DROP_OFF_PRICE = 4000
SHIP_PRICE = 1000

class HaliteTracker:
	def __init__(self, halite):
		self.halite = halite

	def can_build_dropoff(self):
		return 1 if current_halite_amount >= DROP_OFF_PRICE else 0

	def buy_dropoff(self):
		if self.halite >= DROP_OFF_PRICE:
			self.halite -= DROP_OFF_PRICE
			return True

		return False

	def can_afford_ship(self):
		return self.halite >= SHIP_PRICE
