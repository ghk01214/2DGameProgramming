from pico2d import *
import gfw
import random
from missile import *

MISSILE_NUM = 10
ITEM_NUM = 2

def init():
	pass

def update(s):
	global score
	score = s
	max_missile_num = MISSILE_NUM + score // 10

	while gfw.world.count_at(gfw.layer.missile) < MISSILE_NUM:
		generate_missile()

	while gfw.world.count_at(gfw.layer.item) < ITEM_NUM:
		generate_item()

def generate_missile():
	x, y, dx, dy = get_grid()
	missile = Missile((x, y), (dx, dy))
	gfw.world.add(gfw.layer.missile, missile)

def generate_item():
	x, y, dx, dy = get_grid()
	Item = random.choice([PresentBox, Coin])
	item = Item((x, y), (dx, dy))
	gfw.world.add(gfw.layer.item, item)

def get_grid():
	x, y = random.randrange(get_canvas_width()), random.randrange(get_canvas_height())
	dx, dy = random.random(), random.random()
	side = random.randint(1, 4)
	speed = 1 + score / 60

	if dx < 0.5:
		dx -= 1

	if dy < 0.5:
		dy -= 1

	dx *= speed
	dy *= speed

	if side == 1:	#left
		x = 0
	elif side == 2:	#bottom
		y = 0
	elif side == 3:	#right
		x = get_canvas_width()
	else:			#top
		y = get_canvas_height()

	return x, y, dx, dy