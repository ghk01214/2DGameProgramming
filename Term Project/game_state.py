from pico2d import *
import gfw
from game_object import *
from player import Player
from background import Background

def enter():
	gfw.world.init(['background', 'player', 'bullet'])
	center = get_canvas_width() // 2, get_canvas_height() // 2
	background = Background('stage_1.png')

	global player
	player = Player()
	player.pos = background.center
	player.background = background
	background.target = player
	gfw.world.add(gfw.layer.background, background)
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