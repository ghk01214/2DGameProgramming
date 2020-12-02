from pico2d import *
import gfw
from game_object import *
from player import Player
#from background import Background
from platform import Platform
from tile import Background
from collision import check_collision
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

def collides_block(a, b):
	(la, ba, ra, ta) = a.get_bb()
	(lb, bb, rb, tb) = b.get_bb()

	if la > rb: return False
	if ra < lb: return False
	#if ba > tb: return False
	if ta < bb: return False

	return True

def check_block():
	for block in gfw.world.objects_at(gfw.layer.platform):
		if collides_block(player, block):
			#player.move_for = False
			print('hit', block)

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