from pico2d import *
import gfw
import game_object

class Object:
	def __init__(self, left, bottom):
		self.left, self.bottom = left, bottom
		self.width, self.height = 32, 32
	
	def update(self):
		pass

	def draw(self):
		pass

	def get_bb(self):
		return self.left, self.bottom, self.left + self.width, self.bottom + self.height

class Save(Object):
	def __init__(self, left, bottom):
		super().__init__(left, bottom)

class Bullet:
	def __init__(self, x, y, direction):
		self.image = gfw.image.load(game_object.resBM('bullet.png'))
		self.x, self.y = x, y
		self.delta = 8
		self.direction = direction

	def draw(self):
		self.image.draw(self.x, self.y)

	def update(self):
		self.x += self.delta * self.direction

	def get_bb(self):
		return self.x - 5, self.y - 5, self.x + 5, self.y + 5