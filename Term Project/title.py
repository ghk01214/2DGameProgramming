from pico2d import *
import gfw
from game_object import *
import main
import music

def enter():
	global image, bgm
	image = gfw.image.load(resBM('title.png'))
	bgm = music.mp3(resSE('title.mp3'), True)

def update():
	pass

def draw():
	image.draw(400, 300)

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key in [SDLK_ESCAPE, SDLK_q]:
			gfw.quit()
		elif e.key in [SDLK_RETURN, SDLK_KP_ENTER]:
			gfw.push(main)

def pause():
	pass

def resume():
	pass

def exit():
	global image
	del image

if __name__ == '__main__':
	gfw.run_main()