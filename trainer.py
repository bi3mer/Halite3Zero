#!/usr/bin/env python3
# Python 3.6

from subprocess import Popen, PIPE
import subprocess
import time

DIMENSIONS = (32, 40, 48, 56, 64)
PLAYER_COUNTS = (2, 4)
GAMES_PER_EPOCH = 1 # 4 * 2 * 4 = 64 games played before training net

for i in range(GAMES_PER_EPOCH):
	for dimension in DIMENSIONS:
		for player_count in PLAYER_COUNTS:
			cmd = ['./halite', '--replay-directory', 'replays/', '--width', str(dimension), '--height', str(dimension)] 
			for i in range(player_count):
				cmd.append("python3 training_bot.py")

			process = Popen(cmd, stdout=PIPE, stderr=PIPE)
			process.wait()

# cmd = ['./halite', '--replay-directory', 'replays/', '--width', str(32), '--height', str(32), "python3 training_bot.py", "python3 training_bot.py"] 
# process = subprocess.Popen(cmd, stdin=None, stdout=None, stderr=PIPE)
# out, err = process.communicate(None, 1200)
# output = err.decode('ascii').split('\n')
# for line in output:
# 	print(line)
# 	print()
