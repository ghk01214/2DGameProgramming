from pico2d import *
import gfw
from game_object import *
import title
import time
import music

def enter():
	global image, logo_time, bgm

	image = gfw.image.load(resBM('logo.png'))
	logo_time = 0
	bgm = music.mp3(resSE('logo.mp3'), False)

def update():
	global logo_time, bgm

	logo_time += gfw.delta_time

	if logo_time > 3.0:
		gfw.change(title)

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

def pause():
	pass

def resume():
	pass

def exit():
	global image
	del image

if __name__ == '__main__':
	gfw.run_main()