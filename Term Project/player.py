from pico2d import *
from game_object import *
import gfw
import game_object
from bullet import Bullet

class Player:
	STANDING, RUNNING, JUMPING, DOUBLE_JUMP, FALLING, DOUBLE_FALL = range(6)
	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_LEFT):	(-1,  0),
		(SDL_KEYDOWN, SDLK_RIGHT): 	( 1,  0),
		(SDL_KEYUP, SDLK_LEFT): 	( 1,  0),
		(SDL_KEYUP, SDLK_RIGHT): 	(-1,  0),
		(SDL_KEYDOWN, SDLK_UP):		( 0,  1),
		(SDL_KEYDOWN, SDLK_DOWN): 	( 0, -1),
		(SDL_KEYUP, SDLK_UP): 		( 0, -1),
		(SDL_KEYUP, SDLK_DOWN): 	( 0,  1),
	}

	BB_DIFFS = [
		(-14, -12, 12, 10),	#STANDING
		(-14, -12, 12, 10),	#RUNNING
		(-11, -12, 11, 10),	#JUMPING
		(-11, -12, 11, 10),	#DOUBLE_JUMP
		(-14, -12, 12, 10),	#FALLING
		(-14, -12, 12, 10),	#DOUBLE_FALL
	]

	KEYDOWN_JUMP = (SDL_KEYDOWN, SDLK_LCTRL)
	KEYDOWN_SHOOT = (SDL_KEYDOWN, SDLK_z)

	GRAVITY = 2000
	JUMP = 500

	def __init__(self):
		self.image = gfw.image.load(resBM('animation.png'))
		self.pos = 600, 530
		self.delta = 0, 0
		self.speed = 200
		self.time = 0
		self.frame = 0
		self.action = 7
		self.mag = 1
		self.mag_speed = 0
		self.state = Player.STANDING
		self.width, self.height = 28, 25
		self.imageType = 4
		self.jump_speed = 0

		global center
		center = self.pos

	def update(self):
		x, y = self.pos
		dx, dy = self.delta
		self.time += gfw.delta_time

		if self.state in [Player.JUMPING, Player.DOUBLE_JUMP, Player.FALLING, Player.DOUBLE_FALL]:
			x, y = self.move((0, self.jump_speed * gfw.delta_time))
			self.jump_speed -= Player.GRAVITY * self.mag * gfw.delta_time

		if self.state == 0:
			print('stand')
		elif self.state == 1:
			print('run')
		elif self.state == 2:
			print('jump')
		elif self.state == 3:
			print('double jump')
		elif self.state == 4:
			print('fall')
		elif self.state == 5:
			print('double fall')

		left, feet, right, top = self.get_bb()

		if feet < 0:
			x, y = self.move((0, get_canvas_height()))

		platform = self.get_platform(feet)

		if platform is not None:
			p_left, p_bottom, p_right, p_top = platform.get_bb()

			if self.state in [Player.STANDING, Player.RUNNING]:
				if feet > p_top:
					self.state = Player.FALLING
					self.jump_speed = 0
			else:
				if self.jump_speed < 0:
					if self.state == Player.JUMPING:
						self.state = Player.FALLING
					elif self.state == Player.DOUBLE_JUMP:
						self.state = Player.DOUBLE_FALL

					if int(feet) <= p_top:
						_, y = self.move((0, p_top - feet))
						self.state = Player.STANDING
						self.jump_speed = 0
					self.jump_speed = 0

		x += dx * self.speed * self.mag * gfw.delta_time
		y += dy * self.speed * self.mag * gfw.delta_time

		self.pos = x, y
		frame = self.time * 17
		self.frame = int(frame) % self.imageType

	def draw(self):
		x, y = self.pos
		sx = self.frame * self.width
		sy = self.action * self.height + 1

		self.pos = x, y			
		self.image.clip_draw(sx, sy, self.width, self.height, *self.pos)

	def move(self, diff):
		x, y = game_object.point_add(self.pos, diff)
		return x, y

	def get_platform(self, feet):
		selected = None
		sel_top = 0
		x, y = self.pos

		for platform in gfw.world.objects_at(gfw.layer.platform):
			left, bottom, right, top = platform.get_bb()

			if x < left or x > right:
				continue

			mid = (bottom + top) // 2

			if feet < mid:
				continue

			if selected is None:
				selected = platform
				sel_top = top
			else:
				if top > sel_top:
					#print(sel_top)
					#print(left, bottom, right, top)
					selected = platform
					sel_top = top

		return selected

	def get_bb(self):
		left, bottom, right, top = Player.BB_DIFFS[self.state]
		x, y = self.pos
		if self.mag != 1:
			left *= self.mag
			bottom *= self.mag
			right *= self.mag
			top *= self.mag

		return x + left, y + bottom, x + right, y + top

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
				#self.state = Player.RUNNING
			else:
				self.imageType = 4
				self.width = 28
				#self.state = Player.STANDING

		elif pair == Player.KEYDOWN_JUMP:
			self.jump()
		elif pair == Player.KEYDOWN_SHOOT:
			fire()

	def jump(self):
		if self.state == Player.DOUBLE_JUMP:
			if self.jump_speed < 0:
				self.state = Player.DOUBLE_FALL
			return
		elif self.state in [Player.STANDING, Player.RUNNING]:
			self.state = Player.JUMPING
		elif self.state == Player.JUMPING:
			self.state = Player.DOUBLE_JUMP
		elif self.state == Player.FALLING:
			self.state = Player.DOUBLE_FALL

		self.jump_speed = Player.JUMP * self.mag

	def fire(self):
		bullet = Bullet(pos)
		Bullet.bullets.append(bullet)
		print("bullet count = %d" % len(Bullet.bullets))