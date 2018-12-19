#!/usr/bin/env python3
# Python 3.6

from subprocess import Popen, PIPE
from tqdm import tqdm
import subprocess
import glob
import os

DIMENSIONS = (32, 40, 48, 56, 64)
PLAYER_COUNTS = (2, 4)
GAMES_PER_EPOCH = 4 # 4 * 2 * 4 = 64 games played before training net

print("Creating game processes")
processes = []
replay_names = []
for i in range(GAMES_PER_EPOCH):
	for dimension in DIMENSIONS:
		for player_count in PLAYER_COUNTS:
			cmd = ['./halite', '--replay-directory', 'replays/', '--width', str(dimension), '--height', str(dimension)]
			replay_name = f'{i}_{dimension}_{player_count}'
			replay_names.append(replay_name)

			for j in range(player_count):
				cmd.append(f"python3 training_bot.py {replay_name}")

			processes.append(Popen(cmd, stdout=None, stderr=PIPE))

print("Playing games and figuring out results")
# TODO: get training data for the overall net which defines when something 
#       should be built
data_files = []
for index in range(len(processes)):
	out, err = processes[index].communicate(None, 1200)
	output = err.decode('ascii').split('\n')

	winning_player = '0'
	for line in output:
		if 'rank 1' in line:
			winning_player = line.split(',')[0][-1]
			break

	file_name = f'game_training_data/{replay_names[index]}_{winning_player}.csv'
	if os.path.isfile(file_name):
		data_files.append(file_name)
	else:
		print(f'ERROR: {file_name} not found')

print("Creating training data")
x = []
y = []

x = []
y = []

for file_name in data_files:
	f = open(file_name, 'r')

	for line in f:
		line = line.split(',')

		x.append([float(i) for i in line[1:]])
		y.append(line[0])

	f.close()

print("Training nets")


# clean replays folder that contains information we don't care about
print("Cleaning replay folder")
files = glob.glob('replays/*.hlt') + glob.glob('replays/*.log')
for f in files:
    os.remove(f)

# Remove csv files since we are done with them
print("Cleaning game training data")
files = glob.glob('game_training_data/*')
for f in files:
	os.remove(f)