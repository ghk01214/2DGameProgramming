from pico2d import *
import gfw
import game_object
import random

class Platform:
	def __init__(self, type, left, bottom):
		self.left = left
		self.bottom = bottom
		self.width, self.height, fn = INFO[type]
		self.image = gfw.image.load(game_object.resBM('block.png'))

	def update(self):
		pass

	def draw(self):
		self.image.draw_to_origin(self.left, self.bottom, self.width, self.height)

	def get_bb(self):
		return self.left, self.bottom, self.left + self.width, self.bottom + self.height