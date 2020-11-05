from pico2d import *
from game_object import *
import game_framework_image

RES_ANIMATION = 'res/bitmap/sprite/'

class Player:
	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_LEFT): (-3, 0),
		(SDL_KEYDOWN, SDLK_RIGHT): (3, 0),
		(SDL_KEYDOWN, SDLK_DOWN): (0, -3),
		(SDL_KEYDOWN, SDLK_UP): (0, 3),
		(SDL_KEYUP, SDLK_LEFT): (3, 0),
		(SDL_KEYUP, SDLK_RIGHT): (-3, 0),
		(SDL_KEYUP, SDLK_DOWN): (0, 3),
		(SDL_KEYUP, SDLK_UP): (0, -3),
	}

	KEYDOWN_Z = (SDL_KEYDOWN, SDLK_z)

	image = None

	def __init__(self):
		if self.image == None:
			self.image = gfwi.load(RES_ANIMATION + 'Idle.png')

		self.pos = get_canvas_width() // 2, get_canvas_height() // 2
		self.delta = 0, 0
		self.frame = 0
		self.action = 0

	def draw(self):
		sx = self.frame * 28
		sy = self.action * 25
		self.image.clip_draw(sx, sy, 28, 25, *self.pos)

	def fire(self):
		bullet = Bullet(self.pos)
		Bullet.bullets.append(bullet)
		print("bullet count = %d" % len(Bullet.bullets))

	def handle_event(self, e):
		pair = (e.type, e.key)

		if pair[0] == SDL_KEYDOWN:
			if pair[1] == SDLK_UP or pair[1] == SDLK_DOWN or pair[1] == SDLK_LEFT or pair[1] == SDLK_RIGHT:
				self.image = gfwi.load(RES_ANIMATION + 'Run.png')
		else:
			self.image = gfwi.load(RES_ANIMATION + 'Idle.png')

		if pair in Player.KEY_MAP:
			self.update_delta(*Player.KEY_MAP[pair])
		elif pair == Player.KEYDOWN_Z:
			self.fire()

	def player_delta(self):
		dxs = [-3, 3, -1, 1]
		mag = dxs[self.action]
		dx, dy = self.delta
		return mag+dx, 2 + dy

	def update(self):
		x, y = self.pos
		dx, dy = self.delta
		self.pos = x + dx, y + dy
		self.frame = (self.frame + 1) % 4
		gravity = 0.05
		self.delta = dx, dy - gravity

	def update_delta(self, ddx, ddy):
		dx, dy = self.delta
		dx += ddx
		dy += ddy

		if ddx != 0:
			self.action = \
				0 if dx > 0 else \
				1 if dx < 0 else \
				1 if ddx > 0 else 0

		self.delta = dx, dy