from pico2d import *
import gfw
import game_object
import random

class Platform:
	def __init__(self, type, left, bottom):
		self.left = left
		self.bottom = bottom
		self.width, self.height = 16, 16
		self.image = gfw.image.load(game_object.resBM('block.png'))
		self.type = type

	def update(self):
		pass

	def draw(self):
		self.image.clip_draw(self.type * 16, 16, 16, 16, 0, 0)

	def get_bb(self):
		return self.left, self.bottom, self.left + self.width, self.bottom + self.height