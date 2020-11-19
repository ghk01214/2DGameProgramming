from pico2d import *
import gfw

MOVE_FPS = 300

def init():
	global image, pos, delta_x, delta_y, radius

	image = gfw.image.load('res/player.png')
	pos = get_canvas_width() // 2, get_canvas_height() // 2

	delta_x, delta_y = 0, 0
	radius = image.w // 2

def update():
	global pos

	x, y = pos
	x += delta_x * MOVE_FPS * gfw.delta_time
	y += delta_y * MOVE_FPS * gfw.delta_time

	half_width, half_height = image.w // 2, image.h // 2
	x = clamp(half_width, x, get_canvas_width() - half_width)
	y = clamp(half_height, y, get_canvas_height() - half_height)

	pos = x, y

def draw():
	image.draw(*pos)

def handle_event(e):
	global delta_x, delta_y
	if e.type == SDL_KEYDOWN:
		if e.key == SDLK_LEFT:
			delta_x -= 1
		elif e.key == SDLK_RIGHT:
			delta_x += 1
		elif e.key == SDLK_UP:
			delta_y += 1
		elif e.key == SDLK_DOWN:
			delta_y -= 1
	elif e.type == SDL_KEYUP:
		if e.key == SDLK_LEFT:
			delta_x += 1
		elif e.key == SDLK_RIGHT:
			delta_x -= 1
		elif e.key == SDLK_UP:
			delta_y -= 1
		elif e.key == SDLK_DOWN:
			delta_y += 1