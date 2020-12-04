from pico2d import *
import gfw
import game_object

class Platform:
	def __init__(self, type, left, bottom):
		self.left = left
		self.bottom = bottom
		self.width, self.height = 32, 32
		#self.image = gfw.image.load(game_object.resBM(im))
		#self.type = type

	def update(self):
		pass

	def draw(self):
		#self.image.draw_to_origin(self.left, self.bottom, self.width, self.height)
		pass

	def get_bb(self):
		return self.left, self.bottom, self.left + self.width, self.bottom + self.height