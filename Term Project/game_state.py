from pico2d import *
import game_framework as gfw
from game_object import *
from player import Player

def enter():
	global player
	player = Player()

def update():
	player.update()

	for b in Bullet.bullets:
		b.update()

def draw():
	player.draw()

	for b in Bullet.bullets:
		b.draw()

def handle_event(e):
	global player

	if e.type == SDL_QUIT:
		gfw.quit()
	elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_q):
		gfw.quit()
	elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
		gfw.pop()

	player.handle_event(e)

def pause():
	pass

def resume():
	pass

def exit():
	pass

if __name__ == '__main__':
	gfw.run_main()