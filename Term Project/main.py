from pico2d import *
import gfw
from game_object import *
import end
from player import Player
from background import Background
from tile import Tile
import stage_gen
import pickle
import music

FILENAME = 'save.dat'

def enter():
	gfw.world.init(['background', 'tile', 'bullet', 'save', 'platform', 'spike', 'player'])

	global background, tile, player, stage_num, bgm
	stage_num = 1
	bgm = music.mp3(resSE('stage_%d.mp3' % stage_num), True)
	
	player = Player()
	gfw.world.add(gfw.layer.player, player)

	background = Background('background.png', player)
	gfw.world.add(gfw.layer.background, background)

	tile = Tile('res/tile_background.json', 'res/bitmap/tileset.png', player)
	gfw.world.add(gfw.layer.tile, tile)

	stage_gen.load(resBM('../stage_%d.txt' % stage_num), False)
	save()

def exit():
	pass

def update():
	global player, stage_num, bgm
	x, y = player.pos

	gfw.world.update()

	if x > get_canvas_width():
		x = 14
		player.pos = x, y
		stage_num += 1
		stage_gen.remove()
		bgm = music.mp3(resSE('stage_%d.mp3' % stage_num), True)
		stage_gen.load(resBM('../stage_%d.txt' % stage_num))

		if stage_num == 3:
			bgm.set_volume(128)
		else:
			bgm.set_volume(64)

	if player.saved:
		save()
		player.saved = False

	if y < -10:
		bgm.stop()
		gfw.change(end)

	stage_gen.update()

def draw():
	gfw.world.draw()
	#draw_collision_box()

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key in [SDLK_ESCAPE, SDLK_q]:
			gfw.quit()
		elif e.key == SDLK_r:
			load()
			player.revived = True
		elif e.key == SDLK_d:
			player.state = 6
		elif e.key == SDLK_s and player.state !=6:
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
		pickle.dump(player.state, file)
		pickle.dump(player.action, file)
		pickle.dump(player.width, file)
		pickle.dump(player.imageType, file)

def load():
	global background, tile, player, stage_num, bgm

	temp_stage = stage_num

	try:
		with open(FILENAME, "rb") as file:
			stage_num = pickle.load(file)
			background.pos = pickle.load(file)
			tile.scroll_x = pickle.load(file)
			player.pos = pickle.load(file)
			player.state = pickle.load(file)
			player.action = pickle.load(file)
			player.width = pickle.load(file)
			player.imageType = pickle.load(file)

		player.delta = 0
		player.frame = 0
	except:
		print("No save file")

	if temp_stage != stage_num:
		stage_gen.remove()
		bgm = music.mp3(resSE('stage_%d.mp3' % stage_num), True)
		stage_gen.load(resBM('../stage_%d.txt' % stage_num))

	if stage_num == 3:
		bgm.set_volume(80)

if __name__ == '__main__':
	gfw.run_main()