def draw_smiley(stdscr, up):
    # Clear screen
    stdscr.clear()
    
    # Get height and width of the screen
    height, width = stdscr.getmaxyx()
    
    # Calculate center
    center_y, center_x = height // 2, width // 2
    if(up == True):
        # Eyes
        stdscr.addstr(center_y - 9, center_x - 20, "     █████                    █████   ")
        stdscr.addstr(center_y - 8, center_x - 20, "     █████                    █████   ")
        stdscr.addstr(center_y - 7, center_x - 20, "     █████                    █████   ")
        stdscr.addstr(center_y - 6, center_x - 20, "█████     █████          █████     █████")
        stdscr.addstr(center_y - 5, center_x - 20, "█████     █████          █████     █████")
        stdscr.addstr(center_y - 4, center_x - 20, "█████     █████          █████     █████")
    
        # Gap
        stdscr.addstr(center_y - 3, center_x, "")
        stdscr.addstr(center_y - 2 , center_x, "")
        stdscr.addstr(center_y - 1, center_x, "")
        
        # Mouth
        stdscr.addstr(center_y    ,  center_x - 20, "████████████████████████████████████████")
        stdscr.addstr(center_y + 1,  center_x - 20, "████████████████████████████████████████")
        stdscr.addstr(center_y + 2,  center_x - 20, "████████████████████████████████████████")
        stdscr.addstr(center_y + 3,  center_x - 20, "████████████████████████████████████████")
        stdscr.addstr(center_y + 4,  center_x - 20, "██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████")
        stdscr.addstr(center_y + 5,  center_x - 20, "██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████")
        stdscr.addstr(center_y + 6,  center_x - 20, "     █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████     ")
        stdscr.addstr(center_y + 7,  center_x - 20, "     █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████     ")
        stdscr.addstr(center_y + 8, center_x - 20, "     █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████     ")
        
    elif(up == False):
        # Eyes
        stdscr.addstr(center_y - 8, center_x - 20, "     █████                    █████   ")
        stdscr.addstr(center_y - 7, center_x - 20, "     █████                    █████   ")
        stdscr.addstr(center_y - 6, center_x - 20, "     █████                    █████   ")
        stdscr.addstr(center_y - 5, center_x - 20, "█████     █████          █████     █████")
        stdscr.addstr(center_y - 4, center_x - 20, "█████     █████          █████     █████")
        stdscr.addstr(center_y - 3, center_x - 20, "█████     █████          █████     █████")
        
        # Gap
        stdscr.addstr(center_y - 2, center_x, "")
        stdscr.addstr(center_y - 1, center_x, "")
        stdscr.addstr(center_y    , center_x, "")
        
        # Mouth
        stdscr.addstr(center_y + 1,  center_x - 20, "████████████████████████████████████████")
        stdscr.addstr(center_y + 2,  center_x - 20, "████████████████████████████████████████")
        stdscr.addstr(center_y + 3,  center_x - 20, "████████████████████████████████████████")
        stdscr.addstr(center_y + 4,  center_x - 20, "████████████████████████████████████████")
        stdscr.addstr(center_y + 5,  center_x - 20, "██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████")
        stdscr.addstr(center_y + 6,  center_x - 20, "██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████")
        stdscr.addstr(center_y + 7,  center_x - 20, "     █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████     ")
        stdscr.addstr(center_y + 8, center_x - 20, "     █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████     ")
        stdscr.addstr(center_y + 9, center_x - 20, "     █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████     ")
    
    # Refresh to draw
    stdscr.refresh()