from tensorflow import keras
import tensorflow as tf
import numpy as np
import time
import os

# reduce memory usage of tensorflow to minimum
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

# constants
NUMBER_OF_ACTIONS = 6
VERSION = 'v000'

class ShipModel:
	def __init__(self, load_most_recent_model):
		'''
		set load_most-recent_model to true if you want to get the most recently
		trained model. Else set it to false and it will create a new model.
		'''
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
		max_probability = predictions[0]
		prediction = 0

		for index in range(1, NUMBER_OF_ACTIONS):
			probability = predictions[index]
			if probability > max_probability:
				max_probability = probability
				prediction = index

		return prediction

	def save(self):
		self.model.save_weights(f'models/shipModels/{VERSION}/{int(time.time())}')