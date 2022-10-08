from pico2d import *
import gfw
import player
import generator
import background
from collision import check_collision

STATE_IN_GAME, STATE_GAME_OVER = range(2)
SCORE_COLOR = (255, 255, 255)

def enter():
	gfw.world.init(['background', 'missile', 'item', 'player'])

	background.init()
	player.init()
	generator.init()
	
	gfw.world.add(gfw.layer.background, background)
	gfw.world.add(gfw.layer.player, player)

	global gg_image, font
	gg_image = gfw.image.load('res/game_over.png')
	font = gfw.font.load('res/ConsolaMalgun.ttf', 35)

	global state, score
	state = STATE_IN_GAME
	score = 0

def exit():
	pass

def update():
	global state, score

	if state!= STATE_IN_GAME:
		return

	score += gfw.delta_time

	gfw.world.update()
	generator.update(score)
	dead, full = check_collision()

	if dead:
		end_game()
	
	if full:
		score += 5

def draw():
	gfw.world.draw()
	score_pos = 30, get_canvas_height() - 30
	font.draw(*score_pos, 'ScoreL %.1f' % score, SCORE_COLOR)

	if state == STATE_GAME_OVER:
		x, y = get_canvas_width() // 2, get_canvas_height() // 2
		gg_image.draw(x, y)

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			gfw.pop()
		elif e.key == SDLK_q:
			gfw.quit()

	player.handle_event(e)

def end_game():
	global state
	state = STATE_GAME_OVER

if __name__ == '__main__':
	gfw.run_main()