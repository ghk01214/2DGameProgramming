from pico2d import *
from game_object import *
import gfw
from bullet import Bullet

class Player:
	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_LEFT): 	(-1,  0),
		(SDL_KEYDOWN, SDLK_RIGHT): 	( 1,  0),
		(SDL_KEYDOWN, SDLK_DOWN): 	( 0, -1),
		(SDL_KEYDOWN, SDLK_UP): 	( 0,  1),
		(SDL_KEYUP, SDLK_LEFT): 	( 1,  0),
		(SDL_KEYUP, SDLK_RIGHT):	(-1,  0),
		(SDL_KEYUP, SDLK_DOWN): 	( 0,  1),
		(SDL_KEYUP, SDLK_UP): 		( 0, -1),
	}

	KEYDOWN_JUMP = (SDL_KEYDOWN, SDLK_LCTRL)
	KEYDOWN_SHOOT = (SDL_KEYDOWN, SDLK_z)

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
		self.frame = int(frame) % self.imageData[0]

	def draw(self):
		width, height = self.imageData[1], 25
		sx = self.frame * width
		sy = self.action * height
		pos = self.background.to_screen(self.pos)
			
		self.image.clip_draw(sx, sy, 28, 25, *pos)

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
				self.imageData = 5, 29
			else:
				self.imageData = 4, 28
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
		if self.state in [Player.FALLING, Player.DOUBLE_JUMP]:
			return

		if self.state in [Player.RUNNING, Player.STANDING]:
			self.state = Player.JUMPING
		elif self.state == Player.JUMPING:
			self.state = Player.DOUBLE_JUMP

		self.jump_speed = Player.JUMP * self.mag
	def update_mag(self):
		if self.mag_speed == 0:
			return

		x, y = self.pos
		_, b, _, _ = self.get_bb()
		diff = y - b
		prev_mag = self.mag

		self.mag += self.mag_speed * gfw.delta_time
		if self.mag > 2.0:
			self.mag = 2.0
			self.mag_speed = 0
		elif self.mag < 1.0:
			self.mag = 1.0
			self.mag_speed = 0

	def fire(self):
		bullet = Bullet(pos)
		Bullet.bullets.append(bullet)
		print("bullet count = %d" % len(Bullet.bullets))