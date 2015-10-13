class Rect:
	def __init__(self, x, y, width=0, height=0, x_end=0, y_end=0):
		"""
		Draw a rectangle with x,y being the bottom-left
		:param x:
		:param y:
		:param width:
		:param height:
		:param x_end:
		:param y_end:
		:return:
		"""
		if not width:
			if x_end:
				self.width = abs(x_end - x)
				self.x = min(x, x_end)
			else:
				raise Exception
		else:
			self.x = x
			self.width = width

		if not height:
			if y_end:
				self.height = abs(y_end - y)
				self.y = min(y, y_end)
			else:
				raise Exception
		else:
			self.y = y
			self.height = height

	def __str__(self):
		return '({},{}) to ({},{}) - width={} height={}'.format(
			self.x, self.y, self.x+self.width, self.y+self.height, self.width,
			self.height)
