from pico2d import *
import gfw
import game_object
from object import Object

class Platform(Object):
	def __init__(self, left, bottom):
		super().__init__(left, bottom)