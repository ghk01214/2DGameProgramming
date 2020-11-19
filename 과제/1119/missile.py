from pico2d import *
import gfw

MOVE_FPS = 200

class Missile():
	def __init__(self, pos, delta):
		self.pos = pos
		self.delta = delta
		self.image = gfw.image.load('res/missile.png')
		self.radius = self.image.w // 2
		self.bb_width = -self.image.w, get_canvas_width() + self.image.w
		self.bb_height = -self.image.h, get_canvas_height() + self.image.h

	def update(self):
		x, y = self.pos
		dx, dy = self.delta

		x += dx * MOVE_FPS * gfw.delta_time
		y += dy * MOVE_FPS * gfw.delta_time

		self.pos = x, y

		if self.out_of_screen():
			gfw.world.remove(self)

	def draw(self):
		self.image.draw(*self.pos)

	def out_of_screen(self):
		x, y = self.pos
		l, r = self.bb_width
		b, t = self.bb_height

		if x < l or x > r or y < b or y > t:
			return True
		else:
			return False

