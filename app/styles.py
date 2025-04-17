# code for the custom styles

import time
from rich import print

def print_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def p_magenta(text):
    print("[bold magenta]" + text + "[/bold magenta]")
