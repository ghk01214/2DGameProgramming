from pico2d import *
import gfw
from game_object import *
from player import Player
from background import Background
from platform import Platform
from tile import Tile
from collision import check_collision
import stage_gen
import pickle

FILENAME = 'save.data'

def enter():
	gfw.world.init(['background', 'tile', 'save', 'bullet', 'platform', 'spike', 'player'])

	global background, tile, player, stage_num
	stage_num = 1
	
	player = Player()
	gfw.world.add(gfw.layer.player, player)

	background = Background('background.png', player)
	gfw.world.add(gfw.layer.background, background)

	tile = Tile('res/tile_background.json', 'res/bitmap/tileset.png', player)
	gfw.world.add(gfw.layer.tile, tile)

	stage_gen.load(resBM('../stage_%d.txt' % stage_num))
	save()

def exit():
	pass

def update():
	global player, stage_num
	x, y = player.pos

	gfw.world.update()

	if x > get_canvas_width():
		stage_num += 1
		stage_gen.remove()
		stage_gen.load(resBM('../stage_%d.txt' % stage_num))

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
		elif e.key == SDLK_r:
			load()
		elif e.key == SDLK_s:
			save()

	if player.handle_event(e):
		return

def pause():
	pass

def resume():
	pass

def save():
	global background, tile, player, stage_num

	with open(FILENAME, "wb") as file:
		pickle.dump(stage_num, file)
		pickle.dump(background.pos, file)
		pickle.dump(tile.scroll_x, file)		
		pickle.dump(player.pos, file)

def load():
	global background, tile, player, stage_num

	try:
		with open(FILENAME, "rb") as file:
			stage_num = pickle.load(file)
			background.pos = pickle.load(file)
			tile.scroll_x = pickle.load(file)
			player.pos = pickle.load(file)

		stage_gen.remove()
	except:
		print("No save file")

	stage_gen.load(resBM('../stage_%d.txt' % stage_num))

if __name__ == '__main__':
	gfw.run_main()