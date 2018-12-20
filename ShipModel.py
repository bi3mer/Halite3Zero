from tensorflow import keras
import numpy as np
import random
import time
import sys
import os

# change tensorflow output location
stderr = sys.stderr
sys.stder = open(os.devnull, 'w')
import tensorflow as tf
sys.stder = stderr

# reduce memory usage of tensorflow to minimum
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.05)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

# constants
NUMBER_OF_ACTIONS = 6
VERSION = 'v000'
RANDOM_EXPLORATION_CHANCE = 0.1
COMMANDS = [0,1,2,3,4,5]

class ShipModel:
	def __init__(self, load_most_recent_model, random_exploration_allowed):
		'''
		set load_most-recent_model to true if you want to get the most recently
		trained model. Else set it to false and it will create a new model.
		'''
		self.random_exploration_allowed = random_exploration_allowed
		self.model = keras.Sequential([
			keras.layers.Dense(3075, activation=tf.nn.relu),
			keras.layers.Dense(4096, activation=tf.nn.relu),
			keras.layers.Dense(2048, activation=tf.nn.relu),
			keras.layers.Dense(1024, activation=tf.nn.relu),
			keras.layers.Dense(512, activation=tf.nn.relu),
			keras.layers.Dense(256, activation=tf.nn.relu),
			keras.layers.Dense(6, activation=tf.nn.softmax)
		])

		self.model.compile(loss='mse', optimizer='adam', metrics=['mae'])

		if load_most_recent_model:
			most_recent_model = 0
			dir_path = f'models/shipModels/{VERSION}/'
			for file_name in os.listdir(dir_path):
				if '.index' in file_name:
					file_name = int(file_name.split('.')[0])
					if file_name > most_recent_model:
						most_recent_model = file_name

			file_name = f'{dir_path}{most_recent_model}'
			if os.path.isfile(file_name):
				self.model.load_weights(file_name)

	def predict(self, data):
		# TODO: have data in this format from the get go
		predictions = self.model.predict([np.array(data).reshape(1,3075)])[0]
		prediction = np.argmax(predictions)

		if self.random_exploration_allowed and random.random() < RANDOM_EXPLORATION_CHANCE:
			predictions = random.choice(COMMANDS)

		return prediction

	def save(self):
		self.model.save_weights(f'models/shipModels/{VERSION}/{int(time.time())}')