from pico2d import *
import gfw

MOVE_FPS = 300
MAX_LIFE = 5

def init():
	global image, red_heart, white_heart
	global pos, delta_x, delta_y, radius, life
	image = gfw.image.load('res/player.png')
	red_heart = gfw.image.load('res/heart_red.png')
	white_heart = gfw.image.load('res/heart_white.png')
	pos = get_canvas_width() // 2, get_canvas_height() // 2

	delta_x, delta_y = 0, 0
	radius = image.w // 2
	life = MAX_LIFE

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
	x, y = get_canvas_width() - 30, get_canvas_height() - 30

	image.draw(*pos)
	for i in range(MAX_LIFE):
		heart = red_heart if i < life else white_heart
		heart.draw(x, y)
		x -= heart.w

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

def increase_life():
	global life

	if life == MAX_LIFE:
		return True

	life += 1

	return False

def decrease_life():
	global life

	life -= 1
	print(life)

	return life <= 0