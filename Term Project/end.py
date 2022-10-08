from pico2d import *
import gfw
import game_object
import music
from background import Background
from player import Player
import stage_gen

def enter():
	gfw.world.init(['background', 'bullet', 'save', 'platform', 'spike', 'player', 'clear'])

	global background, clear, bgm, victory, player, victory_time, play_bgm, play_clear

	play_bgm = 0
	play_clear = 0
	victory_time = 0

	player = Player()
	player.pos = 335, get_canvas_height()
	player.state = 5
	player.action = 1
	gfw.world.add(gfw.layer.player, player)

	background = Background('ending.png', player)
	gfw.world.add(gfw.layer.background, background)

	clear = Background('game_clear.png', player)
	clear.ch = 200
	clear.draw_pos = 0, 200

	stage_gen.load(game_object.resBM('../ending.txt'), True)

def update():
	global victory_time, victory, play_bgm, bgm, play_clear, player
	x, y = player.pos
	victory_time += gfw.delta_time

	if victory_time > 1.0:
		play_clear += 1

		if play_clear == 1:
			victory = music.mp3(game_object.resSE('game_clear.mp3'), True)

	if victory_time > 7.0:
		play_bgm += 1

		if play_bgm == 1:
			victory.stop()
			bgm = music.mp3(game_object.resSE('ending.mp3'), True)
		elif play_bgm == 50:
			gfw.world.add(gfw.layer.clear, clear)

	if x + 10 > get_canvas_width():
		x = get_canvas_width() - 10
		player.pos = x, y

	gfw.world.update()
	stage_gen.update()

def draw():
	gfw.world.draw()
	#game_object.draw_collision_box()

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key in [SDLK_ESCAPE, SDLK_q]:
			gfw.quit()

	if player.handle_event(e):
		return

def pause():
	pass

def resume():
	pass

def exit():
	pass

if __name__ == '__main__':
	gfw.run_main()