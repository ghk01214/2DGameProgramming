from pico2d import *
import gfw
import json

class Layer:
	def __init__(self, dict):
		self.__dict__.update(dict)

class Tileset:
	def __init__(self, dict):
		self.__dict__.update(dict)
		self.rows = math.ceil((self.tilecount + 25) / self.columns)
		#print('rows: ', self.rows)

	def getRectForTile(self, tile):
		x = (tile - 1) % self.columns
		y = (tile - 1) // self.columns
		l = x * (self.tilewidth + self.spacing) + self.margin
		t = (self.rows - y - 1) * (self.tileheight + self.spacing) + self.margin

		return l, t - 8, self.tilewidth, self.tileheight

class Map:
	def __init__(self, dict):
		self.__dict__.update(dict)
		self.layers = list(map(Layer, self.layers))
		self.tilesets = list(map(Tileset, self.tilesets))

class Tile:
	def __init__(self, json_fn, tile_fn, player):
		with open(json_fn) as f:
			self.map = Map(json.load(f))

		self.image = gfw.image.load(tile_fn)
		self.width = self.map.tilewidth * self.map.width
		self.height = self.map.tileheight * self.map.height - 8
		self.tileset = self.map.tilesets[0]
		self.layer = self.map.layers[0]
		self.wraps = True
		self.player = player
		self.scroll_x = 0

	def get_boundary(self):
		return 0, 0, self.width, self.height

	def update(self):
		px, py = self.player.pos

		if px > get_canvas_width():
			self.scroll_x += get_canvas_width()

	def draw(self):
		sx, sy = round(self.scroll_x), 0

		if self.wraps:
			sx %= self.width

			if sx < 0:
				sx += self.width

			sy %= self.height

			if sy <0:
				sy += self.height

		cw, ch = get_canvas_width(), get_canvas_height()

		tile_x = sx // self.map.tilewidth
		tile_y = sy // self.map.tileheight
		beg_x = -(sx % self.map.tilewidth)
		beg_y = -(sy % self.map.tileheight)

		db = beg_y
		ty = tile_y

		while ty < self.layer.height and db < ch:
			if ty >= 0:
				dl = beg_x
				dr = beg_x + self.map.tilewidth
				tx = tile_x
				ti = (self.map.height - ty - 1) * self.map.width + tx

				while tx < self.layer.width and dl < cw:
					tile = self.layer.data[ti]
					rect = self.tileset.getRectForTile(tile)
					self.image.clip_draw_to_origin(*rect, dl, db)
					dl += self.map.tilewidth
					ti += 1
					tx += 1

			db += self.map.tileheight
			ty += 1

			if self.wraps and ty >= self.layer.height:
				ty -= self.layer.height