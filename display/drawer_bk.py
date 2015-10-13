import curses


class CursesScreen:
	def __init__(self):
		self.key = ''
		self.window = curses.initscr()
		curses.raw()
		curses.noecho()
		curses.nonl()
		curses.start_color()
		curses.use_default_colors()
		self.max_colors = 1
		self.init_colors()
		self.window.nodelay(True)
		self.window.keypad(True)
		curses.curs_set(0)
		self.max_y, self.max_x = self.window.getmaxyx()

		self.print_pallet()

	def init_colors(self):
		for i in range(20, 40):
			curses.init_color(i, (i-20)*50, (i-20)*50, (i-20)*50)
			curses.init_pair(i, i-5, i)
			self.max_colors += 1

	def print_pallet(self):
		i = 20
		while i < 19 + self.max_colors:
			self.draw(i, 20, str(i)[1], curses.color_pair(i))
			i += 1
		pass

	def close(self):
		curses.nocbreak()
		curses.curs_set(1)
		self.window.keypad(0)
		curses.nl()
		curses.echo()
		curses.endwin()

	def get_input(self):
		try:
			return self.window.getkey()
		except:
			return ''

	def draw(self, x, y, string, att=None):
		y = self.max_y - 1 - y
		try:
			if att:
				self.window.addstr(y, x, str(string), att)
			else:
				self.window.addstr(y, x, str(string))
		except:
			pass



	def refresh(self):
		self.window.refresh()
