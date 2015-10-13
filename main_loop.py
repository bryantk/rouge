from time import time, sleep


class MainLoop:
	def __init__(self, game_window, game_input, fps=60):
		self.game_window = game_window
		self.user_inputs = game_input
		self.fps = fps
		self.time_per_frame = 1. / fps
		self.total_frames = 0
		self.game_start_time = time()
		self.game_time = 0
		self.slow_frames = 0
		self.frames = []

		self.player_input = ''
		self.running = True
		self.debug = True

	def end_game(self):
		self.running = False

	def run(self):
		original_x, original_y = self.game_window.get_dimensions()
		self.game_window.resize(60, 20)
		while self.running:
			self.total_frames += 1
			frame_start = time()
			self.game_time = frame_start - self.game_start_time
			# user input
			key = self.user_inputs()
			if key:
				self.player_input = key
			# TODO temp
			self.game_window.draw(2, 8, self.player_input + '      ')
			if key == '\x11':
				break
			# draw debug info?
			if self.debug:
				self.draw_debug()

			logic_end = time()
			# time to re-draw?
			if logic_end - frame_start < self.time_per_frame:
				self.game_window.refresh()
			draw_end = time()
			# determine timings
			frame_took = draw_end - frame_start
			sleep_time = self.time_per_frame - frame_took
			self.frames.append(frame_took)
			# if time for sleeping
			if sleep_time > 0:
				sleep(sleep_time)
			else:
				# frame took too long, do stuff!
				self.slow_frames += 1
		# END GAME
		# return terminal to original size
		if self.game_window.platform == 'linux':
			print '\x1b[8;{};{}t'.format(original_y, original_x)

	def draw_debug(self):
		self.game_window.draw(40, 1, '{:>6} seconds'.format(self.total_frames/60))
		self.game_window.draw(40, 2, '{:>6} frames'.format(self.total_frames))
		self.game_window.draw(40, 3, self.time_per_frame)
		self.game_window.draw(40, 4, '0,0 to {},{}'.format(self.game_window.max_x, self.game_window.max_y))
		self.game_window.draw(40, 6, self.game_window.platform)

