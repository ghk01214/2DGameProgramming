from pico2d import *
import gfw
import game_object
from object import Object

class Spike(Object):
	def __init__(self, left, bottom):
		super().__init__(left, bottom)

class HalfSpike:
	LEFT, BOTTOM, RIGHT, TOP = range(4)
	def __init__(self, type, left, bottom):
		self.left, self.bottom = left, bottom
		self.width, self.height = 32, 32
		self.spike_type(type)
	
	def update(self):
		pass

	def draw(self):
		pass

	def get_bb(self):
		return self.left, self.bottom, self.left + self.width, self.bottom + self.height

	def spike_type(self, type):
		if type == HalfSpike.LEFT:
			self.width = self.width // 2
		elif type == HalfSpike.BOTTOM:
			self.height = self.height // 2
		elif type == HalfSpike.RIGHT:
			self.width = self.width // 2
			self.left += self.width
		elif type == HalfSpike.TOP:
			self.height = self.height // 2
			self.bottom += self.height