import traceback

from display.drawer import CursesScreen
from main_loop import MainLoop

# Get essential 0 initialized components
# get display
game_window = CursesScreen()
# get input
game_input = game_window.get_input
# get sound
# get others

# set main
main = MainLoop(game_window, game_input, 60)
try:
	main.run()
except Exception as e:
	game_window.close()
	traceback.print_exc()
	print str(e)
	exit(1)
game_window.close()

