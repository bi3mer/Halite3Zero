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
import sys

import numpy as np
from Utility.ShipModel import *

DIMENSIONS = (32, 40, 48, 56, 64)
PLAYER_COUNTS = (2, 4)
GAMES_PER_EPOCH = 4
MIN_HALITE_COLLECTED = 4001

class Trainer:
	def __init__(self, read_from_json):
		self.games_payed = 0
		self.halite_collected = 0
		self.iterations = -1
		self.shipModel = ShipModel(True, False)
		self.json_file_name = f'models/shipModels/{VERSION}/trainer_info.json'
		self.base_dir = '/media/colanbiemer/My Passport/data/halite/'
		self.default_data_dir = 'game_training_data/'
		self.data_dir = self.default_data_dir
		self.phase_one_training_index = 0

		if read_from_json and os.path.isfile(self.json_file_name):
			f = open(self.json_file_name, 'r')
			data = json.load(f)
			f.close()

			self.phase1Finished = data['phase1']
			self.phase2Finished = data['phase2']
			self.phase3Finished = data['phase3']
			self.phase4Finished = data['phase4']

			self.gamma = data['gamma']
			self.epsilon = data['epsilon']
			self.epsilon_decay = data['epsilon_decay']
			self.min_epsilon = data['min_epsilon']
			self.learning_rate = data['learning_rate']
			self.batch_size = data['batch_size']

			self.phase_one_training_index = data['phase_one_training_index']
		else:
			self.phase1Finished = False
			self.phase2Finished = False
			self.phase3Finished = False
			self.phase4Finished = False

			self.gamma = 0.95
			self.epsilon = 1.000
			self.epsilon_decay = 0.99
			self.min_epsilon = 0.1
			self.learning_rate = 0.001
			self.batch_size = 512

			self.phase_one_training_index = 0

	def save_self_to_json(self):
		json_self = {}
		json_self['phase1'] = self.phase1Finished
		json_self['phase2'] = self.phase2Finished
		json_self['phase3'] = self.phase3Finished
		json_self['phase4'] = self.phase4Finished

		json_self['gamma'] = self.gamma
		json_self['epsilon'] = self.epsilon
		json_self['epsilon_decay'] = self.epsilon_decay
		json_self['min_epsilon'] = self.min_epsilon
		json_self['learning_rate'] = self.learning_rate
		json_self['batch_size'] = self.batch_size

		json_self['phase_one_training_index'] = self.phase_one_training_index

		f = open(self.json_file_name, 'w')
		f.write(json.dumps(json_self))
		f.close()

	def clean_files(self):
		files = glob.glob('replays/*.hlt') + glob.glob('replays/*.log') + glob.glob('game_training_data/*')
		for f in tqdm(files, desc='Purging Data', ascii=True):
			os.remove(f)

	def create_training_data(self, file_names):
		x_world = [] # input world data
		x_map = [] # input map data
		y = [] # command
		r = [] # reward

		for file_name in tqdm(file_names, desc='Collecting Training Data', ascii=True):
			reward = float(file_name.split('_')[-2]) / 1000.0
			f = open(file_name, 'r')

			for line in f:
				y_val = int(line[0])

				y.append([1 if y_val == i else 0 for i in range(6)])
				x_world.append([float(i) for i in line.split('[')[0][:-1].split(',')][1:])
				x_map.append(json.loads('[' + ','.join(line.split(',')[4:]) +']'))
				r.append(reward)

			f.close()

		x_world = np.array(x_world)
		x_map = np.array(x_map)
		y = np.array(y)

		return shuffle(x_world, x_map, y)

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
		cmd.append(f'python3 OneShipCollection.py "{os.path.join(self.data_dir, self.replay_name)}"')

		return cmd

	def chunker(self, l, return_list_size, current_index):
		i = current_index * return_list_size
		while i < len(l):
			new_i = i + return_list_size
			yield l[i:new_i]
			i = new_i

	def train(self, current_training_index, update_training_index):
		files_allowed = 115
		total_iterations = int(len(self.data_files) / files_allowed) + 1
		current_iteration = current_training_index

		for files in self.chunker(self.data_files, files_allowed, current_iteration):
			print(f'{current_iteration} out of {total_iterations}')
			x_world, x_map, y = self.create_training_data(files)
			
			self.shipModel.model.fit([x_map, x_world], y, epochs=1, batch_size=self.batch_size)
			self.shipModel.save()
			current_iteration += 1
			update_training_index(current_iteration)
			self.save_self_to_json()

	def q_learn(self):
		print('q learning is not implemented')
		sys.exit(0)	

		files_allowed = 115
		total_iterations = int(len(self.data_files) / files_allowed) + 1
		current_iteration = current_training_index

		for files in self.chunker(self.data_files, files_allowed, current_iteration):
			print(f'{current_iteration} out of {total_iterations}')
			x, y = self.create_training_data(files)
			
			self.shipModel.model.fit(x, y, epochs=4, batch_size=self.batch_size)
			self.shipModel.save()
			current_iteration += 1
			update_training_index(current_iteration)
			self.save_self_to_json()

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
			file_name = os.path.join(self.data_dir, f'{self.replay_name}_{winning_player}.csv')
			if os.path.isfile(file_name):
				# rename file to include the halite collected
				try:
					new_file_name = os.path.join(self.data_dir, f'{self.replay_name}_{halite_collected}_{winning_player}.csv')
					os.rename(file_name, new_file_name)

					self.data_files.append(new_file_name)
				except:
					os.remove(file_name)
			else:
				print(f'ERROR: {file_name} not found')

		# todo: delete invalid files

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
						self.replay_name = f'{time.time()}'
						self.player_count = player_count
						self.turn_count = turn_count
						self.dimension = dimension
						self.epoch = epoch

						max_halite_collected = self.run_game()
						total_halite_collected += max_halite_collected

						if max_halite_collected >= MIN_HALITE_COLLECTED:
							valid_games_bar.update(1)
							valid_games += 1

						games_played += 1

	def create_and_check_dir(self):
		if not os.path.isdir(self.data_dir):
			os.mkdir(self.data_dir)

		if not os.access(self.data_dir, os.W_OK):
			print(f'{self.data_dir} does not have write permissions')
			sys.exit(0)

	def valid_directory_structure(self):
		if not os.path.isdir(self.base_dir):
			print(f'{self.base_dir} directory does not exist and is in readonly location.')
			return False
		elif not os.access(self.base_dir, os.W_OK):
			print(f'{self.base_dir} directory does not have permissions set to allow writing.')
			return False

		return True

	def update_phase_one_iteration(self, iteration):
		self.phase_one_training_index = iteration

	def phase1(self):
		'''
		Phase 1 is to generate 15,000 games where one ship collects as much 
		halite as possible and then q learn on said games to initialize the 
		net
		'''
		self.generate_command = self.play_one_ship_collect
		self.turn_count = 300
		self.data_dir = os.path.join(self.base_dir, 'one_ship_collect/')
		self.create_and_check_dir()

		self.data_files = os.listdir(self.data_dir)
		self.data_files = [f'{self.data_dir}{file_name}' for file_name in self.data_files]

		for i in tqdm(range(len(self.data_files) - 1, 15000), desc='One Player One Ship Collection Games', ascii=True):
			self.replay_name = str(time.time())
			self.dimension = 32	
			self.run_game()

			if i % 1000 == 0:
				self.clean_files()

		print('\n\n\nTraining Phase 1')
		self.train(self.phase_one_training_index, self.update_phase_one_iteration)
		self.phase1Finished = True

	def phase2(self):
		'''
		Phase 2 is to play as many games as necessary for the bot to play against
		the Sentdex bot till it can win 99 out of 100 games
		'''
		pass

	def phase3(self):
		'''
		Phase 3 is to self play for as long as posible to get as good as possible
		at the game. Some stuff needs to be added to play against previous 
		iterations of the bot as well as the one ship and sentdex bot to make sure
		that the bot isn't getting worse over time
		'''
		pass

	def phase4(self):
		'''
		Phase 4 is the mystery phase. We'll see if we ever add this phase to the
		game
		'''
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

			if self.games_played > 0:
				f = open('halite_collected.nsv', 'a')
				f.write(f'{self.halite_collected / float(self.games_played)},{self.games_played}\n')
				f.close()

			self.clean_files()
			self.save_self_to_json()

			print('----------------------------------------')

if __name__ == '__main__':
	trainer = Trainer(True)

	if trainer.valid_directory_structure():
		print('Valid directory structure. Commencing training.')
		trainer.run_loop()