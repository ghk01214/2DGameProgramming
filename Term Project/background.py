from pico2d import *
from game_object import *
import gfw

class Background:
	def __init__(self, imageName, player):
		self.imageName = imageName
		self.image = gfw.image.load(resBM(imageName))
		self.pos = 0, 0
		self.cw, self.ch = get_canvas_width(), get_canvas_height()
		self.player = player
		self.draw_pos = 0, 0

	def update(self):
		x, y = self.pos
		p_x, p_y = self.player.pos

		if p_x > self.cw:
			x += self.cw
			self.pos = x, y

	def draw(self):
		x, y = self.pos
		dx, dy = self.draw_pos
		self.image.clip_draw_to_origin(x, y, x + self.cw, y + self.ch, dx, dy)

	def get_bb(self):
		x, y = self.pos
		return x, y, x + self.cw, y + self.ch
		
	def to_screen(self, point):
		x, y = point
		l, b, r, t = self.window
		return x - l, y - b