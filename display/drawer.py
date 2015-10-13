import platform

from curses import *
from display_interface import DisplayAdapter


class CursesScreen(DisplayAdapter):
	def __init__(self):
		self.window = initscr()
		raw()
		noecho()
		nonl()
		start_color()
		use_default_colors()
		self.max_colors = 1
		self.window.nodelay(True)
		self.window.keypad(True)
		curs_set(0)
		self.max_x, self.max_y = self.get_dimensions()
		self.platform = platform.system().lower()

		#self.init_colors()
		#self.print_pallet()

	def init_colors(self):
		for i in range(20, 40):
			init_color(i, (i-20)*50, (i-20)*50, (i-20)*50)
			init_pair(i, i-5, i)
			self.max_colors += 1

	def print_pallet(self):
		i = 20
		while i < 19 + self.max_colors:
			self.draw(i, 20, str(i)[1], color_pair(i))
			i += 1
		pass

	def get_input(self):
		try:
			return self.window.getkey()
		except:
			return ''

	def close(self):
		nocbreak()
		curs_set(1)
		self.window.keypad(0)
		nl()
		echo()
		endwin()

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

	def has_colors(self):
		return has_colors()

	def resize(self, new_x, new_y):
		if self.platform == 'linux':
			print '\x1b[8;{};{}t'.format(new_y, new_x)
		resizeterm(new_y, new_x)
		self.max_x, self.max_y = self.get_dimensions()

	def get_dimensions(self):
		y, x = self.window.getmaxyx()
		return x, y
