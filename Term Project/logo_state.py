from pico2d import *
import gfw
from game_object import *
import title_state
import time

def enter():
	global image
	global logo_time

	image = gfw.image.load(resBM('logo.png'))
	logo_time = 0

def update():
	global logo_time

	logo_time += gfw.delta_time

	if logo_time > 1.0:
		gfw.change(title_state)

def draw():
	image.draw(400, 300)

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_q):
		gfw.quit()
	elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
		gfw.push(game_state)

def pause():
	pass

def resume():
	pass

def exit():
	global image
	del image

if __name__ == '__main__':
	gfw.run_main()