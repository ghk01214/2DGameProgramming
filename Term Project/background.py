from pico2d import *
from game_object import *
import gfw

class Background:
	def __init__(self, imageName):
		self.imageName = imageName
		self.image = gfw.image.load(resBM(imageName))
		self.target = None
		self.canvas_w, self.canvas_h = get_canvas_width(), get_canvas_height()
		self.win_rect = 0, 0, self.canvas_w, self.canvas_h
		self.center = self.image.w // 2, self.image.h // 2
		half_w, half_h = self.canvas_w // 2, self.canvas_h // 2
		self.boundary = half_w, half_h, self.image.w - half_w, self.image.h - half_h

	def set_target(self, target):
		self.target = target
		self.update()

	def update(self):
		if self.target is None:
			return

		tx, ty = self.target.pos
		sl = round(tx - self.canvas_w / 2)
		sb = round(ty - self.canvas_h / 2)
		self.win_rect = sl, sb, self.canvas_w, self.canvas_h

	def draw(self):
		self.image.clip_draw_to_origin(*self.win_rect, 0, 0)

	def get_boundary(self):
		return self.boundary

	def translate(self, point):
		x, y = point
		l, b, r, t = self.win_rect
		return l + x, b + y

	def to_screen(self, point):
		x, y = point
		l, b, r, t = self.win_rect
		return x - l, y - b

class FixedBackground(Background):
	MARGIN_L, MARGIN_B, MARGIN_R, MARGIN_T = 20, 40, 20, 40

	def __init__(self, imageName):
		super().__init__(imageName)
		self.boundary = (FixedBackground.MARGIN_L, FixedBackground.MARGIN_B,
			self.image.w - FixedBackground.MARGIN_R, self.image.h - FixedBackground.MARGIN_T)

	def update(self):
		if self.target is None:
			return

		tx, ty = self.target.pos
		sl = clamp(0, round(tx, self.canvas_w / 2), self.image.w - self.canvas_w)
		sb = clamp(0, round(ty, self.canvas_h / 2), self.image.h - self.canvas_h)
		self.win_rect = sl, sb, self.canvas_w, self.canvas_h