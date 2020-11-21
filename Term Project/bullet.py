from pico2d import *
import gfw

class Bullet:
	bullets = []
	image = None

	def __init__(self, pos):
		if Bullet.image == None:
			self.image = gfw.image.load('res/bitmap/bullet.png')
		self.x, self.y = pos
		self.delta = 8

	def draw(self):
		self.image.draw(self.x, self.y)

	def update(self):
		self.x += self.delta

		if self.x < -10 or self.x > get_canvas_width() + 10:
			Bullet.bullets.remove(self)
			print('bullet count = %d' % len(Bullet.bullets))