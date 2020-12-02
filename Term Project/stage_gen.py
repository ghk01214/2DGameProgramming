from pico2d import *
import gfw
import game_object
from platform import Platform

UNIT_PER_LINE = 25
SCREEN_LINES = 19
BLOCK_SIZE = 32

lines = []

def load(file):
	global lines, current_x, create_at, map_index
	with open(file, 'r') as f:
		lines = f.readlines()

	current_x = 15
	map_index = 0
	create_at = get_canvas_width()

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
	if ch == 'b':
		y -= BLOCK_SIZE // 2
		x -= BLOCK_SIZE // 2
		obj = Platform(ord(ch) - ord('b'), x, y)
		gfw.world.add(gfw.layer.platform, obj)
	elif ch == 's':
		dy = 1
		y -= int(dy * BLOCK_SIZE) // 2
		x -= BLOCK_SIZE // 2
		#obj = Platform(ord(ch) - ord('b'), x, y)
		#gfw.world.add(gfw.layer.platform, obj)

def get(x, y):
	col = x % UNIT_PER_LINE
	row = x // UNIT_PER_LINE * SCREEN_LINES + SCREEN_LINES - 1 - y
	return lines[row][col]