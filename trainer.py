#!/usr/bin/env python3
# Python 3.6

from subprocess import Popen, PIPE
from sklearn.utils import shuffle
from tqdm import tqdm
import subprocess
import glob
import os
import time

import numpy as np
from ShipModel import ShipModel

DIMENSIONS = (32, 40, 48, 56, 64)
PLAYER_COUNTS = (2, 4)
GAMES_PER_EPOCH = 2 # 4 * 2 * 4 = 64 games played before training net
MIN_HALITE_COLLECTED = 4001

shipModel = ShipModel(True)
iterations = -1

while True:
	iterations += 1
	halite_collected = 0
	data_files = []

	print(f'ITERATION: {iterations}')
	turn_count =  max(20, min(int(iterations/2), 250))
	print(f'Turns per game {turn_count}')

	for epoch in tqdm(range(GAMES_PER_EPOCH)):
		for dimension in tqdm(DIMENSIONS):
			for player_count in tqdm(PLAYER_COUNTS):
				cmd = ['./halite', '--replay-directory', 'replays/', '--width', str(dimension), '--height', str(dimension)]
				
				if turn_count < 250:
					cmd.append('--turn-limit')
					cmd.append(str(turn_count))

				replay_name = f'{epoch}_{dimension}_{player_count}'
				python_cmd = f"python3 training_bot.py {replay_name}"
				cmd += [python_cmd for __ in range(player_count)]

				process = Popen(cmd, stdout=None, stderr=PIPE)
				out, err = process.communicate(None, 1200)
				output = err.decode('ascii').split('\n')

				enough_halite_collected = False
				winning_player = '0'
				for line in output:
					if 'rank 1' in line:
						halite = int(line.split('rank 1')[1].split(' ')[2])
						enough_halite_collected = halite >= MIN_HALITE_COLLECTED
						halite_collected += halite
						winning_player = line.split(',')[0][-1]
						break

				if enough_halite_collected:
					file_name = f'game_training_data/{replay_name}_{winning_player}.csv'
					if os.path.isfile(file_name):
						data_files.append(file_name)
					else:
						print(f'ERROR: {file_name} not found') # means no halite was mined

	f = open('halite_collected.nsv', 'a')
	f.write(f'{halite_collected / float(GAMES_PER_EPOCH * len(DIMENSIONS) * len(PLAYER_COUNTS))}\n')
	f.close()

	print("Creating training data")
	x = []
	y = []

	for file_name in tqdm(data_files):
		f = open(file_name, 'r')

		for line in f:
			line = line.split(',')

			x.append([float(i) for i in line[1:]])
			y_val = int(line[0])
			y.append([1 if y_val == i else 0 for i in range(6)])

		f.close()

	x,y = shuffle(x, y)
	x = np.array(x)
	y = np.array(y)

	print("Training nets")
	if len(y) > 0:
		shipModel.model.fit(x, y, epochs=4, batch_size=1024)
		shipModel.save()
	else:
		print('No valid training games found in this epoch')

	print("Cleaning folders")
	files = glob.glob('replays/*.hlt') + glob.glob('replays/*.log') + glob.glob('game_training_data/*')
	for f in files:
	    os.remove(f)





# for epoch in range(GAMES_PER_EPOCH):
# 	print("Creating game processes")
# 	processes = []

# 	for dimension in DIMENSIONS:
# 		for player_count in PLAYER_COUNTS:
# 			cmd = ['./halite', '--replay-directory', 'replays/', '--width', str(dimension), '--height', str(dimension)]
# 			replay_name = f'{epoch}_{dimension}_{player_count}'
# 			replay_names.append(replay_name)

# 			for j in range(player_count):
# 				cmd.append(f"python3 training_bot.py {replay_name}")

# 			processes.append(Popen(cmd, stdout=None, stderr=PIPE))

# 	print("Playing games and figuring out results")
# 	data_files = []
# 	for index in range(len(processes)):
		# out, err = processes[index].communicate(None, 1200)
		# output = err.decode('ascii').split('\n')

		# winning_player = '0'
		# for line in output:
		# 	if 'rank 1' in line:
		# 		halite_collected += int(line.split('rank 1')[1].split(' ')[2])
		# 		winning_player = line.split(',')[0][-1]
		# 		break

		# file_name = f'game_training_data/{replay_names[index]}_{winning_player}.csv'
		# if os.path.isfile(file_name):
		# 	data_files.append(file_name)
		# else:
		# 	print(f'ERROR: {file_name} not found') # means no halite was mined