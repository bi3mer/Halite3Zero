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
GAMES_PER_EPOCH = 4 # 4 * 2 * 4 = 64 games played before training net
MIN_HALITE_COLLECTED = 4001

shipModel = ShipModel(True, False)
iterations = -1

def clean_files():
	files = glob.glob('replays/*.hlt') + glob.glob('replays/*.log') + glob.glob('game_training_data/*')
	for f in tqdm(files, desc='Purging Data'):
		os.remove(f)

def train_model(x, y):
	if len(y) > 0:
		shipModel.model.fit(x, y, epochs=4, batch_size=1024)
		shipModel.save()
	else:
		iterations -= 1
		print('No valid training games found in this epoch')

def create_training_data(data_files):
	x = []
	y = []

	for file_name in tqdm(data_files, desc='Training Data'):
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

def base_command(epoch, dimension, turn_count):
	cmd = ['./halite', '--replay-directory', 'replays/', '--width', str(dimension), '--height', str(dimension)]
	
	if turn_count < 250:
		cmd.append('--turn-limit')
		cmd.append(str(turn_count))

	return cmd

def play_vs_self(epoch, dimension, player_count, turn_count, replay_name):
	cmd = base_command(epoch, dimension, turn_count)
	python_cmd = f"python3 training_bot.py {replay_name}"
	cmd += [python_cmd for __ in range(player_count)]
	return cmd

def play_vs_sented(epoch, dimension, player_count, turn_count, replay_name):
	cmd = base_command(epoch, dimension, turn_count)
	cmd.append(f'python3 training_bot.py {replay_name}')
	cmd += ['python3 sentedBot.py' for __ in range(player_count - 1)]
	return cmd

def run_game(cmd, replay_name, data_files):
	process = Popen(cmd, stdout=None, stderr=PIPE)
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
		file_name = f'game_training_data/{replay_name}_{winning_player}.csv'
		if os.path.isfile(file_name):
			data_files.append(file_name)
		else:
			print(f'ERROR: {file_name} not found')

	return halite_collected

def run_training_epoch(cmd_generator):
	total_halite_collected = 0
	data_files = []

	print(f'ITERATION: {iterations}')
	turn_count =  max(100, min(int(iterations/2), 250))
	print(f'Turns per game {turn_count}')

	for epoch in tqdm(range(GAMES_PER_EPOCH), desc='Epoch'):
		for dimension in tqdm(DIMENSIONS, desc='Dimension'):
			for player_count in tqdm(PLAYER_COUNTS, desc='Player Count'):
				replay_name = f'{epoch}_{dimension}_{player_count}'
				cmd = cmd_generator(epoch, dimension, player_count, turn_count, replay_name)
				total_halite_collected += run_game(cmd, replay_name, data_files)

	f = open('halite_collected.nsv', 'a')
	f.write(f'{halite_collected / float(GAMES_PER_EPOCH * len(DIMENSIONS) * len(PLAYER_COUNTS))}\n')
	f.close()

	return data_files

def main():
	global iterations
	global shipModel

	while True:
		iterations += 1

		cmd_generator = play_vs_self # removed sentedbot
		if iterations > 50:
			cmd_generator = play_vs_self

		data_files = run_training_epoch(cmd_generator)
		x, y = create_training_data(data_files)
		train_model(x, y)
		clean_files()		

if __name__ == '__main__':
	main()