from pico2d import *
import gfw
import game_object
from object import Save
from plat import Platform
from spike import Spike, HalfSpike

UNIT_PER_LINE = 25
SCREEN_LINES = 19
BLOCK_SIZE = 32

lines = []

def load(file, end):
	global lines, current_x, create_at, map_index, ending
	with open(file, 'r') as f:
		lines = f.readlines()

	current_x = 15
	map_index = 0
	create_at = get_canvas_width()
	ending = end

def update():
	while current_x < create_at:
		create_column()

def create_column():
	global current_x, map_index
	y = BLOCK_SIZE // 2

	for row in range(SCREEN_LINES):
		ch = get(map_index, row)
		create_object(ch, current_x, y)
		y += BLOCK_SIZE

	current_x += BLOCK_SIZE
	map_index += 1

ignore_char_map = set()

def create_object(ch, x, y):
	global ending

	x -= BLOCK_SIZE // 2
	y -= BLOCK_SIZE // 2

	if ch == 'b':
		obj = Platform(x, y)
		gfw.world.add(gfw.layer.platform, obj)
	elif ch == 's':
		obj = Spike(x, y)
		gfw.world.add(gfw.layer.spike, obj)
	elif ch == 'l':
		obj = HalfSpike(0, x, y)
		gfw.world.add(gfw.layer.spike, obj)
	elif ch == 'f':
		obj = HalfSpike(1, x, y)
		gfw.world.add(gfw.layer.spike, obj)
	elif ch == 'r':
		obj = HalfSpike(2, x, y)
		gfw.world.add(gfw.layer.spike, obj)
	elif ch == 't':
		obj = HalfSpike(3, x, y)
		gfw.world.add(gfw.layer.spike, obj)
	elif ch == 'c':
		obj = Save(x, y)
		gfw.world.add(gfw.layer.save, obj)

def get(x, y):
	col = x % UNIT_PER_LINE
	row = x // UNIT_PER_LINE * SCREEN_LINES + SCREEN_LINES - 1 - y
	return lines[row][col]

def remove():
	for obj in gfw.world.objects_at(gfw.layer.platform):
		gfw.world.remove(obj)

	for obj in gfw.world.objects_at(gfw.layer.spike):
		gfw.world.remove(obj)

	for obj in gfw.world.objects_at(gfw.layer.save):
		gfw.world.remove(obj)