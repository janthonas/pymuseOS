import curses
import term_face
import directory_nav

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Make getch non-blocking
    view_mode = "smiley"  # Start in smiley animation view
    
    while True:
        if view_mode == "smiley":
            term_face.animate_smiley(stdscr)
        elif view_mode == "directory":
            directory_nav.main_directory(stdscr)

        key = stdscr.getch()
        
        # Switch view mode on arrow key press
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT]:
            view_mode = "directory" if view_mode == "smiley" else "smiley"
        elif key in [10, 13, curses.KEY_ENTER]:  # Exit on Enter
            break

# Initialize curses
curses.wrapper(main)