import curses
import time
from faces import open_smile
    
def animate_smiley(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Set stdscr.getch() to be non-blocking
    
    open_smile.draw_smiley(stdscr, up=True)
    time.sleep(0.6)
    open_smile.draw_smiley(stdscr, up=False)
    time.sleep(0.6)
    