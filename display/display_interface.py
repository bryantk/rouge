class DisplayAdapter(object):
	def __init__(self):
		"""
		Create a game window and related data
		max_x and max_y
		colors
		etc.
		"""
		raise NotImplementedError()

	def get_input(self):
		"""
		Get player input. May be from a different module
		Handle keyboard, mouse, gamepad
		:return: Defined keycode of input
		"""
		raise NotImplementedError()

	def close(self):
		"""
		Everything required for a clean exit
		:return:
		"""
		raise NotImplementedError()

	def resize(self, new_x, new_y):
		"""
		Resize the terminal to new_x and new_y lines
		:param new_x:
		:param new_y:
		:return:
		"""
		raise NotImplementedError()

	def get_dimensions(self):
		"""
		Get x and y of current screen
		:return: screen_x, screen_y
		"""
		raise NotImplementedError()

	def draw(self, x, y, content, **kwargs):
		"""
		draw content at x,y (bottom-left = 0,0)
		:param x: x from left
		:param y: y from bottom
		:param content: content to print
		:param kwargs: options
		:return:
		"""
		raise NotImplementedError()

	def refresh(self):
		"""
		Refresh the display
		:return:
		"""
		raise NotImplementedError()

	def has_colors(self):
		"""
		can the terminal do colors?
		:return: True/False
		"""
		raise NotImplementedError()

	# do research and define
	def draw_character(self, x, y, char, **kwargs):
		"""
		Draw a single character at x,y
		:return:
		"""
		if len(char) != 1:
			raise Exception
		self.draw(x, y, char, **kwargs)

	def draw_text(self, rect, text, **kwargs):
		"""
		Draw text within rectangle. Auto-caps to display bounds?
		:param rect:location
		:param text:
		:param kwargs: justify=['left', 'right', 'center']
		:return:
		"""
		raise NotImplementedError()

	def draw_choices(self, rect, choices, layout='vertical', **kwargs):
		"""

		:param rect: location
		:param choices:
		:param layout: 'vertical' or 'horizontal'
		:param kwargs: toggle, colors
		:return:
		"""
		raise NotImplementedError()

	def draw_bar(self, rect, layout='horizontal', direction='right', invert=False, **kwargs):
		"""

		:param rect: location
		:param layout: 'vertical' or 'horizontal'
		:param direction: location
		:param invert: F = color on black, T = black on color
		:param kwargs:
		:return:
		"""
		raise NotImplementedError()

	def draw_window(self, rect):
		"""

		:param rect:
		:return:
		"""
		raise NotImplementedError()

