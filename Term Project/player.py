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

	GRAVITY = 3000
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
		self.left, self.right, self.top = 0, 0, 0

		global center
		center = self.pos

	def update(self):
		x, y = self.pos
		dx, dy = self.delta
		if self.state in [Player.JUMPING, Player.DOUBLE_JUMP, Player.FALLING, Player.DOUBLE_FALL]:
			x, y = self.move((0, self.jump_speed * gfw.delta_time))
			self.jump_speed -= Player.GRAVITY * self.mag * gfw.delta_time

		self.left, feet, self.right, self.top = self.get_bb()
					x, y = self.move((0, top - feet))
					self.state = Player.STANDING
					self.jump_speed = 0

		x += dx * self.speed * self.mag * gfw.delta_time
		y += dy * self.speed * self.mag * gfw.delta_time

		bg_l, bg_b, bg_r, bg_t = self.background.get_boundary()
		x = clamp(bg_l, x, bg_r)
		y = clamp(bg_b, y, bg_t)

		self.pos = x, y
		self.time += gfw.delta_time
		frame = self.time * 17
		self.frame = int(frame) % self.imageType
		#gravity = 0.05
		#self.delta = dx, dy - gravity

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
					print(sel_top)
					print(left, bottom, right, top)
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
		if self.state in [Player.DOUBLE_JUMP, Player.DOUBLE_FALL]:
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