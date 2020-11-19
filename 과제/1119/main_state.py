from pico2d import *
import gfw
import player
import generator
import background

def enter():
	gfw.world.init(['background', 'missile', 'player'])	
	background.init(player)
	player.init()
	generator.init()
	gfw.world.add(gfw.layer.background, background)
	gfw.world.add(gfw.layer.player, player)

def exit():
	pass

def update():
	gfw.world.update()
	generator.update()
	check_collision()

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

	player.handle_event(e)

# 충돌체크는 들키지 않을 정도로 적당히 해야 하므로 제곱근을 구하는 것보다 제곱을 구하는 것이 효율적이다.
def collides_distance(a, b):
	ax, ay = a.pos
	bx, by = b.pos
	
	distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
	radius_sum = a.radius + b.radius

	return distance_sq < radius_sum ** 2

def check_collision():
	for m in gfw.world.objects_at(gfw.layer.missile):
		if collides_distance(player, m):
			gfw.world.remove(m)

if __name__ == '__main__':
	gfw.run_main()