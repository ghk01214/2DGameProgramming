from pico2d import *
import gfw
import random

MOVE_FPS = 200

class Missile():
	def __init__(self, pos, delta):
		mag = random.uniform(0.3, 1.0)
		self.init(pos, delta, 'res/missile.png', mag)

	def init(self, pos, delta, imageName, mag = 0):
		self.pos = pos
		self.delta = delta
		self.image = gfw.image.load(imageName)
		self.size = self.image.h
		self.radius = self.size // 2
		self.bb_l = -self.size
		self.bb_b = -self.size
		self.bb_r = get_canvas_width() + self.size
		self.bb_t = get_canvas_height() + self.size

		if mag != 0:
			self.size = int(self.size * mag)

	def update(self):
		x, y = self.pos
		dx, dy = self.delta

		x += dx * MOVE_FPS * gfw.delta_time
		y += dy * MOVE_FPS * gfw.delta_time

		self.pos = x, y

		if self.out_of_screen():
			gfw.world.remove(self)

	def draw(self):
		self.image.draw(*self.pos, self.size, self.size)

	def out_of_screen(self):
		x, y = self.pos

		if x < self.bb_l or x > self.bb_r or y < self.bb_b or y > self.bb_t:
			return True
		else:
			return False

class PresentBox(Missile):
	def __init__(self, pos, delta):
		self.init(pos, delta, 'res/present_box.png')

class Coin(Missile):
	FPS = 10

	def __init__(self, pos, delta):
		self.init(pos, delta, 'res/coin.png', 0.5)
		self.time = get_time()
		self.fcount = self.image.w // self.image.h

	def draw(self):
		elapsed = get_time() - self.time
		frame = round(elapsed * Coin.FPS) % self.fcount
		rect = frame * self.image.h, 0, self.image.h, self.image.h
		self.image.clip_draw(*rect, *self.pos, self.size, self.size)