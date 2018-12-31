# from tensorflow import keras
# from tensorflow.keras.models import Model

from tqdm import tqdm
import numpy as np
import json
import time
import os

# import tensorflow as tf


for i in tqdm(range(50, 100)):
	time.sleep(0.1)

# f = open('game_training_data/1234_0.csv', 'r')
# for line in f:
# 	y = int(line[0])
# 	matrix = '[' + line[2:].strip() + ']'
# 	# print(matrix)
# 	print(json.loads(matrix))

# 	break	
# f.close()

# halite_dir = '/data/projects/halite/'
# directory = f'{halite_dir}one_ship_collect/'

# if not os.path.isdir(directory):
# 	os.mkdir(directory)

# np.set_printoptions(threshold=np.nan)
# t = [[[0.022, 0, 0, 0.04, 0.004, 1], [0.032, 0, 0, 0.04, 0.004, 1], [0.059, 0, 0, 0.04, 0.004, 1], [0.212, 0, 0, 0.04, 0.004, 1], [0.206, 0, 0, 0.04, 0.004, 1], [0.023, 0, 0, 0.04, 0.004, 1], [0.048, 0, 0, 0.04, 0.004, 1], [0.023, 0, 0, 0.04, 0.004, 1], [0.023, 0, 0, 0.04, 0.004, 1], [0.048, 0, 0, 0.04, 0.004, 1], [0.023, 0, 0, 0.04, 0.004, 1], [0.206, 0, 0, 0.04, 0.004, 1], [0.212, 0, 0, 0.04, 0.004, 1], [0.059, 0, 0, 0.04, 0.004, 1], [0.032, 0, 0, 0.04, 0.004, 1], [0.022, 0, 0, 0.04, 0.004, 1], [0.006, 0, 0, 0.04, 0.004, 1], [0.013, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.017, 0, 0, 0.04, 0.004, 1], [0.01, 0, 0, 0.04, 0.004, 1], [0.019, 0, 0, 0.04, 0.004, 1], [0.011, 0, 0, 0.04, 0.004, 1], [0.014, 0, 0, 0.04, 0.004, 1], [0.014, 0, 0, 0.04, 0.004, 1], [0.011, 0, 0, 0.04, 0.004, 1], [0.019, 0, 0, 0.04, 0.004, 1], [0.01, 0, 0, 0.04, 0.004, 1], [0.017, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.013, 0, 0, 0.04, 0.004, 1], [0.006, 0, 0, 0.04, 0.004, 1]], [[0.029, 0, 0, 0.04, 0.004, 1], [0.052, 0, 0, 0.04, 0.004, 1], [0.076, 0, 0, 0.04, 0.004, 1], [0.083, 0, 0, 0.04, 0.004, 1], [0.083, 0, 0, 0.04, 0.004, 1], [0.097, 0, 0, 0.04, 0.004, 1], [0.044, 0, 0, 0.04, 0.004, 1], [0.038, 0, 0, 0.04, 0.004, 1], [0.038, 0, 0, 0.04, 0.004, 1], [0.044, 0, 0, 0.04, 0.004, 1], [0.097, 0, 0, 0.04, 0.004, 1], [0.083, 0, 0, 0.04, 0.004, 1], [0.083, 0, 0, 0.04, 0.004, 1], [0.076, 0, 0, 0.04, 0.004, 1], [0.052, 0, 0, 0.04, 0.004, 1], [0.029, 0, 0, 0.04, 0.004, 1], [0.022, 0, 0, 0.04, 0.004, 1], [0.031, 0, 0, 0.04, 0.004, 1], [0.034, 0, 0, 0.04, 0.004, 1], [0.131, 0, 0, 0.04, 0.004, 1], [0.024, 0, 0, 0.04, 0.004, 1], [0.116, 0, 0, 0.04, 0.004, 1], [0.071, 0, 0, 0.04, 0.004, 1], [0.076, 0, 0, 0.04, 0.004, 1], [0.076, 0, 0, 0.04, 0.004, 1], [0.071, 0, 0, 0.04, 0.004, 1], [0.116, 0, 0, 0.04, 0.004, 1], [0.024, 0, 0, 0.04, 0.004, 1], [0.131, 0, 0, 0.04, 0.004, 1], [0.034, 0, 0, 0.04, 0.004, 1], [0.031, 0, 0, 0.04, 0.004, 1], [0.022, 0, 0, 0.04, 0.004, 1]], [[0.029, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.057, 0, 0, 0.04, 0.004, 1], [0.057, 0, 0, 0.04, 0.004, 1], [0.119, 0, 0, 0.04, 0.004, 1], [0.073, 0, 0, 0.04, 0.004, 1], [0.194, 0, 0, 0.04, 0.004, 1], [0.13, 0, 0, 0.04, 0.004, 1], [0.13, 0, 0, 0.04, 0.004, 1], [0.194, 0, 0, 0.04, 0.004, 1], [0.073, 0, 0, 0.04, 0.004, 1], [0.119, 0, 0, 0.04, 0.004, 1], [0.057, 0, 0, 0.04, 0.004, 1], [0.057, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.029, 0, 0, 0.04, 0.004, 1], [0.02, 0, 0, 0.04, 0.004, 1], [0.059, 0, 0, 0.04, 0.004, 1], [0.127, 0, 0, 0.04, 0.004, 1], [0.062, 0, 0, 0.04, 0.004, 1], [0.142, 0, 0, 0.04, 0.004, 1], [0.132, 0, 0, 0.04, 0.004, 1], [0.081, 0, 0, 0.04, 0.004, 1], [0.211, 0, 0, 0.04, 0.004, 1], [0.211, 0, 0, 0.04, 0.004, 1], [0.081, 0, 0, 0.04, 0.004, 1], [0.132, 0, 0, 0.04, 0.004, 1], [0.142, 0, 0, 0.04, 0.004, 1], [0.062, 0, 0, 0.04, 0.004, 1], [0.127, 0, 0, 0.04, 0.004, 1], [0.059, 0, 0, 0.04, 0.004, 1], [0.02, 0, 0, 0.04, 0.004, 1]], [[0.026, 0, 0, 0.04, 0.004, 1], [0.045, 0, 0, 0.04, 0.004, 1], [0.107, 0, 0, 0.04, 0.004, 1], [0.147, 0, 0, 0.04, 0.004, 1], [0.088, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.221, 0, 0, 0.04, 0.004, 1], [0.108, 0, 0, 0.04, 0.004, 1], [0.108, 0, 0, 0.04, 0.004, 1], [0.221, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.088, 0, 0, 0.04, 0.004, 1], [0.147, 0, 0, 0.04, 0.004, 1], [0.107, 0, 0, 0.04, 0.004, 1], [0.045, 0, 0, 0.04, 0.004, 1], [0.026, 0, 0, 0.04, 0.004, 1], [0.015, 0, 0, 0.04, 0.004, 1], [0.12, 0, 0, 0.04, 0.004, 1], [0.037, 0, 0, 0.04, 0.004, 1], [0.054, 0, 0, 0.04, 0.004, 1], [0.035, 0, 0, 0.04, 0.004, 1], [0.123, 0, 0, 0.04, 0.004, 1], [0.051, 0, 0, 0.04, 0.004, 1], [0.094, 0, 0, 0.04, 0.004, 1], [0.094, 0, 0, 0.04, 0.004, 1], [0.051, 0, 0, 0.04, 0.004, 1], [0.123, 0, 0, 0.04, 0.004, 1], [0.035, 0, 0, 0.04, 0.004, 1], [0.054, 0, 0, 0.04, 0.004, 1], [0.037, 0, 0, 0.04, 0.004, 1], [0.12, 0, 0, 0.04, 0.004, 1], [0.015, 0, 0, 0.04, 0.004, 1]], [[0.044, 0, 0, 0.04, 0.004, 1], [0.054, 0, 0, 0.04, 0.004, 1], [0.148, 0, 0, 0.04, 0.004, 1], [0.141, 0, 0, 0.04, 0.004, 1], [0.124, 0, 0, 0.04, 0.004, 1], [0.277, 0, 0, 0.04, 0.004, 1], [0.113, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.113, 0, 0, 0.04, 0.004, 1], [0.277, 0, 0, 0.04, 0.004, 1], [0.124, 0, 0, 0.04, 0.004, 1], [0.141, 0, 0, 0.04, 0.004, 1], [0.148, 0, 0, 0.04, 0.004, 1], [0.054, 0, 0, 0.04, 0.004, 1], [0.044, 0, 0, 0.04, 0.004, 1], [0.029, 0, 0, 0.04, 0.004, 1], [0.021, 0, 0, 0.04, 0.004, 1], [0.053, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.026, 0, 0, 0.04, 0.004, 1], [0.034, 0, 0, 0.04, 0.004, 1], [0.06, 0, 0, 0.04, 0.004, 1], [0.08, 0, 0, 0.04, 0.004, 1], [0.08, 0, 0, 0.04, 0.004, 1], [0.06, 0, 0, 0.04, 0.004, 1], [0.034, 0, 0, 0.04, 0.004, 1], [0.026, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.053, 0, 0, 0.04, 0.004, 1], [0.021, 0, 0, 0.04, 0.004, 1], [0.029, 0, 0, 0.04, 0.004, 1]], [[0.138, 0, 0, 0.04, 0.004, 1], [0.115, 0, 0, 0.04, 0.004, 1], [0.123, 0, 0, 0.04, 0.004, 1], [0.113, 0, 0, 0.04, 0.004, 1], [0.219, 0, 0, 0.04, 0.004, 1], [0.179, 0, 0, 0.04, 0.004, 1], [0.221, 0, 0, 0.04, 0.004, 1], [0.376, 0, 0, 0.04, 0.004, 1], [0.376, 0, 0, 0.04, 0.004, 1], [0.221, 0, 0, 0.04, 0.004, 1], [0.179, 0, 0, 0.04, 0.004, 1], [0.219, 0, 0, 0.04, 0.004, 1], [0.113, 0, 0, 0.04, 0.004, 1], [0.123, 0, 0, 0.04, 0.004, 1], [0.115, 0, 0, 0.04, 0.004, 1], [0.138, 0, 0, 0.04, 0.004, 1], [0.041, 0, 0, 0.04, 0.004, 1], [0.113, 0, 0, 0.04, 0.004, 1], [0.051, 0, 0, 0.04, 0.004, 1], [0.062, 0, 0, 0.04, 0.004, 1], [0.1, 0, 0, 0.04, 0.004, 1], [0.103, 0, 0, 0.04, 0.004, 1], [0.123, 0, 0, 0.04, 0.004, 1], [0.218, 0, 0, 0.04, 0.004, 1], [0.218, 0, 0, 0.04, 0.004, 1], [0.123, 0, 0, 0.04, 0.004, 1], [0.103, 0, 0, 0.04, 0.004, 1], [0.1, 0, 0, 0.04, 0.004, 1], [0.062, 0, 0, 0.04, 0.004, 1], [0.051, 0, 0, 0.04, 0.004, 1], [0.113, 0, 0, 0.04, 0.004, 1], [0.041, 0, 0, 0.04, 0.004, 1]], [[0.03, 0, 0, 0.04, 0.004, 1], [0.07, 0, 0, 0.04, 0.004, 1], [0.231, 0, 0, 0.04, 0.004, 1], [0.194, 0, 0, 0.04, 0.004, 1], [0.199, 0, 0, 0.04, 0.004, 1], [0.152, 0, 0, 0.04, 0.004, 1], [0.219, 0, 0, 0.04, 0.004, 1], [0.537, 0, 0, 0.04, 0.004, 1], [0.537, 0, 0, 0.04, 0.004, 1], [0.219, 0, 0, 0.04, 0.004, 1], [0.152, 0, 0, 0.04, 0.004, 1], [0.199, 0, 0, 0.04, 0.004, 1], [0.194, 0, 0, 0.04, 0.004, 1], [0.231, 0, 0, 0.04, 0.004, 1], [0.07, 0, 0, 0.04, 0.004, 1], [0.03, 0, 0, 0.04, 0.004, 1], [0.008, 0, 0, 0.04, 0.004, 1], [0.073, 0, 0, 0.04, 0.004, 1], [0.194, 0, 0, 0.04, 0.004, 1], [0.171, 0, 0, 0.04, 0.004, 1], [0.365, 0, 0, 0.04, 0.004, 1], [0.226, 0, 0, 0.04, 0.004, 1], [0.438, 0, 0, 0.04, 0.004, 1], [0.297, 0, 0, 0.04, 0.004, 1], [0.297, 0, 0, 0.04, 0.004, 1], [0.438, 0, 0, 0.04, 0.004, 1], [0.226, 0, 0, 0.04, 0.004, 1], [0.365, 0, 0, 0.04, 0.004, 1], [0.171, 0, 0, 0.04, 0.004, 1], [0.194, 0, 0, 0.04, 0.004, 1], [0.073, 0, 0, 0.04, 0.004, 1], [0.008, 0, 0, 0.04, 0.004, 1]], [[0.126, 0, 0, 0.04, 0.004, 1], [0.111, 0, 0, 0.04, 0.004, 1], [0.068, 0, 0, 0.04, 0.004, 1], [0.081, 0, 0, 0.04, 0.004, 1], [0.118, 0, 0, 0.04, 0.004, 1], [0.302, 0, 0, 0.04, 0.004, 1], [0.298, 0, 0, 0.04, 0.004, 1], [0.453, 0, 0, 0.04, 0.004, 1], [0.453, 0, 0, 0.04, 0.004, 1], [0.298, 0, 0, 0.04, 0.004, 1], [0.302, 0, 0, 0.04, 0.004, 1], [0.118, 0, 0, 0.04, 0.004, 1], [0.081, 0, 0, 0.04, 0.004, 1], [0.068, 0, 0, 0.04, 0.004, 1], [0.111, 0, 0, 0.04, 0.004, 1], [0.126, 0, 0, 0.04, 0.004, 1], [0.008, 0, 0, 0.04, 0.004, 1], [0.045, 0, 0, 0.04, 0.004, 1], [0.123, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.153, 0, 0, 0.04, 0.004, 1], [0.208, 0, 0, 0.04, 0.004, 1], [0.286, 0, 0, 0.04, 0.004, 1], [0.347, 0, 0, 0.04, 0.004, 1], [0.347, 0, 0, 0.04, 0.004, 1], [0.286, 0, 0, 0.04, 0.004, 1], [0.208, 0, 0, 0.04, 0.004, 1], [0.153, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.123, 0, 0, 0.04, 0.004, 1], [0.045, 0, 0, 0.04, 0.004, 1], [0.008, 0, 0, 0.04, 0.004, 1]], [[0.06, 0, 0, 0.04, 0.004, 1], [0.235, 0, 0, 0.04, 0.004, 1], [0.11, 0, 0, 0.04, 0.004, 1], [0.038, 0, 0, 0.04, 0.004, 1], [0.116, 0, 0, 0.04, 0.004, 1], [0.35, 0, 0, 0.04, 0.004, 1], [0.672, 0, 0, 0.04, 0.004, 1], [0.942, 0, 0, 0.04, 0.004, 1], [0.942, 0, 0, 0.04, 0.004, 1], [0.672, 0, 0, 0.04, 0.004, 1], [0.35, 0, 0, 0.04, 0.004, 1], [0.116, 0, 0, 0.04, 0.004, 1], [0.038, 0, 0, 0.04, 0.004, 1], [0.11, 0, 0, 0.04, 0.004, 1], [0.235, 0, 0, 0.04, 0.004, 1], [0.06, 0, 0, 0.04, 0.004, 1], [0.012, 0, 0, 0.04, 0.004, 1], [0.05, 0, 0, 0.04, 0.004, 1], [0.256, 0, 0, 0.04, 0.004, 1], [0.218, 0, 0, 0.04, 0.004, 1], [0.229, 0, 0, 0.04, 0.004, 1], [0.394, 0, 0, 0.04, 0.004, 1], [0.414, 0, 0, 0.04, 0.004, 1], [0.68, 0, 0, 0.04, 0.004, 1], [0.68, 0, 0, 0.04, 0.004, 1], [0.414, 0, 0, 0.04, 0.004, 1], [0.394, 0, 0, 0.04, 0.004, 1], [0.229, 0, 0, 0.04, 0.004, 1], [0.218, 0, 0, 0.04, 0.004, 1], [0.256, 0, 0, 0.04, 0.004, 1], [0.05, 0, 0, 0.04, 0.004, 1], [0.012, 0, 0, 0.04, 0.004, 1]], [[0.075, 0, 0, 0.04, 0.004, 1], [0.207, 0, 0, 0.04, 0.004, 1], [0.239, 0, 0, 0.04, 0.004, 1], [0.136, 0, 0, 0.04, 0.004, 1], [0.129, 0, 0, 0.04, 0.004, 1], [0.247, 0, 0, 0.04, 0.004, 1], [0.577, 0, 0, 0.04, 0.004, 1], [0.654, 0, 0, 0.04, 0.004, 1], [0.654, 0, 0, 0.04, 0.004, 1], [0.577, 0, 0, 0.04, 0.004, 1], [0.247, 0, 0, 0.04, 0.004, 1], [0.129, 0, 0, 0.04, 0.004, 1], [0.136, 0, 0, 0.04, 0.004, 1], [0.239, 0, 0, 0.04, 0.004, 1], [0.207, 0, 0, 0.04, 0.004, 1], [0.075, 0, 0, 0.04, 0.004, 1], [0.024, 0, 0, 0.04, 0.004, 1], [0.166, 0, 0, 0.04, 0.004, 1], [0.132, 0, 0, 0.04, 0.004, 1], [0.111, 0, 0, 0.04, 0.004, 1], [0.144, 0, 0, 0.04, 0.004, 1], [0.173, 0, 0, 0.04, 0.004, 1], [0.386, 0, 0, 0.04, 0.004, 1], [0.373, 0, 0, 0.04, 0.004, 1], [0.373, 0, 0, 0.04, 0.004, 1], [0.386, 0, 0, 0.04, 0.004, 1], [0.173, 0, 0, 0.04, 0.004, 1], [0.144, 0, 0, 0.04, 0.004, 1], [0.111, 0, 0, 0.04, 0.004, 1], [0.132, 0, 0, 0.04, 0.004, 1], [0.166, 0, 0, 0.04, 0.004, 1], [0.024, 0, 0, 0.04, 0.004, 1]], [[0.057, 0, 0, 0.04, 0.004, 1], [0.068, 0, 0, 0.04, 0.004, 1], [0.175, 0, 0, 0.04, 0.004, 1], [0.099, 0, 0, 0.04, 0.004, 1], [0.204, 0, 0, 0.04, 0.004, 1], [0.203, 0, 0, 0.04, 0.004, 1], [0.335, 0, 0, 0.04, 0.004, 1], [0.78, 0, 0, 0.04, 0.004, 1], [0.78, 0, 0, 0.04, 0.004, 1], [0.335, 0, 0, 0.04, 0.004, 1], [0.203, 0, 0, 0.04, 0.004, 1], [0.204, 0, 0, 0.04, 0.004, 1], [0.099, 0, 0, 0.04, 0.004, 1], [0.175, 0, 0, 0.04, 0.004, 1], [0.068, 0, 0, 0.04, 0.004, 1], [0.057, 0, 0, 0.04, 0.004, 1], [0.048, 0, 0, 0.04, 0.004, 1], [0.083, 0, 0, 0.04, 0.004, 1], [0.233, 0, 0, 0.04, 0.004, 1], [0.106, 0, 0, 0.04, 0.004, 1], [0.058, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.16, 0, 0, 0.04, 0.004, 1], [0.314, 0, 0, 0.04, 0.004, 1], [0.314, 0, 0, 0.04, 0.004, 1], [0.16, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.058, 0, 0, 0.04, 0.004, 1], [0.106, 0, 0, 0.04, 0.004, 1], [0.233, 0, 0, 0.04, 0.004, 1], [0.083, 0, 0, 0.04, 0.004, 1], [0.048, 0, 0, 0.04, 0.004, 1]], [[0.292, 0, 0, 0.04, 0.004, 1], [0.235, 0, 0, 0.04, 0.004, 1], [0.166, 0, 0, 0.04, 0.004, 1], [0.251, 0, 0, 0.04, 0.004, 1], [0.265, 0, 0, 0.04, 0.004, 1], [0.481, 0, 0, 0.04, 0.004, 1], [0.37, 0, 0, 0.04, 0.004, 1], [0.607, 0, 0, 0.04, 0.004, 1], [0.607, 0, 0, 0.04, 0.004, 1], [0.37, 0, 0, 0.04, 0.004, 1], [0.481, 0, 0, 0.04, 0.004, 1], [0.265, 0, 0, 0.04, 0.004, 1], [0.251, 0, 0, 0.04, 0.004, 1], [0.166, 0, 0, 0.04, 0.004, 1], [0.235, 0, 0, 0.04, 0.004, 1], [0.292, 0, 0, 0.04, 0.004, 1], [0.255, 0, 0, 0.04, 0.004, 1], [0.255, 0, 0, 0.04, 0.004, 1], [0.117, 0, 0, 0.04, 0.004, 1], [0.141, 0, 0, 0.04, 0.004, 1], [0.055, 0, 0, 0.04, 0.004, 1], [0.157, 0, 0, 0.04, 0.004, 1], [0.339, 0, 0, 0.04, 0.004, 1], [0.337, 0, 0, 0.04, 0.004, 1], [0.337, 0, 0, 0.04, 0.004, 1], [0.339, 0, 0, 0.04, 0.004, 1], [0.157, 0, 0, 0.04, 0.004, 1], [0.055, 0, 0, 0.04, 0.004, 1], [0.141, 0, 0, 0.04, 0.004, 1], [0.117, 0, 0, 0.04, 0.004, 1], [0.255, 0, 0, 0.04, 0.004, 1], [0.255, 0, 0, 0.04, 0.004, 1]], [[0.261, 0, 0, 0.04, 0.004, 1], [0.267, 0, 0, 0.04, 0.004, 1], [0.28, 0, 0, 0.04, 0.004, 1], [0.647, 0, 0, 0.04, 0.004, 1], [0.481, 0, 0, 0.04, 0.004, 1], [0.515, 0, 0, 0.04, 0.004, 1], [0.609, 0, 0, 0.04, 0.004, 1], [0.856, 0, 0, 0.04, 0.004, 1], [0.856, 0, 0, 0.04, 0.004, 1], [0.609, 0, 0, 0.04, 0.004, 1], [0.515, 0, 0, 0.04, 0.004, 1], [0.481, 0, 0, 0.04, 0.004, 1], [0.647, 0, 0, 0.04, 0.004, 1], [0.28, 0, 0, 0.04, 0.004, 1], [0.267, 0, 0, 0.04, 0.004, 1], [0.261, 0, 0, 0.04, 0.004, 1], [0.556, 0, 0, 0.04, 0.004, 1], [0.353, 0, 0, 0.04, 0.004, 1], [0.159, 0, 0, 0.04, 0.004, 1], [0.065, 0, 0, 0.04, 0.004, 1], [0.031, 0, 0, 0.04, 0.004, 1], [0.072, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.281, 0, 0, 0.04, 0.004, 1], [0.281, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.072, 0, 0, 0.04, 0.004, 1], [0.031, 0, 0, 0.04, 0.004, 1], [0.065, 0, 0, 0.04, 0.004, 1], [0.159, 0, 0, 0.04, 0.004, 1], [0.353, 0, 0, 0.04, 0.004, 1], [0.556, 0, 0, 0.04, 0.004, 1]], [[0.338, 0, 0, 0.04, 0.004, 1], [0.199, 0, 0, 0.04, 0.004, 1], [0.192, 0, 0, 0.04, 0.004, 1], [0.439, 0, 0, 0.04, 0.004, 1], [0.32, 0, 0, 0.04, 0.004, 1], [0.334, 0, 0, 0.04, 0.004, 1], [0.587, 0, 0, 0.04, 0.004, 1], [0.36, 0, 0, 0.04, 0.004, 1], [0.36, 0, 0, 0.04, 0.004, 1], [0.587, 0, 0, 0.04, 0.004, 1], [0.334, 0, 0, 0.04, 0.004, 1], [0.32, 0, 0, 0.04, 0.004, 1], [0.439, 0, 0, 0.04, 0.004, 1], [0.192, 0, 0, 0.04, 0.004, 1], [0.199, 0, 0, 0.04, 0.004, 1], [0.338, 0, 0, 0.04, 0.004, 1], [0.326, 0, 0, 0.04, 0.004, 1], [0.336, 0, 0, 0.04, 0.004, 1], [0.098, 0, 0, 0.04, 0.004, 1], [0.099, 0, 0, 0.04, 0.004, 1], [0.072, 0, 0, 0.04, 0.004, 1], [0.092, 0, 0, 0.04, 0.004, 1], [0.16, 0, 0, 0.04, 0.004, 1], [0.212, 0, 0, 0.04, 0.004, 1], [0.212, 0, 0, 0.04, 0.004, 1], [0.16, 0, 0, 0.04, 0.004, 1], [0.092, 0, 0, 0.04, 0.004, 1], [0.072, 0, 0, 0.04, 0.004, 1], [0.099, 0, 0, 0.04, 0.004, 1], [0.098, 0, 0, 0.04, 0.004, 1], [0.336, 0, 0, 0.04, 0.004, 1], [0.326, 0, 0, 0.04, 0.004, 1]], [[0.155, 0, 0, 0.04, 0.004, 1], [0.127, 0, 0, 0.04, 0.004, 1], [0.119, 0, 0, 0.04, 0.004, 1], [0.098, 0, 0, 0.04, 0.004, 1], [0.188, 0, 0, 0.04, 0.004, 1], [0.471, 0, 0, 0.04, 0.004, 1], [0.401, 0, 0, 0.04, 0.004, 1], [0.148, 0, 0, 0.04, 0.004, 1], [0.148, 0, 0, 0.04, 0.004, 1], [0.401, 0, 0, 0.04, 0.004, 1], [0.471, 0, 0, 0.04, 0.004, 1], [0.188, 0, 0, 0.04, 0.004, 1], [0.098, 0, 0, 0.04, 0.004, 1], [0.119, 0, 0, 0.04, 0.004, 1], [0.127, 0, 0, 0.04, 0.004, 1], [0.155, 0, 0, 0.04, 0.004, 1], [0.168, 0, 0, 0.04, 0.004, 1], [0.201, 0, 0, 0.04, 0.004, 1], [0.062, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.134, 0, 0, 0.04, 0.004, 1], [0.101, 0, 0, 0.04, 0.004, 1], [0.232, 0, 0, 0.04, 0.004, 1], [0.19, 0, 0, 0.04, 0.004, 1], [0.19, 0, 0, 0.04, 0.004, 1], [0.232, 0, 0, 0.04, 0.004, 1], [0.101, 0, 0, 0.04, 0.004, 1], [0.134, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.062, 0, 0, 0.04, 0.004, 1], [0.201, 0, 0, 0.04, 0.004, 1], [0.168, 0, 0, 0.04, 0.004, 1]], [[0.168, 0, 0, 0.04, 0.004, 1], [0.169, 0, 0, 0.04, 0.004, 1], [0.121, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.152, 0, 0, 0.04, 0.004, 1], [0.35, 0, 0, 0.04, 0.004, 1], [0.164, 0, 0, 0.04, 0.004, 1], [0.129, 0, 0, 0.04, 0.004, 1], [0.129, 0, 0, 0.04, 0.004, 1], [0.164, 0, 0, 0.04, 0.004, 1], [0.35, 0, 0, 0.04, 0.004, 1], [0.152, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.121, 0, 0, 0.04, 0.004, 1], [0.169, 0, 0, 0.04, 0.004, 1], [0.168, 0, 0, 0.04, 0.004, 1], [0.159, 0, 0, 0.04, 0.004, 1], [0.224, 0, 0, 0.04, 0.004, 1], [0.166, 0, 0, 0.04, 0.004, 1], [0.081, 0, 0, 0.04, 0.004, 1], [0.05, 0, 0, 0.04, 0.004, 1], [0.151, 0, 0, 0.04, 0.004, 1], [0.109, 0, 0, 0.04, 0.004, 1], [0.221, 0, 0, 0.04, 0.004, 1], [0.221, 0, 0, 0.04, 0.004, 1], [0.109, 0, 0, 0.04, 0.004, 1], [0.151, 0, 0, 0.04, 0.004, 1], [0.05, 0, 0, 0.04, 0.004, 1], [0.081, 0, 0, 0.04, 0.004, 1], [0.166, 0, 0, 0.04, 0.004, 1], [0.224, 0, 0, 0.04, 0.004, 1], [0.159, 0, 0, 0.04, 0.004, 1]], [[0.128, 0, 0, 0.04, 0.004, 1], [0.181, 0, 0, 0.04, 0.004, 1], [0.13, 0, 0, 0.04, 0.004, 1], [0.064, 0, 0, 0.04, 0.004, 1], [0.097, 0, 0, 0.04, 0.004, 1], [0.38, 0, 0, 0.04, 0.004, 1], [0.135, 0, 0, 0.04, 0.004, 1], [0.171, 0, 0, 0.04, 0.004, 1], [0.171, 0, 0, 0.04, 0.004, 1], [0.135, 0, 0, 0.04, 0.004, 1], [0.38, 0, 0, 0.04, 0.004, 1], [0.097, 0, 0, 0.04, 0.004, 1], [0.064, 0, 0, 0.04, 0.004, 1], [0.13, 0, 0, 0.04, 0.004, 1], [0.181, 0, 0, 0.04, 0.004, 1], [0.128, 0, 0, 0.04, 0.004, 1], [0.0, 0.0, 1, 0.04, 0.004, 1], [0.121, 0, 0, 0.04, 0.004, 1], [0.159, 0, 0, 0.04, 0.004, 1], [0.057, 0, 0, 0.04, 0.004, 1], [0.027, 0, 0, 0.04, 0.004, 1], [0.059, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.125, 0, 0, 0.04, 0.004, 1], [0.125, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.059, 0, 0, 0.04, 0.004, 1], [0.027, 0, 0, 0.04, 0.004, 1], [0.057, 0, 0, 0.04, 0.004, 1], [0.159, 0, 0, 0.04, 0.004, 1], [0.121, 0, 0, 0.04, 0.004, 1], [0.0, 0.0, -1, 0.04, 0.004, 1]], [[0.146, 0, 0, 0.04, 0.004, 1], [0.142, 0, 0, 0.04, 0.004, 1], [0.138, 0, 0, 0.04, 0.004, 1], [0.158, 0, 0, 0.04, 0.004, 1], [0.12, 0, 0, 0.04, 0.004, 1], [0.153, 0, 0, 0.04, 0.004, 1], [0.12, 0, 0, 0.04, 0.004, 1], [0.25, 0, 0, 0.04, 0.004, 1], [0.25, 0, 0, 0.04, 0.004, 1], [0.12, 0, 0, 0.04, 0.004, 1], [0.153, 0, 0, 0.04, 0.004, 1], [0.12, 0, 0, 0.04, 0.004, 1], [0.158, 0, 0, 0.04, 0.004, 1], [0.138, 0, 0, 0.04, 0.004, 1], [0.142, 0, 0, 0.04, 0.004, 1], [0.146, 0, 0, 0.04, 0.004, 1], [0.135, 0, 0, 0.04, 0.004, 1], [0.266, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.121, 0, 0, 0.04, 0.004, 1], [0.109, 0, 0, 0.04, 0.004, 1], [0.07, 0, 0, 0.04, 0.004, 1], [0.102, 0, 0, 0.04, 0.004, 1], [0.1, 0, 0, 0.04, 0.004, 1], [0.1, 0, 0, 0.04, 0.004, 1], [0.102, 0, 0, 0.04, 0.004, 1], [0.07, 0, 0, 0.04, 0.004, 1], [0.109, 0, 0, 0.04, 0.004, 1], [0.121, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.266, 0, 0, 0.04, 0.004, 1], [0.135, 0, 0, 0.04, 0.004, 1]], [[0.119, 0, 0, 0.04, 0.004, 1], [0.093, 0, 0, 0.04, 0.004, 1], [0.286, 0, 0, 0.04, 0.004, 1], [0.409, 0, 0, 0.04, 0.004, 1], [0.208, 0, 0, 0.04, 0.004, 1], [0.09, 0, 0, 0.04, 0.004, 1], [0.106, 0, 0, 0.04, 0.004, 1], [0.189, 0, 0, 0.04, 0.004, 1], [0.189, 0, 0, 0.04, 0.004, 1], [0.106, 0, 0, 0.04, 0.004, 1], [0.09, 0, 0, 0.04, 0.004, 1], [0.208, 0, 0, 0.04, 0.004, 1], [0.409, 0, 0, 0.04, 0.004, 1], [0.286, 0, 0, 0.04, 0.004, 1], [0.093, 0, 0, 0.04, 0.004, 1], [0.119, 0, 0, 0.04, 0.004, 1], [0.142, 0, 0, 0.04, 0.004, 1], [0.136, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.157, 0, 0, 0.04, 0.004, 1], [0.161, 0, 0, 0.04, 0.004, 1], [0.132, 0, 0, 0.04, 0.004, 1], [0.125, 0, 0, 0.04, 0.004, 1], [0.29, 0, 0, 0.04, 0.004, 1], [0.29, 0, 0, 0.04, 0.004, 1], [0.125, 0, 0, 0.04, 0.004, 1], [0.132, 0, 0, 0.04, 0.004, 1], [0.161, 0, 0, 0.04, 0.004, 1], [0.157, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.136, 0, 0, 0.04, 0.004, 1], [0.142, 0, 0, 0.04, 0.004, 1]], [[0.176, 0, 0, 0.04, 0.004, 1], [0.172, 0, 0, 0.04, 0.004, 1], [0.15, 0, 0, 0.04, 0.004, 1], [0.296, 0, 0, 0.04, 0.004, 1], [0.174, 0, 0, 0.04, 0.004, 1], [0.104, 0, 0, 0.04, 0.004, 1], [0.253, 0, 0, 0.04, 0.004, 1], [0.375, 0, 0, 0.04, 0.004, 1], [0.375, 0, 0, 0.04, 0.004, 1], [0.253, 0, 0, 0.04, 0.004, 1], [0.104, 0, 0, 0.04, 0.004, 1], [0.174, 0, 0, 0.04, 0.004, 1], [0.296, 0, 0, 0.04, 0.004, 1], [0.15, 0, 0, 0.04, 0.004, 1], [0.172, 0, 0, 0.04, 0.004, 1], [0.176, 0, 0, 0.04, 0.004, 1], [0.251, 0, 0, 0.04, 0.004, 1], [0.298, 0, 0, 0.04, 0.004, 1], [0.225, 0, 0, 0.04, 0.004, 1], [0.164, 0, 0, 0.04, 0.004, 1], [0.286, 0, 0, 0.04, 0.004, 1], [0.173, 0, 0, 0.04, 0.004, 1], [0.171, 0, 0, 0.04, 0.004, 1], [0.155, 0, 0, 0.04, 0.004, 1], [0.155, 0, 0, 0.04, 0.004, 1], [0.171, 0, 0, 0.04, 0.004, 1], [0.173, 0, 0, 0.04, 0.004, 1], [0.286, 0, 0, 0.04, 0.004, 1], [0.164, 0, 0, 0.04, 0.004, 1], [0.225, 0, 0, 0.04, 0.004, 1], [0.298, 0, 0, 0.04, 0.004, 1], [0.251, 0, 0, 0.04, 0.004, 1]], [[0.251, 0, 0, 0.04, 0.004, 1], [0.138, 0, 0, 0.04, 0.004, 1], [0.129, 0, 0, 0.04, 0.004, 1], [0.184, 0, 0, 0.04, 0.004, 1], [0.19, 0, 0, 0.04, 0.004, 1], [0.17, 0, 0, 0.04, 0.004, 1], [0.317, 0, 0, 0.04, 0.004, 1], [0.553, 0, 0, 0.04, 0.004, 1], [0.553, 0, 0, 0.04, 0.004, 1], [0.317, 0, 0, 0.04, 0.004, 1], [0.17, 0, 0, 0.04, 0.004, 1], [0.19, 0, 0, 0.04, 0.004, 1], [0.184, 0, 0, 0.04, 0.004, 1], [0.129, 0, 0, 0.04, 0.004, 1], [0.138, 0, 0, 0.04, 0.004, 1], [0.251, 0, 0, 0.04, 0.004, 1], [0.646, 0, 0, 0.04, 0.004, 1], [0.308, 0, 0, 0.04, 0.004, 1], [0.285, 0, 0, 0.04, 0.004, 1], [0.192, 0, 0, 0.04, 0.004, 1], [0.215, 0, 0, 0.04, 0.004, 1], [0.252, 0, 0, 0.04, 0.004, 1], [0.175, 0, 0, 0.04, 0.004, 1], [0.305, 0, 0, 0.04, 0.004, 1], [0.305, 0, 0, 0.04, 0.004, 1], [0.175, 0, 0, 0.04, 0.004, 1], [0.252, 0, 0, 0.04, 0.004, 1], [0.215, 0, 0, 0.04, 0.004, 1], [0.192, 0, 0, 0.04, 0.004, 1], [0.285, 0, 0, 0.04, 0.004, 1], [0.308, 0, 0, 0.04, 0.004, 1], [0.646, 0, 0, 0.04, 0.004, 1]], [[0.431, 0, 0, 0.04, 0.004, 1], [0.21, 0, 0, 0.04, 0.004, 1], [0.399, 0, 0, 0.04, 0.004, 1], [0.17, 0, 0, 0.04, 0.004, 1], [0.237, 0, 0, 0.04, 0.004, 1], [0.196, 0, 0, 0.04, 0.004, 1], [0.142, 0, 0, 0.04, 0.004, 1], [0.168, 0, 0, 0.04, 0.004, 1], [0.168, 0, 0, 0.04, 0.004, 1], [0.142, 0, 0, 0.04, 0.004, 1], [0.196, 0, 0, 0.04, 0.004, 1], [0.237, 0, 0, 0.04, 0.004, 1], [0.17, 0, 0, 0.04, 0.004, 1], [0.399, 0, 0, 0.04, 0.004, 1], [0.21, 0, 0, 0.04, 0.004, 1], [0.431, 0, 0, 0.04, 0.004, 1], [0.482, 0, 0, 0.04, 0.004, 1], [0.319, 0, 0, 0.04, 0.004, 1], [0.228, 0, 0, 0.04, 0.004, 1], [0.194, 0, 0, 0.04, 0.004, 1], [0.245, 0, 0, 0.04, 0.004, 1], [0.167, 0, 0, 0.04, 0.004, 1], [0.099, 0, 0, 0.04, 0.004, 1], [0.282, 0, 0, 0.04, 0.004, 1], [0.282, 0, 0, 0.04, 0.004, 1], [0.099, 0, 0, 0.04, 0.004, 1], [0.167, 0, 0, 0.04, 0.004, 1], [0.245, 0, 0, 0.04, 0.004, 1], [0.194, 0, 0, 0.04, 0.004, 1], [0.228, 0, 0, 0.04, 0.004, 1], [0.319, 0, 0, 0.04, 0.004, 1], [0.482, 0, 0, 0.04, 0.004, 1]], [[0.36, 0, 0, 0.04, 0.004, 1], [0.303, 0, 0, 0.04, 0.004, 1], [0.373, 0, 0, 0.04, 0.004, 1], [0.293, 0, 0, 0.04, 0.004, 1], [0.352, 0, 0, 0.04, 0.004, 1], [0.127, 0, 0, 0.04, 0.004, 1], [0.247, 0, 0, 0.04, 0.004, 1], [0.096, 0, 0, 0.04, 0.004, 1], [0.096, 0, 0, 0.04, 0.004, 1], [0.247, 0, 0, 0.04, 0.004, 1], [0.127, 0, 0, 0.04, 0.004, 1], [0.352, 0, 0, 0.04, 0.004, 1], [0.293, 0, 0, 0.04, 0.004, 1], [0.373, 0, 0, 0.04, 0.004, 1], [0.303, 0, 0, 0.04, 0.004, 1], [0.36, 0, 0, 0.04, 0.004, 1], [0.866, 0, 0, 0.04, 0.004, 1], [0.667, 0, 0, 0.04, 0.004, 1], [0.328, 0, 0, 0.04, 0.004, 1], [0.228, 0, 0, 0.04, 0.004, 1], [0.419, 0, 0, 0.04, 0.004, 1], [0.125, 0, 0, 0.04, 0.004, 1], [0.067, 0, 0, 0.04, 0.004, 1], [0.068, 0, 0, 0.04, 0.004, 1], [0.068, 0, 0, 0.04, 0.004, 1], [0.067, 0, 0, 0.04, 0.004, 1], [0.125, 0, 0, 0.04, 0.004, 1], [0.419, 0, 0, 0.04, 0.004, 1], [0.228, 0, 0, 0.04, 0.004, 1], [0.328, 0, 0, 0.04, 0.004, 1], [0.667, 0, 0, 0.04, 0.004, 1], [0.866, 0, 0, 0.04, 0.004, 1]], [[0.549, 0, 0, 0.04, 0.004, 1], [0.335, 0, 0, 0.04, 0.004, 1], [0.358, 0, 0, 0.04, 0.004, 1], [0.235, 0, 0, 0.04, 0.004, 1], [0.273, 0, 0, 0.04, 0.004, 1], [0.146, 0, 0, 0.04, 0.004, 1], [0.089, 0, 0, 0.04, 0.004, 1], [0.052, 0, 0, 0.04, 0.004, 1], [0.052, 0, 0, 0.04, 0.004, 1], [0.089, 0, 0, 0.04, 0.004, 1], [0.146, 0, 0, 0.04, 0.004, 1], [0.273, 0, 0, 0.04, 0.004, 1], [0.235, 0, 0, 0.04, 0.004, 1], [0.358, 0, 0, 0.04, 0.004, 1], [0.335, 0, 0, 0.04, 0.004, 1], [0.549, 0, 0, 0.04, 0.004, 1], [0.531, 0, 0, 0.04, 0.004, 1], [0.37, 0, 0, 0.04, 0.004, 1], [0.24, 0, 0, 0.04, 0.004, 1], [0.199, 0, 0, 0.04, 0.004, 1], [0.245, 0, 0, 0.04, 0.004, 1], [0.174, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.044, 0, 0, 0.04, 0.004, 1], [0.044, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.174, 0, 0, 0.04, 0.004, 1], [0.245, 0, 0, 0.04, 0.004, 1], [0.199, 0, 0, 0.04, 0.004, 1], [0.24, 0, 0, 0.04, 0.004, 1], [0.37, 0, 0, 0.04, 0.004, 1], [0.531, 0, 0, 0.04, 0.004, 1]], [[0.494, 0, 0, 0.04, 0.004, 1], [0.715, 0, 0, 0.04, 0.004, 1], [0.492, 0, 0, 0.04, 0.004, 1], [0.494, 0, 0, 0.04, 0.004, 1], [0.169, 0, 0, 0.04, 0.004, 1], [0.076, 0, 0, 0.04, 0.004, 1], [0.127, 0, 0, 0.04, 0.004, 1], [0.024, 0, 0, 0.04, 0.004, 1], [0.024, 0, 0, 0.04, 0.004, 1], [0.127, 0, 0, 0.04, 0.004, 1], [0.076, 0, 0, 0.04, 0.004, 1], [0.169, 0, 0, 0.04, 0.004, 1], [0.494, 0, 0, 0.04, 0.004, 1], [0.492, 0, 0, 0.04, 0.004, 1], [0.715, 0, 0, 0.04, 0.004, 1], [0.494, 0, 0, 0.04, 0.004, 1], [0.842, 0, 0, 0.04, 0.004, 1], [0.561, 0, 0, 0.04, 0.004, 1], [0.177, 0, 0, 0.04, 0.004, 1], [0.144, 0, 0, 0.04, 0.004, 1], [0.166, 0, 0, 0.04, 0.004, 1], [0.079, 0, 0, 0.04, 0.004, 1], [0.042, 0, 0, 0.04, 0.004, 1], [0.056, 0, 0, 0.04, 0.004, 1], [0.056, 0, 0, 0.04, 0.004, 1], [0.042, 0, 0, 0.04, 0.004, 1], [0.079, 0, 0, 0.04, 0.004, 1], [0.166, 0, 0, 0.04, 0.004, 1], [0.144, 0, 0, 0.04, 0.004, 1], [0.177, 0, 0, 0.04, 0.004, 1], [0.561, 0, 0, 0.04, 0.004, 1], [0.842, 0, 0, 0.04, 0.004, 1]], [[0.56, 0, 0, 0.04, 0.004, 1], [0.445, 0, 0, 0.04, 0.004, 1], [0.365, 0, 0, 0.04, 0.004, 1], [0.289, 0, 0, 0.04, 0.004, 1], [0.22, 0, 0, 0.04, 0.004, 1], [0.088, 0, 0, 0.04, 0.004, 1], [0.082, 0, 0, 0.04, 0.004, 1], [0.022, 0, 0, 0.04, 0.004, 1], [0.022, 0, 0, 0.04, 0.004, 1], [0.082, 0, 0, 0.04, 0.004, 1], [0.088, 0, 0, 0.04, 0.004, 1], [0.22, 0, 0, 0.04, 0.004, 1], [0.289, 0, 0, 0.04, 0.004, 1], [0.365, 0, 0, 0.04, 0.004, 1], [0.445, 0, 0, 0.04, 0.004, 1], [0.56, 0, 0, 0.04, 0.004, 1], [0.304, 0, 0, 0.04, 0.004, 1], [0.377, 0, 0, 0.04, 0.004, 1], [0.245, 0, 0, 0.04, 0.004, 1], [0.131, 0, 0, 0.04, 0.004, 1], [0.149, 0, 0, 0.04, 0.004, 1], [0.076, 0, 0, 0.04, 0.004, 1], [0.043, 0, 0, 0.04, 0.004, 1], [0.046, 0, 0, 0.04, 0.004, 1], [0.046, 0, 0, 0.04, 0.004, 1], [0.043, 0, 0, 0.04, 0.004, 1], [0.076, 0, 0, 0.04, 0.004, 1], [0.149, 0, 0, 0.04, 0.004, 1], [0.131, 0, 0, 0.04, 0.004, 1], [0.245, 0, 0, 0.04, 0.004, 1], [0.377, 0, 0, 0.04, 0.004, 1], [0.304, 0, 0, 0.04, 0.004, 1]], [[0.374, 0, 0, 0.04, 0.004, 1], [0.18, 0, 0, 0.04, 0.004, 1], [0.216, 0, 0, 0.04, 0.004, 1], [0.508, 0, 0, 0.04, 0.004, 1], [0.405, 0, 0, 0.04, 0.004, 1], [0.178, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.033, 0, 0, 0.04, 0.004, 1], [0.033, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.178, 0, 0, 0.04, 0.004, 1], [0.405, 0, 0, 0.04, 0.004, 1], [0.508, 0, 0, 0.04, 0.004, 1], [0.216, 0, 0, 0.04, 0.004, 1], [0.18, 0, 0, 0.04, 0.004, 1], [0.374, 0, 0, 0.04, 0.004, 1], [0.149, 0, 0, 0.04, 0.004, 1], [0.184, 0, 0, 0.04, 0.004, 1], [0.159, 0, 0, 0.04, 0.004, 1], [0.087, 0, 0, 0.04, 0.004, 1], [0.044, 0, 0, 0.04, 0.004, 1], [0.152, 0, 0, 0.04, 0.004, 1], [0.034, 0, 0, 0.04, 0.004, 1], [0.083, 0, 0, 0.04, 0.004, 1], [0.083, 0, 0, 0.04, 0.004, 1], [0.034, 0, 0, 0.04, 0.004, 1], [0.152, 0, 0, 0.04, 0.004, 1], [0.044, 0, 0, 0.04, 0.004, 1], [0.087, 0, 0, 0.04, 0.004, 1], [0.159, 0, 0, 0.04, 0.004, 1], [0.184, 0, 0, 0.04, 0.004, 1], [0.149, 0, 0, 0.04, 0.004, 1]], [[0.111, 0, 0, 0.04, 0.004, 1], [0.13, 0, 0, 0.04, 0.004, 1], [0.314, 0, 0, 0.04, 0.004, 1], [0.273, 0, 0, 0.04, 0.004, 1], [0.264, 0, 0, 0.04, 0.004, 1], [0.099, 0, 0, 0.04, 0.004, 1], [0.104, 0, 0, 0.04, 0.004, 1], [0.177, 0, 0, 0.04, 0.004, 1], [0.177, 0, 0, 0.04, 0.004, 1], [0.104, 0, 0, 0.04, 0.004, 1], [0.099, 0, 0, 0.04, 0.004, 1], [0.264, 0, 0, 0.04, 0.004, 1], [0.273, 0, 0, 0.04, 0.004, 1], [0.314, 0, 0, 0.04, 0.004, 1], [0.13, 0, 0, 0.04, 0.004, 1], [0.111, 0, 0, 0.04, 0.004, 1], [0.115, 0, 0, 0.04, 0.004, 1], [0.084, 0, 0, 0.04, 0.004, 1], [0.08, 0, 0, 0.04, 0.004, 1], [0.196, 0, 0, 0.04, 0.004, 1], [0.033, 0, 0, 0.04, 0.004, 1], [0.071, 0, 0, 0.04, 0.004, 1], [0.041, 0, 0, 0.04, 0.004, 1], [0.071, 0, 0, 0.04, 0.004, 1], [0.071, 0, 0, 0.04, 0.004, 1], [0.041, 0, 0, 0.04, 0.004, 1], [0.071, 0, 0, 0.04, 0.004, 1], [0.033, 0, 0, 0.04, 0.004, 1], [0.196, 0, 0, 0.04, 0.004, 1], [0.08, 0, 0, 0.04, 0.004, 1], [0.084, 0, 0, 0.04, 0.004, 1], [0.115, 0, 0, 0.04, 0.004, 1]], [[0.161, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.374, 0, 0, 0.04, 0.004, 1], [0.501, 0, 0, 0.04, 0.004, 1], [0.201, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.09, 0, 0, 0.04, 0.004, 1], [0.167, 0, 0, 0.04, 0.004, 1], [0.167, 0, 0, 0.04, 0.004, 1], [0.09, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.201, 0, 0, 0.04, 0.004, 1], [0.501, 0, 0, 0.04, 0.004, 1], [0.374, 0, 0, 0.04, 0.004, 1], [0.122, 0, 0, 0.04, 0.004, 1], [0.161, 0, 0, 0.04, 0.004, 1], [0.033, 0, 0, 0.04, 0.004, 1], [0.108, 0, 0, 0.04, 0.004, 1], [0.092, 0, 0, 0.04, 0.004, 1], [0.109, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.11, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.186, 0, 0, 0.04, 0.004, 1], [0.186, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.11, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.109, 0, 0, 0.04, 0.004, 1], [0.092, 0, 0, 0.04, 0.004, 1], [0.108, 0, 0, 0.04, 0.004, 1], [0.033, 0, 0, 0.04, 0.004, 1]], [[0.058, 0, 0, 0.04, 0.004, 1], [0.084, 0, 0, 0.04, 0.004, 1], [0.106, 0, 0, 0.04, 0.004, 1], [0.386, 0, 0, 0.04, 0.004, 1], [0.19, 0, 0, 0.04, 0.004, 1], [0.066, 0, 0, 0.04, 0.004, 1], [0.193, 0, 0, 0.04, 0.004, 1], [0.066, 0, 0, 0.04, 0.004, 1], [0.066, 0, 0, 0.04, 0.004, 1], [0.193, 0, 0, 0.04, 0.004, 1], [0.066, 0, 0, 0.04, 0.004, 1], [0.19, 0, 0, 0.04, 0.004, 1], [0.386, 0, 0, 0.04, 0.004, 1], [0.106, 0, 0, 0.04, 0.004, 1], [0.084, 0, 0, 0.04, 0.004, 1], [0.058, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.047, 0, 0, 0.04, 0.004, 1], [0.151, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.023, 0, 0, 0.04, 0.004, 1], [0.024, 0, 0, 0.04, 0.004, 1], [0.021, 0, 0, 0.04, 0.004, 1], [0.169, 0, 0, 0.04, 0.004, 1], [0.169, 0, 0, 0.04, 0.004, 1], [0.021, 0, 0, 0.04, 0.004, 1], [0.024, 0, 0, 0.04, 0.004, 1], [0.023, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.151, 0, 0, 0.04, 0.004, 1], [0.047, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1]], [[0.088, 0, 0, 0.04, 0.004, 1], [0.046, 0, 0, 0.04, 0.004, 1], [0.064, 0, 0, 0.04, 0.004, 1], [0.078, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.069, 0, 0, 0.04, 0.004, 1], [0.113, 0, 0, 0.04, 0.004, 1], [0.038, 0, 0, 0.04, 0.004, 1], [0.038, 0, 0, 0.04, 0.004, 1], [0.113, 0, 0, 0.04, 0.004, 1], [0.069, 0, 0, 0.04, 0.004, 1], [0.114, 0, 0, 0.04, 0.004, 1], [0.078, 0, 0, 0.04, 0.004, 1], [0.064, 0, 0, 0.04, 0.004, 1], [0.046, 0, 0, 0.04, 0.004, 1], [0.088, 0, 0, 0.04, 0.004, 1], [0.115, 0, 0, 0.04, 0.004, 1], [0.124, 0, 0, 0.04, 0.004, 1], [0.016, 0, 0, 0.04, 0.004, 1], [0.022, 0, 0, 0.04, 0.004, 1], [0.045, 0, 0, 0.04, 0.004, 1], [0.032, 0, 0, 0.04, 0.004, 1], [0.016, 0, 0, 0.04, 0.004, 1], [0.037, 0, 0, 0.04, 0.004, 1], [0.037, 0, 0, 0.04, 0.004, 1], [0.016, 0, 0, 0.04, 0.004, 1], [0.032, 0, 0, 0.04, 0.004, 1], [0.045, 0, 0, 0.04, 0.004, 1], [0.022, 0, 0, 0.04, 0.004, 1], [0.016, 0, 0, 0.04, 0.004, 1], [0.124, 0, 0, 0.04, 0.004, 1], [0.115, 0, 0, 0.04, 0.004, 1]], [[0.029, 0, 0, 0.04, 0.004, 1], [0.036, 0, 0, 0.04, 0.004, 1], [0.137, 0, 0, 0.04, 0.004, 1], [0.148, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.138, 0, 0, 0.04, 0.004, 1], [0.037, 0, 0, 0.04, 0.004, 1], [0.053, 0, 0, 0.04, 0.004, 1], [0.053, 0, 0, 0.04, 0.004, 1], [0.037, 0, 0, 0.04, 0.004, 1], [0.138, 0, 0, 0.04, 0.004, 1], [0.074, 0, 0, 0.04, 0.004, 1], [0.148, 0, 0, 0.04, 0.004, 1], [0.137, 0, 0, 0.04, 0.004, 1], [0.036, 0, 0, 0.04, 0.004, 1], [0.029, 0, 0, 0.04, 0.004, 1], [0.052, 0, 0, 0.04, 0.004, 1], [0.016, 0, 0, 0.04, 0.004, 1], [0.04, 0, 0, 0.04, 0.004, 1], [0.066, 0, 0, 0.04, 0.004, 1], [0.03, 0, 0, 0.04, 0.004, 1], [0.036, 0, 0, 0.04, 0.004, 1], [0.03, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.028, 0, 0, 0.04, 0.004, 1], [0.03, 0, 0, 0.04, 0.004, 1], [0.036, 0, 0, 0.04, 0.004, 1], [0.03, 0, 0, 0.04, 0.004, 1], [0.066, 0, 0, 0.04, 0.004, 1], [0.04, 0, 0, 0.04, 0.004, 1], [0.016, 0, 0, 0.04, 0.004, 1], [0.052, 0, 0, 0.04, 0.004, 1]]]
# # t = np.random.randint(0,10,(5,5,1))

# input_layer = keras.layers.Input(shape=(32,32,6,))

# model = keras.layers.Conv2D(32,(3,3))(input_layer)
# model = keras.layers.Activation('relu')(model)

# model = keras.layers.Conv2D(32,(3,3))(model)
# model = keras.layers.Activation('relu')(model)

# model = keras.layers.MaxPooling2D(pool_size=(2,2))(model)

# model = keras.layers.Conv2D(64,(3,3))(model)
# model = keras.layers.Activation('relu')(model)

# model = keras.layers.Conv2D(64,(3,3))(model)
# model = keras.layers.Activation('relu')(model)

# model = keras.layers.MaxPooling2D(pool_size=(2,2))(model)

# model = keras.layers.Flatten()(model)
# model = keras.layers.Dense(6)(model)
# model = keras.layers.Activation('softmax')(model)

# hallite_model = Model(input_layer, model)
# print(hallite_model.summary())

# #reshaped_data = np.array(t).reshape(-1,len(t))
# # print(reshaped_data.shape)ata
# image_data = np.array(t)
# # print(image_data.shape)
# image_data = np.expand_dims(image_data, axis=0)
# # print(image_data)
# print(hallite_model.predict(image_data))