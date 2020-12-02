from pico2d import *
import gfw
import game_object
import random
UNIT = 32
INFO = [
	( UNIT, UNIT, 'stage_1_block.png'),
	( UNIT, UNIT, 'stage_2_block.png'),
	( UNIT, UNIT, 'stage_3_block.png'),
	( UNIT, UNIT, 'stage_4_block.png'),
	( UNIT, UNIT, 'stage_5_block.png'),
]

class Platform:
	def __init__(self, type, left, bottom):
		self.left = left
		self.bottom = bottom
		self.width, self.height, im = INFO[0]

	def update(self):
		pass

	def draw(self):
		self.image.clip_draw(self.type * 16, 16, 16, 16, 0, 0)

	def get_bb(self):
		return self.left, self.bottom, self.left + self.width, self.bottom + self.height