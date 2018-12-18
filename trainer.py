#!/usr/bin/env python3
# Python 3.6

from subprocess import Popen, PIPE
import subprocess
import time

DIMENSIONS = (32, 40, 48, 56, 64)
PLAYER_COUNTS = (1, 2, 4)
GAMES_PER_EPOCH = 4 # 15 * 4 = 60 games played before training net

processes = []
for i in range(GAMES_PER_EPOCH)
	for dimension in DIMENSIONS:
		for player_count in PLAYER_COUNTS:
			cmd = ['./halite', '--replay-directory', 'replays/', '-vvv', '--width', str(dimension), '--height', str(dimension)] 
			for i in range(player_count):
				cmd.append("python3 MyBot.py")

			processes.append(Popen(cmd, stdout=PIPE, stderr=PIPE))

	for proc in processes:
		proc.wait()