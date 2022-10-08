from pico2d import *
from game_object import *
import gfw
import game_object
from object import Bullet
import music

class Player:
	STANDING, RUNNING, JUMPING, DOUBLE_JUMP, FALLING, DOUBLE_FALL, DEAD = range(7)
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
		(-14, -12, 12, 10),	#DEAD
	]

	JUMP_MAP = (SDL_KEYDOWN, SDLK_x)
	SHOOT_MAP = (SDL_KEYDOWN, SDLK_z)

	GRAVITY = 2000
	JUMP = 500

	def __init__(self):
		self.image = gfw.image.load(resBM('animation.png'))
		self.pos = 600, 530		# 1 Stage
		#self.pos = 50, 524		# 2 Stage
		#self.pos = 15, 364		# 3 Stage
		#self.pos = 15, 492		# 4, 5 Stage
		self.delta = 0
		self.speed = 200
		self.time = 0
		self.frame = 0
		self.action = Player.FALL_L
		self.mag = 1
		self.mag_speed = 0
		self.state = Player.FALLING
		self.width, self.height = 28, 25
		self.imageType = 2
		self.jump_speed = 0
		self.on_floor = False

		self.jump_sound = None
		self.dead_sound = None
		self.shot_sound = None
		self.coffin_dance = None
		self.play_over = 0
		self.saved = False
		self.bullet = None
		self.saveImage = gfw.image.load(resBM('save(a).png'))
		self.save_time = -1
		self.save_point = None
		self.game_over = gfw.image.load(resBM('game_over.png'))
		self.revived = False

	def update(self):
		x, y = self.pos
		dx = self.delta
		self.time += gfw.delta_time

		if self.save_time >= 0.0 and self.save_time < 1.0:
			self.save_time += gfw.delta_time

		if self.save_time > 1.0:
			self.save_time = -1

		if self.state in [Player.JUMPING, Player.DOUBLE_JUMP, Player.FALLING, Player.DOUBLE_FALL]:
			_, y = self.move((0, self.jump_speed * gfw.delta_time))
			self.jump_speed -= Player.GRAVITY * gfw.delta_time

		x, y, self.left = self.collides_platform(x, y, dx)
		self.collides_spike(x, y, dx)

		if self.bullet is not None:
			self.bullet_collision()

		if self.state != Player.DEAD:
			temp_x = x
			x, _ = self.move((dx * self.speed * self.mag * gfw.delta_time, 0))

			if x < self.width // 2:
				x = temp_x

			if y > get_canvas_height() - self.height // 2:
				self.state = Player.FALLING
				_, y = self.move((0, self.jump_speed * gfw.delta_time))
				self.jump_speed -= Player.GRAVITY * gfw.delta_time

			self.pos = x, y
			frame = self.time * 17
			self.frame = int(frame) % self.imageType

			self.dead_sound = None
			self.play_over = 0
		else:
			self.play_over += 1

			if self.play_over == 1:
				self.dead_sound = music.wav(game_object.resSE('dead.wav'), False)

	def draw(self):
		x, y = self.pos
		sx = self.frame * self.width
		sy = self.action * self.height + 1

		if self.save_time > 0.0 and self.save_time < 1.0:
			self.saveImage.clip_draw_to_origin(0, 0, self.save_point.width, self.save_point.height, self.save_point.left, self.save_point.bottom)
		
		if self.state != Player.DEAD:
			self.image.clip_draw(sx, sy, self.width, self.height, *self.pos)
		
		if self.play_over > 0:
			self.game_over.draw(get_canvas_width() // 2, get_canvas_height() // 2)

	def move(self, diff):
		x, y = game_object.point_add(self.pos, diff)

		return x, y

	def get_bb(self):
		left, bottom, right, top = Player.BB_DIFFS[self.state]
		x, y = self.pos

		return x + left, y + bottom, x + right, y + top

	def get_obj(self, feet, layer):
		selected = None
		sel_top = 0
		x, _ = self.pos

		for platform in gfw.world.objects_at(layer):
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
					selected = platform
					sel_top = top

		return selected

	def get_obj_wall(self, selfLeft, selfRight, layer):
		selected = None
		_, y = self.pos

		for platform in gfw.world.objects_at(layer):
			left, bottom, right, top = platform.get_bb()

			if y > top or y < bottom:
				continue

			if selfRight < left or selfLeft > right:
				continue

			selected = platform

		return selected

	def get_obj_roof(self, head, layer):
		selected = None
		sel_bottom = 0
		x, _ = self.pos

		for platform in gfw.world.objects_at(layer):
			left, bottom, right, top = platform.get_bb()

			if x < left or x > right:
				continue

			mid = (bottom + top) // 2

			if head > mid:
				continue

			if selected is None:
				selected = platform
				break

		return selected

	def collides_platform(self, x, y, dx):
		left, feet, right, head = self.get_bb()

		platform = self.get_obj(feet, gfw.layer.platform)
		roof = self.get_obj_roof(head, gfw.layer.platform)
		wall = self.get_obj_wall(left, right, gfw.layer.platform)

		#바닥과의 충돌처리
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

					if self.action in [Player.JUMP_L, Player.JUMP_R]:
						self.action -= 2
						self.width = 28

					if int(feet) <= p_top:
						_, y = self.move((0, p_top - feet))

						if self.action in [Player.FALL_L, Player.FALL_R] and self.state in [Player.FALLING, Player.DOUBLE_FALL]:
							self.action += 6
							self.width = 28
							self.imageType = 4

						self.state = Player.STANDING
						self.jump_speed = 0
						self.on_floor = True

		#천장과의 충돌처리
		if roof is not None:
			_, r_bottom, _, _ = roof.get_bb()

			if self.state in [Player.JUMPING, Player.DOUBLE_JUMP]:
				if head > r_bottom:
					if self.state == Player.JUMPING:
						self.state = Player.FALLING
					elif self.state == Player.DOUBLE_JUMP:
						self.state = Player.DOUBLE_JUMP

					self.jump_speed = 0
					_, y = self.move((0, self.jump_speed * gfw.delta_time))
					self.jump_speed -= Player.GRAVITY * gfw.delta_time

		#벽과의 충돌처리
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

		return x, y, left

	def collides_spike(self, x, y, dx):
		left, feet, right, head = self.get_bb()

		spike = self.get_obj(feet, gfw.layer.spike)
		roof = self.get_obj_roof(head, gfw.layer.spike)
		wall = self.get_obj_wall(left, right, gfw.layer.spike)

		#바닥과의 충돌처리
		if spike is not None:
			_, _, _, p_top = spike.get_bb()

			if self.jump_speed < 0:
				if self.state == Player.JUMPING:
					self.state = Player.FALLING
				elif self.state == Player.DOUBLE_JUMP:
					self.state = Player.DOUBLE_FALL

				if int(feet) <= p_top:
					_, y = self.move((0, p_top - feet))
					self.state = Player.DEAD
					self.jump_speed = 0

		#천장과의 충돌처리
		if roof is not None:
			_, r_bottom, _, _ = roof.get_bb()

			if self.state in [Player.JUMPING, Player.DOUBLE_JUMP]:
				if head > r_bottom:
					self.jump_speed = 0
					self.state = Player.DEAD
					_, y = self.move((0, self.jump_speed * gfw.delta_time))

		#벽과의 충돌처리
		if wall is not None:
			w_left, _, w_right, _ = wall.get_bb()

			#왼쪽 방향
			if dx == -1 and w_right > left and w_left < left:
				self.state = Player.DEAD
			#오른쪽 방향
			elif dx == 1 and w_left < right and w_left > left:
				self.state = Player.DEAD

	def bullet_collision(self):
		left, bottom, right, top = self.bullet.get_bb()

		wall = self.get_bullet(gfw.layer.platform)
		spike = self.get_bullet(gfw.layer.spike)
		save = self.get_bullet(gfw.layer.save)

		if wall is not None:
			w_left, _, w_right, _ = wall.get_bb()

			if right > w_left or left < w_right:
				gfw.world.remove(self.bullet)
				self.bullet = None

		if spike is not None:
			s_left, _, s_right, _ = spike.get_bb()

			mid = (s_left + s_right) // 2

			if right > mid or left < mid:
				gfw.world.remove(self.bullet)
				self.bullet = None

		if save is not None:
			c_left, _, c_right, _ = save.get_bb()

			if left > c_left or right < c_right:
				gfw.world.remove(self.bullet)
				self.bullet = None
				self.saved = True
				self.save_time = 0
				self.save_point = save

	def get_bullet(self, layer):
		selected = None

		for platform in gfw.world.objects_at(layer):
			left, bottom, right, top = platform.get_bb()

			if self.bullet.y > top or self.bullet.y < bottom:
				continue

			if self.bullet.x < left or self.bullet.x > right:
				continue

			selected = platform

		return selected

	def handle_event(self, e):
		pair = (e.type, e.key)

		if pair in Player.KEY_MAP and self.state != Player.DEAD:
			if self.revived and e.type == SDL_KEYUP:
				pass
			else:
				pdx = self.delta
				self.delta, _ = point_add((self.delta, 0), Player.KEY_MAP[pair])
				dx = self.delta

				self.action = \
					Player.RUN_L if dx < 0 else \
					Player.RUN_R if dx > 0 else \
					Player.STAND_L if pdx < 0 else Player.STAND_R

				if self.action in [Player.RUN_L, Player.RUN_R]:
					self.imageType = 5
					self.width = 29
				elif self.action in [Player.STAND_L, Player.STAND_R]:
					self.imageType = 4
					self.width = 28

			self.revived = False

		elif pair == Player.JUMP_MAP:
			self.jump()
		elif pair == Player.SHOOT_MAP:
			self.fire()

	def jump(self):
		if self.state in [Player.DOUBLE_JUMP, Player.DOUBLE_FALL]:
			return
		elif self.state in [Player.STANDING, Player.RUNNING]:
			self.state = Player.JUMPING
			self.jump_sound = music.wav(game_object.resSE('jump.wav'), False)
		elif self.state in [Player.JUMPING, Player.FALLING]:
			self.state = Player.DOUBLE_JUMP
			self.jump_sound = music.wav(game_object.resSE('double_jump.wav'), False)

		if self.action in [Player.STAND_L, Player.RUN_L, Player.JUMP_L, Player.FALL_L]:
			self.action = Player.JUMP_L
		elif self.action in [Player.STAND_R, Player.RUN_R, Player.JUMP_R, Player.FALL_R]:
			self.action = Player.JUMP_R

		self.imageType = 2
		self.width = 22
		self.jump_speed = Player.JUMP

	def fire(self):
		left, _, right, _ = self.get_bb()
		_, y = self.pos

		if self.action in [Player.STAND_L, Player.RUN_L, Player.JUMP_L, Player.FALL_L]:
			direction = -1
			x = left
		else:
			direction = 1
			x = right

		self.bullet = Bullet(x, y, direction)
		self.shot_sound = music.wav(game_object.resSE('bullet.wav'), False)
		gfw.world.add(gfw.layer.bullet, self.bullet)