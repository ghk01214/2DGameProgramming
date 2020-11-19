from pico2d import *
import gfw
import random
from missile import Missile

MISSILE_COUNT = 10

def init():
	pass

def update():
	while gfw.world.count_at(gfw.layer.missile) < MISSILE_COUNT:
		generate()

def generate():
	x, y, dx, dy = get_grid()
	missile = Missile((x, y), (dx, dy))
	gfw.world.add(gfw.layer.missile, missile)

def get_grid():
	x, y = random.randrange(get_canvas_width()), random.randrange(get_canvas_height())
	dx, dy = random.random(), random.random()
	side = random.randint(1, 4)

	if dx < 0.5:
		dx -= 1

	if dy < 0.5:
		dy -= 1

	if side == 1:	#left
		x = 0
	elif side == 2:	#bottom
		y = 0
	elif side == 3:	#right
		x = get_canvas_width()
	else:			#top
		y = get_canvas_height()

	return x, y, dx, dy