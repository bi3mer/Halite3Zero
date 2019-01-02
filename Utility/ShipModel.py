from tensorflow.keras.models import Model
from tensorflow import keras
import numpy as np
import random
import time
import sys
import os

import logging

# change tensorflow output location
stderr = sys.stderr
sys.stder = open(os.devnull, 'w')
import tensorflow as tf
sys.stder = stderr

# reduce memory usage of tensorflow to minimum
# gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.05)
# sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

# constants
NUMBER_OF_ACTIONS = 6
VERSION = 'v001'
RANDOM_EXPLORATION_CHANCE = 0.1
COMMANDS = [0,1,2,3,4,5]

class ShipModel:
	def __init__(self, load_most_recent_model, random_exploration_allowed):
		'''
		set load_most-recent_model to true if you want to get the most recently
		trained model. Else set it to false and it will create a new model.
		'''
		self.random_exploration_allowed = random_exploration_allowed

		cnn_input_layer = keras.layers.Input(shape=(32,32,3,))

		cnn = keras.layers.Conv2D(32,(3,3))(cnn_input_layer)
		cnn = keras.layers.Activation('relu')(cnn)

		cnn = keras.layers.Conv2D(32,(3,3))(cnn)
		cnn = keras.layers.Activation('relu')(cnn)

		cnn = keras.layers.Conv2D(32,(3,3))(cnn)
		cnn = keras.layers.Activation('relu')(cnn)

		cnn = keras.layers.Conv2D(32,(3,3))(cnn)
		cnn = keras.layers.Activation('relu')(cnn)

		cnn = keras.layers.MaxPooling2D(pool_size=(2,2))(cnn)

		cnn = keras.layers.Conv2D(64,(3,3))(cnn)
		cnn = keras.layers.Activation('relu')(cnn)

		cnn = keras.layers.Conv2D(64,(3,3))(cnn)
		cnn = keras.layers.Activation('relu')(cnn)

		cnn = keras.layers.Conv2D(64,(3,3))(cnn)
		cnn = keras.layers.Activation('relu')(cnn)

		cnn = keras.layers.MaxPooling2D(pool_size=(2,2))(cnn)

		cnn = keras.layers.Flatten()(cnn)

		world_data_input_layer = keras.layers.Input(shape=(2,))
		model = keras.layers.Concatenate()([cnn, world_data_input_layer])

		model = keras.layers.Dense(512)(model)
		model = keras.layers.Activation('relu')(model)

		model = keras.layers.Dense(256)(model)
		model = keras.layers.Activation('relu')(model)

		model = keras.layers.Dense(128)(model)
		model = keras.layers.Activation('relu')(model)

		model = keras.layers.Dense(6)(model)
		model = keras.layers.Activation('softmax')(model)

		self.model = Model(inputs=[cnn_input_layer, world_data_input_layer], outputs=model)
		self.model.compile(loss='mse', optimizer='adam', metrics=['mae', 'accuracy'])

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
		image_data = np.expand_dims(np.array(data), axis=0)
		predictions = self.model.predict(image_data)[0]
		prediction = np.argmax(predictions)

		if self.random_exploration_allowed and random.random() < RANDOM_EXPLORATION_CHANCE:
			predictions = random.choice(COMMANDS)

		return prediction

	def get_random_action(self):
		return random.choice(COMMANDS)

	def save(self):
		self.model.save_weights(f'models/shipModels/{VERSION}/{int(time.time())}')

if __name__ == '__main__':
	from keras.utils import plot_model

	shipModel = ShipModel(False, False)
	print(shipModel.model.summary())
	print('--------------------------------')
	print('Preparing model summary and saving to "data/model.png"')
	plot_model(shipModel.model, to_file='data/model.png')