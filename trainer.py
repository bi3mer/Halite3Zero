#!/usr/bin/env python3
# Python 3.6

# TODO live graph argument. If false, save to file to be overwritten

from subprocess import Popen, PIPE
from sklearn.utils import shuffle
from tqdm import tqdm
import subprocess
import glob
import os
import json
import time
import json

import numpy as np
from Utility.ShipModel import *


DIMENSIONS = (32, 40, 48, 56, 64)
PLAYER_COUNTS = (2, 4)
GAMES_PER_EPOCH = 4 # 4 * 2 * 4 = 64 games played before training net
MIN_HALITE_COLLECTED = 4001
#

class Trainer:
	def __init__(self, read_from_json):
		self.games_payed = 0
		self.halite_collected = 0
		self.iterations = -1
		self.shipModel = ShipModel(True, False)
		self.json_file_name = f'models/shipModels/{VERSION}/trainer_info.json'

		if read_from_json and os.path.isfile(self.json_file_name):
			f = open(self.json_file_name, 'r')
			data = json.load(f)
			f.close()

			self.phase1Finished = data['phase1']
			self.phase2Finished = data['phase2']
			self.phase3Finished = data['phase3']
			self.phase4Finished = data['phase4']
		else:
			self.phase1Finished = False
			self.phase2Finished = False
			self.phase3Finished = False
			self.phase4Finished = False

	def save_self_to_json(self):
		json_self = {}
		json_self['phase1'] = self.phase1Finished
		json_self['phase2'] = self.phase2Finished
		json_self['phase3'] = self.phase3Finished
		json_self['phase4'] = self.phase4Finished

		f = open(self.json_file_name, 'w')
		f.write(json.dumps(json_self))
		f.close()

	def clean_files(self):
		files = glob.glob('replays/*.hlt') + glob.glob('replays/*.log') + glob.glob('game_training_data/*')
		for f in tqdm(files, desc='Purging Data'):
			os.remove(f)

	def train_model(self, x, y):
		if len(y) > 0:
			self.shipModel.model.fit(x, y, epochs=4, batch_size=32)
			self.shipModel.save()
		else:
			self.iterations -= 1
			print('No valid training games found in this epoch')

	def create_training_data(self):
		x = []
		y = []

		for file_name in tqdm(self.data_files, desc='Training Data'):
			f = open(file_name, 'r')

			for line in f:
				y_val = int(line[0])
				y.append([1 if y_val == i else 0 for i in range(6)])

				x.append(json.loads('[' + line[2:].strip() + ']'))

			f.close()

		x = np.array(x)
		y = np.array(y)
		return shuffle(x, y)

	def base_command(self):
		cmd = ['./halite', '--replay-directory', 'replays/', '--width', str(self.dimension), '--height', str(self.dimension)]
		
		if self.turn_count < 250:
			cmd.append('--turn-limit')
			cmd.append(str(self.turn_count))

		return cmd

	def play_vs_self(self):
		cmd = self.base_command()
		python_cmd = f"python3 training_bot.py {self.replay_name}"
		cmd += [python_cmd for __ in range(self.player_count)]

		return cmd

	def play_vs_sented(self):
		cmd = self.base_command()
		cmd.append(f"python3 training_bot.py {self.replay_name}")
		cmd += [f'python3 SentedxBot.py {self.replay_name}' for __ in range(self.player_count - 1)]

		return cmd

	def sented_vs_sented(self):
		cmd = self.base_command()
		cmd += [f'python3 SentedxBot.py {self.replay_name}' for __ in range(player_count)]

		return cmd

	def play_one_ship_collect(self):
		cmd = self.base_command()
		cmd.append(f'python3 OneShipCollection.py {self.replay_name}')

		return cmd

	def run_game(self):
		# TODO use learn_from_self_on_win
		process = Popen(self.generate_command(), stdout=None, stderr=PIPE)
		out, err = process.communicate(None, 1200)
		output = err.decode('ascii').split('\n')

		halite_collected = 0
		winning_player = '0'

		for line in output:
			if 'rank 1' in line:
				halite_collected = int(line.split('rank 1')[1].split(' ')[2])
				winning_player = line.split(',')[0][-1]
				break

		if halite_collected >= MIN_HALITE_COLLECTED:
			file_name = f'game_training_data/{self.replay_name}_{winning_player}.csv'
			if os.path.isfile(file_name):
				self.data_files.append(file_name)
			else:
				print(f'ERROR: {file_name} not found')

		self.halite_collected += halite_collected
		self.games_played += 1

	def run_training_epoch(self, learn_from_self_on_win):
		total_halite_collected = 0
		self.data_files = []

		print(f'ITERATION: {self.iterations}')
		turn_count =  max(50, min(int(self.iterations/2), 250))
		print(f'Turns per game {turn_count}')
		valid_games_bar = tqdm(total=100, desc='Valid Games ')
		valid_games = 0
		games_played = 0

		while valid_games < 100:
			for epoch in tqdm(range(GAMES_PER_EPOCH), desc='Epoch       '):
				for dimension in tqdm(DIMENSIONS, desc='Dimension   '):
					for player_count in tqdm(PLAYER_COUNTS, desc='Player Count'):
						self.player_count = player_count
						self.dimension = dimension
						self.epoch = epoch
						self.turn_count = turn_count
						self.replay_name = f'{time.time()}'

						max_halite_collected = self.run_game()
						total_halite_collected += max_halite_collected

						if max_halite_collected >= MIN_HALITE_COLLECTED:
							valid_games_bar.update(1)
							valid_games += 1

						games_played += 1

	def phase1(self):
		self.generate_command = self.play_one_ship_collect
		self.turn_count = 300

		for i in tqdm(range(5000)):
			self.replay_name = str(time.time())
			self.dimension = 32
			self.run_game()

		if self.iterations >= 3:
			self.phase1Finished = True

	def phase2(self):
		pass

	def phase3(self):
		pass

	def phase4(self):
		pass

	def run_loop(self):
		while True:
			self.iterations += 1
			self.games_played = 0
			self.halite_collected = 0
			self.data_files = []

			print(f'ITERATION: {self.iterations}')
			if self.phase1Finished == False:
				self.phase1()
			elif self.phase2Finished == False:
				self.phase2()
				print("i'm at phase 2 and breaking!")
				break
			elif self.phase3Finished == False:
				self.phase3()
				break
			elif self.phase4Finished == False:
				self.phase4()
				break
			else: 
				print('Finished since there is no phase 5')
				break

			f = open('halite_collected.nsv', 'a')
			f.write(f'{self.halite_collected / float(self.games_played)},{self.games_played}\n')
			f.close()

			x, y = self.create_training_data()
			self.train_model(x, y)
			self.clean_files()
			self.save_self_to_json()

			print('----------------------------------------')

if __name__ == '__main__':
	trainer = Trainer(True)
	trainer.run_loop()