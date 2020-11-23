from pico2d import *
from game_object import *
import gfw
from bullet import Bullet

class Player:
	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_LEFT): (-1, 0),
		(SDL_KEYDOWN, SDLK_RIGHT): (1, 0),
		(SDL_KEYDOWN, SDLK_DOWN): (0, -1),
		(SDL_KEYDOWN, SDLK_UP): (0, 1),
		(SDL_KEYUP, SDLK_LEFT): (1, 0),
		(SDL_KEYUP, SDLK_RIGHT): (-1, 0),
		(SDL_KEYUP, SDLK_DOWN): (0, 1),
		(SDL_KEYUP, SDLK_UP): (0, -1),
	}

	KEYDOWN_JUMP = (SDL_KEYDOWN, SDLK_LCTRL)
	KEYDOWN_SHOOT = (SDL_KEYDOWN, SDLK_z)

	GRAVITY = 3000
	JUMP = 1000

	def __init__(self):
		self.image = gfw.image.load(resBM('animation.png'))
		self.pos = get_canvas_width() // 2, get_canvas_height() // 2
		self.delta = 0, 0
		self.speed = 200
		self.time = 0
		self.frame = 0
		self.action = 7
		self.mag = 1
		self.mag_speed = 0
		self.width, self.height = 28, 25
		self.imageType = 4

		global center
		center = self.pos

	def update(self):
		x, y = self.pos
		dx, dy = self.delta

		x += dx * self.speed * self.mag * gfw.delta_time
		y += dy * self.speed * self.mag * gfw.delta_time

		bg_l, bg_b, bg_r, bg_t = self.background.get_boundary()
		x = clamp(bg_l, x, bg_r)
		y = clamp(bg_b, y, bg_t)

		self.pos = x, y
		self.time += gfw.delta_time
		frame = self.time * 15
		self.frame = int(frame) % self.imageType
		gravity = 0.05
		self.delta = dx, dy - gravity

	def draw(self):
		x, y = self.pos
		width, height = self.width, self.height
		sx = self.frame * width
		sy = self.action * height

		if x < self.width // 2:
			x = width // 2

		if y < self.height // 2:
			y = height // 2

		if x > get_canvas_width() - width // 2:
			x = get_canvas_width() - width // 2

		if y > get_canvas_height() - height // 2:
			y = get_canvas_height() - height // 2

		self.pos = x, y			
		self.image.clip_draw(sx, sy, self.width, self.height, *self.pos)

	def get_platform(self, foot):
		selected = None
		sel_top = 0
		x, y = self.pos

		for platform in gfw.world.objects_at(gfw.layer.platform):
			left, bottom, right, top = platform.get_bb()

			if x < left or x > right:
				continue

			mid = (bottom + top) // 2

			if foot < mid:
				continue

			if selected is None:
				selected = platform
				sel_top = top
			else:
				if top > sel_top:
					selected = platform
					sel_top = top

		return selected

	def handle_event(self, e):
		pair = (e.type, e.key)

		if pair in Player.KEY_MAP:
			pdx = self.delta[0]
			self.delta = point_add(self.delta, Player.KEY_MAP[pair])
			dx = self.delta[0]
			self.action = \
				4 if dx < 0 else \
				5 if dx > 0 else \
				6 if pdx < 0 else 7

			if self.action == 4 or self.action == 5:
				self.imageType = 5
				self.width = 29
			else:
				self.imageType = 4
				self.width = 28

		elif pair == Player.KEYDOWN_JUMP:
			self.jump()
		elif pair == Player.KEYDOWN_SHOOT:
			fire()

	def player_delta(self):
		dxs = [-3, 3, -1, 1]
		mag = dxs[action]
		dx, dy = delta
		return mag + dx, 2 + dy

	def jump(self):
		pass

	def fire(self):
		bullet = Bullet(pos)
		Bullet.bullets.append(bullet)
		print("bullet count = %d" % len(Bullet.bullets))