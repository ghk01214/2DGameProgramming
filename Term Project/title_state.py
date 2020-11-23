from pico2d import *
import gfw
from game_object import *
import game_state

def enter():
	global image
	image = gfw.image.load(resBM('title.png'))

def update():
	pass

def draw():
	image.draw(400, 300)

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			gfw.pop()
		elif e.key == SDLK_q:
			gfw.quit()
		elif e.key == SDLK_SPACE:
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