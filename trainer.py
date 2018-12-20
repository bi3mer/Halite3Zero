#!/usr/bin/env python3
# Python 3.6

# TODO live graph argument. If false, save to file to be overwritten

from subprocess import Popen, PIPE
from sklearn.utils import shuffle
from tqdm import tqdm
import subprocess
import glob
import os
import time

import numpy as np
from Utility.ShipModel import ShipModel


DIMENSIONS = (32, 40, 48, 56, 64)
PLAYER_COUNTS = (2, 4)
GAMES_PER_EPOCH = 1 # 4 * 2 * 4 = 64 games played before training net
MIN_HALITE_COLLECTED = 4001


class Trainer:
	def __init__(self):
		self.iterations = -1
		self.shipModel = ShipModel(True, False)

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
				line = line.split(',')

				x.append([float(i) for i in line[1:]])
				y_val = int(line[0])
				y.append([1 if y_val == i else 0 for i in range(6)])

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
		cmd.append(f'python3 training_bot.py {self.replay_name}')
		cmd += ['python3 sentedBot.py' for __ in range(player_count - 1)]

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

		return halite_collected

	def run_training_epoch(self, learn_from_self_on_win):
		total_halite_collected = 0
		self.data_files = []

		print(f'ITERATION: {self.iterations}')
		turn_count =  max(50, min(int(self.iterations/2), 250))
		print(f'Turns per game {turn_count}')

		for epoch in tqdm(range(GAMES_PER_EPOCH), desc='Epoch'):
			for dimension in tqdm(DIMENSIONS, desc='Dimension'):
				for player_count in tqdm(PLAYER_COUNTS, desc='Player Count'):
					self.player_count = player_count
					self.dimension = dimension
					self.epoch = epoch
					self.turn_count = turn_count
					self.replay_name = f'{epoch}_{dimension}_{player_count}'

					total_halite_collected += self.run_game()

		f = open('halite_collected.nsv', 'a')
		f.write(f'{total_halite_collected / float(GAMES_PER_EPOCH * len(DIMENSIONS) * len(PLAYER_COUNTS))}\n')
		f.close()

	def run_loop(self):
		while True:
			self.iterations += 1
			self.generate_command = self.play_vs_self
			self.run_training_epoch( True)
			x, y = self.create_training_data()
			self.train_model(x, y)
			self.clean_files()

if __name__ == '__main__':
	trainer = Trainer()
	trainer.run_loop()