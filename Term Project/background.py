from pico2d import *
from game_object import *
import gfw

class Background:
	def __init__(self, imageName):
		self.imageName = imageName
		self.image = gfw.image.load(resBM(imageName))
		self.canvas_w, self.canvas_h = get_canvas_width(), get_canvas_height()
		self.win_rect = 0, 0, self.canvas_w, self.canvas_h
		self.center = self.image.w // 2, self.image.h // 2
		half_w, half_h = self.canvas_w // 2, self.canvas_h // 2
		self.boundary = 0, 0, self.image.w, self.image.h

	def update(self):
		pass

	def draw(self):
		self.image.clip_draw(*self.win_rect, *self.center)

	def get_boundary(self):
		return self.boundary
		
	def to_screen(self, point):
		x, y = point
		l, b, r, t = self.win_rect
		return x - l, y - b