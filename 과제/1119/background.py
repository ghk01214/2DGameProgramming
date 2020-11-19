from pico2d import *
import gfw

def init(p):
	global space, stars, player
	space = gfw.image.load('res/outerspace.png')
	stars = gfw.image.load('res/stars.png')
	player = p

def update():
	pass

def draw():
	x, y = get_canvas_width() // 2, get_canvas_height() // 2
	px, py = player.pos
	dx, dy = px - x, py - y

	space.draw(x + dx * 0.2, y + dy * 0.2)
	stars.draw(x + dx * 0.5, y + dy * 0.5)