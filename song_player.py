import pygame
import curses
import time
from mutagen.mp3 import MP3

# Initialize pygame mixer
pygame.mixer.init(frequency=44100)

def get_song_duration(file_path):
    audio = MP3(file_path)
    return audio.info.length

def update_display(stdscr, duration, elapsed_time):
    stdscr.clear()
    stdscr.addstr(f"Duration: {duration:.2f}s\n")
    stdscr.addstr(f"Current Position: {elapsed_time:.2f}s\n")
    stdscr.addstr("Press 'p' to pause/unpause. Left/Right arrows to seek.\n")
    stdscr.refresh()

def play_song(stdscr, file_path):
    duration = get_song_duration(file_path)
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    start_time = time.time()
    paused = False
    pause_start = 0
    
    while pygame.mixer.music.get_busy() or paused:
        elapsed_time = time.time() - start_time
        update_display(stdscr, duration, elapsed_time if not paused else pause_start - start_time)
        
        # Non-blocking key input
        stdscr.nodelay(True)
        try:
            key = stdscr.getch()
            if key == ord('p'):
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    start_time += time.time() - pause_start  # Adjust start_time based on pause duration
                else:
                    pygame.mixer.music.pause()
                    paused = True
                    pause_start = time.time()
            elif key == curses.KEY_RIGHT and not paused:  # Seek forward
                # Adjusting start_time backward moves the perceived position forward
                start_time -= 5
                pygame.mixer.music.rewind()
                pygame.mixer.music.set_pos(elapsed_time - 5 if elapsed_time > 5 else 0)
            elif key == curses.KEY_LEFT and not paused:  # Seek backward
                # Adjusting start_time forward moves the perceived position backward
                start_time += 5
                pygame.mixer.music.rewind()
                # We use set_pos to jump to the desired position; it works from the start of the track
                pygame.mixer.music.set_pos(elapsed_time + 5)
        except curses.error:
            pass  # No input

        time.sleep(0.1)

def curses_wrapper(file_path):
    curses.wrapper(play_song, file_path)

file_path = './Jukebox/Even_Flow.mp3'  # Replace with your MP3 file path
curses_wrapper(file_path)

