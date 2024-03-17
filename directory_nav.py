import curses
import os
import time

def create_directory_list(path):
    files = os.listdir(path)
    files.sort()
    
    return files

def list_directory(stdscr, menu, selected):
    # Clear Screen
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    for idx, row in enumerate(menu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(menu) // 2 + idx
        
        if idx == selected:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
            
def main_directory(stdscr):
    height, width = stdscr.getmaxyx()
    stats = curses.newwin(2, 20, height - 3, 1)
    
    curses.curs_set(0)
    current_row = 0
    current_path = "./Jukebox"
    menu = create_directory_list(current_path)
    list_directory(stdscr, menu, current_row)
    
    curses.doupdate()
    
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            current_path = current_path + "/" + str(menu[current_row])
            current_row = 0
        elif key == curses.KEY_BACKSPACE or key == 27:
            current_path = os.path.dirname(current_path)
            
        
        menu = create_directory_list(current_path)
        list_directory(stdscr, menu, current_row)
        curses.doupdate()
            
        
    