from pico2d import *
from game_object import *
import gfw
import game_object
from bullet import Bullet

class Player:
	STANDING, RUNNING, JUMPING, DOUBLE_JUMP, FALLING, DOUBLE_FALL = range(6)
	FALL_L, FALL_R, JUMP_L, JUMP_R, RUN_L, RUN_R, STAND_L, STAND_R = range(8)
	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_LEFT):	(-1,  0),
		(SDL_KEYDOWN, SDLK_RIGHT): 	( 1,  0),
		(SDL_KEYUP, SDLK_LEFT): 	( 1,  0),
		(SDL_KEYUP, SDLK_RIGHT): 	(-1,  0),
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
		self.action = Player.STAND_L
		self.mag = 1
		self.mag_speed = 0
		self.state = Player.STANDING
		self.width, self.height = 28, 25
		self.imageType = 4
		self.jump_speed = 0

	def update(self):
		x, y = self.pos
		dx, dy = self.delta
		self.time += gfw.delta_time

		if self.state in [Player.JUMPING, Player.DOUBLE_JUMP, Player.FALLING, Player.DOUBLE_FALL]:
			_, y = self.move((0, self.jump_speed * gfw.delta_time))
			self.jump_speed -= Player.GRAVITY * gfw.delta_time

		left, feet, right, head = self.get_bb()

		if feet < 0:
			x, y = self.move((0, get_canvas_height()))

		platform = self.get_platform(feet)
		roof = self.get_roof(head)
		wall = self.get_wall(left, right)

		if platform is not None:
			_, _, _, p_top = platform.get_bb()

			if self.state in [Player.STANDING, Player.RUNNING]:
				if feet > p_top:
					self.state = Player.FALLING
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

		if roof is not None:
			_, r_bottom, _, _ = roof.get_bb()

			if head > r_bottom:
				self.jump_speed = 0
				self.state = Player.FALLING
				_, y = self.move((0, self.jump_speed * gfw.delta_time))
				self.jump_speed -= Player.GRAVITY * gfw.delta_time


		if wall is not None:
			w_left, _, w_right, _ = wall.get_bb()

			#왼쪽 방향
			if dx == -1 and w_right > left and w_left < left:
				self.mag = 0
			#오른쪽 방향
			elif dx == 1 and w_left < right and w_left > left:
				self.mag = 0
			else:
				self.mag = 1
		else:
			self.mag = 1

#			if y > mid and self.jump_speed <= 0:
#				if dx == -1 and w_right > left and w_left < left:
#					x, y = w_right - self.width // 2, w_top
#					self.jump_speed = 0
#				elif dx == 1 and w_left < right and w_left > left:
#					x, y = w_left - self.width // 2, w_top
#					self.jump_speed = 0

		#y += dy * self.speed * self.mag * gfw.delta_time
		x += dx * self.speed * self.mag * gfw.delta_time
		self.pos = x, y
		frame = self.time * 17
		self.frame = int(frame) % self.imageType

	def draw(self):
		x, y = self.pos
		sx = self.frame * self.width
		sy = self.action * self.height + 1
	
		self.image.clip_draw(sx, sy, self.width, self.height, *self.pos)

	def move(self, diff):
		x, y = game_object.point_add(self.pos, diff)
		return x, y

	def get_bb(self):
		left, bottom, right, top = Player.BB_DIFFS[self.state]
		x, y = self.pos

		return x + left, y + bottom, x + right, y + top

	def get_platform(self, feet):
		selected = None
		sel_top = 0
		x, _ = self.pos

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

	def get_wall(self, selfLeft, selfRight):
		selected = None
		_, y = self.pos

		for platform in gfw.world.objects_at(gfw.layer.platform):
			left, bottom, right, top = platform.get_bb()

			if y > top or y < bottom:
				continue

			if selfRight < left or selfLeft > right:
				continue

			selected = platform

		return selected

	def get_roof(self, head):
		selected = None
		sel_bottom = 0
		x, _ = self.pos

		for platform in gfw.world.objects_at(gfw.layer.platform):
			left, bottom, right, top = platform.get_bb()

			if x < left or x > right:
				continue

			mid = (bottom + top) // 2

			if head > mid:
				continue

			if selected is None:
				selected = platform
				sel_bottom = bottom
				break

		return selected

	def handle_event(self, e):
		pair = (e.type, e.key)

		if pair in Player.KEY_MAP:
			pdx, _ = self.delta
			self.delta = point_add(self.delta, Player.KEY_MAP[pair])
			dx, _ = self.delta
			self.action = \
				Player.RUN_L if dx < 0 else \
				Player.RUN_R if dx > 0 else \
				Player.STAND_L if pdx < 0 else Player.STAND_R

			if self.action in [Player.RUN_L, Player.RUN_R]:
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
		if self.state == Player.DOUBLE_FALL:
			return
		elif self.state in [Player.STANDING, Player.RUNNING]:
			self.state = Player.JUMPING
		elif self.state in [Player.JUMPING, Player.FALLING]:
			self.state = Player.DOUBLE_JUMP

		self.jump_speed = Player.JUMP

	def fire(self):
		bullet = Bullet(pos)
		Bullet.bullets.append(bullet)
		print("bullet count = %d" % len(Bullet.bullets))