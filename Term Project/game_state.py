from pico2d import *
import gfw
from game_object import *
from player import Player
#from background import Background
from platform import Platform
from tile import Background
import stage_gen

def enter():
	gfw.world.init(['background', 'platform', 'player', 'bullet'])
	center = get_canvas_width() // 2, get_canvas_height() // 2
	#background = Background('stage_5.png')
	background = Background('res/stage_1.json', 'res/bitmap/tileset.png')
	gfw.world.add(gfw.layer.background, background)

	global player
	player = Player()
	player.background = background
	gfw.world.add(gfw.layer.player, player)

	stage_gen.load(resBM('../stage_1.txt'))
def exit():
	pass

def update():
	gfw.world.update()
	#dx = -300 * gfw.delta_time
	#check_block()
	stage_gen.update()

def draw():
	gfw.world.draw()
	draw_collision_box()

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