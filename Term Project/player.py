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

	KEYDOWN_Z = (SDL_KEYDOWN, SDLK_z)

	def __init__(self):
		self.image = gfw.image.load(resBM('animation.png'))
		self.pos = get_canvas_width() // 2, get_canvas_height() // 2
		self.delta = 0, 0
		self.target = None
		self.speed = 200
		self.time = 0
		self.frame = 0
		self.action = 7
		self.mag = 1
		self.imageData = 4, 28

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
		self.frame = int(frame) % 4

	def draw(self):
		width, height = 29, 25
		sx = self.frame * width
		sy = self.action * height
		pos = self.background.to_screen(self.pos)
			
		self.image.clip_draw(sx, sy, 28, 25, *pos)

	def handle_event(self, e):
		pair = (e.type, e.key)

		if pair in Player.KEY_MAP:
			if self.target is not None:
				self.target = None
				self.delta = 0, 0

			pdx = self.delta[0]
			self.delta = point_add(self.delta, Player.KEY_MAP[pair])
			dx = self.delta[0]
			self.action = \
				1 if dx < 0 else 0

			if pair[0] == SDL_KEYDOWN:
				change_image = True
			else:
				change_image = False;
		elif pair == Player.KEYDOWN_Z:
			fire()

	def player_delta(self):
		dxs = [-3, 3, -1, 1]
		mag = dxs[action]
		dx, dy = delta
		return mag + dx, 2 + dy

	def fire(self):
		bullet = Bullet(pos)
		Bullet.bullets.append(bullet)
		print("bullet count = %d" % len(Bullet.bullets))