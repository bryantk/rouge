class Logic:
	def __init__(self):
		self.game_data = None
		self.window = None
		self.inputs = []
		self.last_input = 0

		self.x = 1
		self.y = 1

	def get_input(self):
		key = self.window.get_input()
		if key == 'Q':
			self.game_data.running = False
		if key:
			self.inputs.append(key)
			if not self.last_input:
				self.last_input = self.game_data.game_time

	def logic(self):
		if self.last_input and self.game_data.game_time > self.last_input - 1:
			if '\x11' in self.inputs:
				self.game_data.end_game()
			self.window.draw(self.x, self.y, ' ')
			if 'KEY_DOWN' in self.inputs:
				self.y -= 1
			elif 'KEY_UP' in self.inputs:
				self.y += 1
			elif 'KEY_RIGHT' in self.inputs:
				self.x += 1
			elif 'KEY_LEFT' in self.inputs:
				self.x -= 1
			self.last_input = 0
			# do input
			self.inputs = []

		self.window.draw(self.x, self.y, '@')

		self.window.draw(40, 5, '{},{}'.format(self.x, self.y))
