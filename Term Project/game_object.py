from pico2d import *
import game_framework_image as gfwi

RES_OBJECT = 'res/bitmap/object/'

class Bullet:
	bullets = []
	image = None

	def __init__(self, pos):
		if Bullet.image == None:
			self.image = gfwi.load(RES_OBJECT + 'Bullet.png')
		self.x, self.y = pos[0], pos[1]
		self.delta = 8

	def draw(self):
		self.image.draw(self.x, self.y)

	def update(self):
		self.x += self.delta

		if self.x < -10 or self.x > get_canvas_width() + 10:
			Bullet.bullets.remove(self)
			print('bullet count = %d' % len(Bullet.bullets))

def res(self):
	return RES + file