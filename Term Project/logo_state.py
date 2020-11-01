from pico2d import *
import game_framework as gfw
import title_state
import time

RES_BACK = 'res/bitmap/background/'

def enter():
	global image
	global logo_time

	image = load_image(RES_BACK + 'Logo.png')
	logo_time = 0

def update():
	global logo_time

	logo_time += game_framework.delta_time

	if logo_time > 1.0:
		game_framework.change(title_state)

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
	game_framework.run_main()