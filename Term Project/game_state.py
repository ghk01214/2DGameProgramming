from pico2d import *
import gfw
from game_object import *
from player import Player
from background import Background
from platform import Platform

def enter():
	gfw.world.init(['background', 'platform', 'player', 'bullet'])
	center = get_canvas_width() // 2, get_canvas_height() // 2
	background = Background('stage_5.png')

	global player
	player = Player()
	player.pos = background.center
	player.background = background
	background.target = player
	gfw.world.add(gfw.layer.background, background)
	
	x = 0
	canvas_w = get_canvas_width()
	
	gfw.world.add(gfw.layer.player, player)

def exit():
	pass

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			gfw.pop()
		elif e.key == SDLK_q:
			gfw.quit()

	if player.handle_event(e):
		return

def pause():
	pass

def resume():
	pass

if __name__ == '__main__':
	gfw.run_main()