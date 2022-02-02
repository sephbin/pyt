import pygame
import pygame.locals
import configparser

# define a main function
def load_tile_table(filename, width, height):
	image = pygame.image.load(filename).convert_alpha()#.convert()
	image_width, image_height = image.get_size()
	tile_table = []
	for tile_x in range(0, int(image_width/width)):
		line = []
		tile_table.append(line)
		for tile_y in range(0, int(image_height/height)):
			rect = ( tile_y*height, tile_x*width, width, height)
			line.append(image.subsurface(rect))
	return tile_table
class Level(object):
	def load_file(self, filename="level.map"):
		self.map = []
		self.key = {}
		parser = configparser.ConfigParser()
		parser.read(filename)
		self.tileset = parser.get("level", "tileset")
		self.map = parser.get("level", "map").split("\n")
		print(self.map)
		for section in parser.sections():
			if len(section) == 1:
				desc = dict(parser.items(section))
				self.key[section] = desc
		self.width = int(len(self.map[0])/2)
		self.height = int(len(self.map)/2)


	def get_tile(self, x, y):
		"""Tell what's at the specified position of the map."""
		try:
			char = self.map[y][x*2]
		except IndexError:
			return {}
		try:
			return self.key[char]
		except KeyError:
			return {}

	def get_bool(self, x, y, name):
		"""Tell if the specified flag is set for position on the map."""
		value = self.get_tile(x, y).get(name)
		return value in (True, 1, 'true', 'yes', 'True', 'Yes', '1', 'on', 'On')

	def is_wall(self, x, y):
		"""Is there a wall?"""
		return self.get_bool(x, y, 'wall')

	def is_blocking(self, x, y):
		"""Is this place blocking movement?"""
		if not 0 <= x < self.width or not 0 <= y < self.height:
			return True
		return self.get_bool(x, y, 'block')
	def render(self):
		MAP_TILE_WIDTH = 34
		MAP_TILE_HEIGHT = 34
		MAP_CACHE = {'ground.png': load_tile_table('ground.png', MAP_TILE_WIDTH, MAP_TILE_HEIGHT), }
		tiles = MAP_CACHE[self.tileset]
		image = pygame.Surface((self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
		overlays = {}
		print(self.map)
		for map_y, line in enumerate(self.map):
			for map_x, c in enumerate(line):
				if map_x % 2 == 0:
					try:
						print(">>",self.key, c)
						tile = self.key[c]['tile'].split(',')
						tile = int(tile[0])+int(line[map_x+1]), int(tile[1])
					except (ValueError, KeyError):
						# Default to ground tile
						tile = 0, 0
					tile_image = tiles[tile[0]][tile[1]]
					offset = map_y % 2
					print(map_x/2*48+(offset*24),)
					image.blit(tile_image,(map_x/2*48+(offset*24), map_y*15))
		return image, overlays
def main():
	# pygame.init()
	# pygame.display.set_caption("minimal program")
	# screen = pygame.display.set_mode((500, 500))
	# # screen.fill((255, 0, 0))
	# table = load_tile_table("ground.png", 34, 34)
	# table = [item for sublist in table for item in sublist]
	# print(table)
	# tileList =	[
	# 			[0,1,1,0,0,0,0],
	# 			 [0,1,0,1,1,0],
	# 			[0,0,0,0,1,1,0],
	# 			 [0,0,0,1,1,1],
	# 			[0,0,0,0,2,1,0],
	# 			 [0,1,0,1,1,1],
	# 			[0,1,1,0,0,0,0],
	# 			 [0,1,0,1,1,0],
	# 			[0,0,0,0,1,1,0],
	# 			 [0,0,0,1,1,1],
	# 			[0,0,0,0,0,1,0],
	# 			 [0,1,2,3,4,5],
	# 			]
	# for x, row in enumerate(tileList):
	# 	for y, tile in enumerate(row):
	# 		offset = x % 2
	# 		screen.blit(table[tile], (y*48+(offset*24), x*15))
	# pygame.display.flip()
	screen = pygame.display.set_mode((424, 320))

	MAP_TILE_WIDTH = 34
	MAP_TILE_HEIGHT = 34
	MAP_CACHE = {'ground.png': load_tile_table('ground.png', MAP_TILE_WIDTH, MAP_TILE_HEIGHT), }

	level = Level()
	level.load_file('level.map')

	clock = pygame.time.Clock()

	background, overlay_dict = level.render()
	overlays = pygame.sprite.RenderUpdates()

	# for (x, y), image in overlay_dict.items():
	# 	print(x,y,image)
	# 	overlay = pygame.sprite.Sprite(overlays)
	# 	overlay.image = image
	# 	overlay.rect = image.get_rect().move(x * 24, y * 16 - 16)
	screen.blit(background, (0, 0))
	overlays.draw(screen)
	pygame.display.flip()
	running = True
	while running:
		# event handling, gets all event from the event queue
		for event in pygame.event.get():
			# only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False






# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
	# call the main function
	main()