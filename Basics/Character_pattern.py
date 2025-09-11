import os
import random
import time
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

ascii_chars = ["#", "@", "%", "&", "$", "*", "+", "=", "-", ".", " "]

def random_color():
    return f"\033[38;2;{random.randint(0,255)};{random.randint(0,255)};{random.randint(0,255)}m"

def generate_frame(width, height):
    frame = ""
    for _ in range(height):
        for _ in range(width):
            char = random.choice(ascii_chars)
            color = random_color()
            frame += f"{color}{char}"
        frame += "\033[0m\n"
    return frame

def animated_ascii_art():
    width, height = 100, 30 
    try:
        while True:
            clear_screen()
            frame = generate_frame(width, height)
            print(frame)
            time.sleep(0.1) 
    except KeyboardInterrupt:
        clear_screen()
        print("Animation stopped. Have a colorful day!")
        sys.exit()

if __name__ == "__main__":
    animated_ascii_art()
