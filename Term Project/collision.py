from pico2d import *
import gfw
import player

# 충돌체크는 들키지 않을 정도로 적당히 해야 하므로 제곱근을 구하는 것보다 제곱을 구하는 것이 효율적이다.
def collides_distance(a, b):
	ax, ay = a.pos
	bx, by = b.pos
	
	distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
	radius_sum = a.radius + b.radius

	return distance_sq < radius_sum ** 2

def check_collision():
	dead, full = False, False

	for m in gfw.world.objects_at(gfw.layer.platform):
		if collides_distance(player, m):
			return True

	#for i in gfw.world.objects_at(gfw.layer.item):
	#	if collides_distance(player, i):
	#		gfw.world.remove(i)
	#		full = player.increase_life()

	#return dead, full